from fastapi import FastAPI
from src.parser import ScriptParser
from src.voice import VoiceManager
from src.audio import AudioGenerator
from src.app import create_gradio_interface

# Initialize FastAPI app
app = FastAPI()

# Initialize components
parser = ScriptParser()
voice_manager = VoiceManager()
audio_gen = AudioGenerator()

# API Routes
@app.post("/upload")
async def upload_script(file):
    """
    1. Receive FDX file
    2. Pass to parser
    3. Return parsed characters and dialogue
    """

@app.post("/assign-voices")
async def assign_voices(character_list):
    """
    1. Receive list of characters
    2. Use voice manager to assign voices
    3. Return voice assignments
    """

@app.post("/generate-audio")
async def generate_audio(dialogue_data):
    """
    1. Receive dialogue and voice assignments
    2. Generate audio using Cartesia
    3. Return audio file/stream
    """

# Mount Gradio interface
app.mount("/ui", create_gradio_interface())