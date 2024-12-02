from cartesia import CartesiaAPI
from typing import Dict, List

class VoiceManager:
    def __init__(self):
        """
        1. Initialize Cartesia client
        2. Load available voices
        """
        self.client = CartesiaAPI()
        self.available_voices = {}
        
    def get_available_voices(self) -> List:
        """
        1. Call Cartesia API for voice list
        2. Cache voice information
        3. Return formatted voice list
        """
        
    def assign_voices(self, characters: List[str]) -> Dict:
        """
        1. Take list of characters
        2. Match with available voices
        3. Return character-voice mapping
        """
        
    def update_voice_assignment(self, character: str, voice_id: str):
        """
        1. Validate voice ID
        2. Update character-voice mapping
        3. Return updated assignment
        """