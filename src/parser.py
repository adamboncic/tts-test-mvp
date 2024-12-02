# src/parser.py
from typing import Dict, List, Optional
import xml.etree.ElementTree as ET
from dataclasses import dataclass
import logging

@dataclass
class DialogueLine:
    character: str
    text: str
    scene: str
    page: int
    sequence: int

class ScriptParser:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.dialogue_sequence: List[DialogueLine] = []
        self.characters: Dict[str, List[DialogueLine]] = {}

    def parse_fdx(self, content: bytes) -> Dict:
        """Parse FDX file content and extract structured data."""
        try:
            root = ET.fromstring(content)
            
            # Track parsing context
            current_scene = ""
            current_page = 1
            sequence_counter = 0
            
            # Find all paragraphs
            for paragraph in root.findall(".//Paragraph"):
                para_type = paragraph.get("Type", "")
                
                # Update scene tracking
                if para_type == "Scene Heading":
                    current_scene = self._get_text_content(paragraph)
                
                # Extract dialogue
                elif para_type == "Character":
                    character = self._get_text_content(paragraph)
                    dialogue = self._get_next_dialogue(paragraph)
                    
                    if dialogue:
                        sequence_counter += 1
                        line = DialogueLine(
                            character=character,
                            text=dialogue,
                            scene=current_scene,
                            page=current_page,
                            sequence=sequence_counter
                        )
                        
                        # Store by character
                        if character not in self.characters:
                            self.characters[character] = []
                        self.characters[character].append(line)
                        
                        # Store in sequence
                        self.dialogue_sequence.append(line)
                
                # Track page numbers
                if "Page" in paragraph.attrib:
                    current_page = int(paragraph.get("Page"))
            
            return self._build_response()
            
        except ET.ParseError as e:
            self.logger.error(f"XML parsing error: {e}")
            raise ValueError(f"Invalid FDX format: {e}")
        except Exception as e:
            self.logger.error(f"Parsing error: {e}")
            raise

    def _get_text_content(self, element: ET.Element) -> str:
        """Extract clean text content from an XML element."""
        return "".join(element.itertext()).strip()

    def _get_next_dialogue(self, character_elem: ET.Element) -> Optional[str]:
        """Get dialogue text following a character element."""
        next_elem = character_elem.getnext()
        if next_elem is not None and next_elem.get("Type") == "Dialogue":
            return self._get_text_content(next_elem)
        return None

    def _build_response(self) -> Dict:
        """Build structured response from parsed data."""
        return {
            "characters": list(self.characters.keys()),
            "dialogue_count": len(self.dialogue_sequence),
            "scenes": self._get_scene_summary(),
            "dialogue_sequence": [
                {
                    "character": line.character,
                    "text": line.text,
                    "scene": line.scene,
                    "page": line.page,
                    "sequence": line.sequence
                }
                for line in self.dialogue_sequence
            ]
        }

    def _get_scene_summary(self) -> List[Dict]:
        """Generate scene summary with dialogue counts."""
        scenes = {}
        for line in self.dialogue_sequence:
            if line.scene not in scenes:
                scenes[line.scene] = {
                    "dialogue_count": 0,
                    "characters": set()
                }
            scenes[line.scene]["dialogue_count"] += 1
            scenes[line.scene]["characters"].add(line.character)
        
        return [
            {
                "scene": scene,
                "dialogue_count": data["dialogue_count"],
                "characters": list(data["characters"])
            }
            for scene, data in scenes.items()
        ]

    def get_character_lines(self, character: str) -> List[DialogueLine]:
        """Get all dialogue lines for a specific character."""
        return self.characters.get(character, [])

    def get_dialogue_sequence(self) -> List[DialogueLine]:
        """Get complete dialogue sequence."""
        return self.dialogue_sequence