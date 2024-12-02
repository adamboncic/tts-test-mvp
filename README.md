# TTS Script Reader MVP

A proof-of-concept application for converting screenplay files (FDX format) into AI-voiced audio using the Cartesia TTS API.

## Features

- FDX screenplay file parsing
- Character and dialogue extraction
- AI voice assignment per character
- Real-time audio generation
- Basic playback functionality

## Tech Stack

- Python 3.9+
- FastAPI
- Gradio
- Cartesia API
- XML parsing libraries

## Project Structure

```
script_reader/
├── src/
│   ├── parser.py      # FDX parsing
│   ├── voice.py       # Cartesia integration
│   ├── audio.py       # Audio generation
│   └── app.py         # Gradio interface
├── main.py            # FastAPI setup
└── .env
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/adamboncic/tts-test-mvp.git
cd tts-test-mvp
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn gradio cartesia python-multipart
```

4. Create a `.env` file:
```
CARTESIA_API_KEY=your_api_key_here
```

5. Run the application:
```bash
uvicorn main:app --reload
```

## Development Status

This is an MVP (Minimum Viable Product) focused on validating:
- FDX parsing functionality
- Character extraction reliability
- Voice assignment feasibility
- Real-time audio generation performance