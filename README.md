# Voice Assistant Project

### Overview
This project is a **Voice Assistant** to perform a variety of tasks, including:
- Answering general questions.
- Playing music directly from YouTube.
- Fetching live weather updates for any location.
- Setting reminders with notifications.
- Live interaction through voice commands and responses.

The assistant integrates **Flask** for the backend and a robust **chat-based UI** to display conversations in real-time.

### Features
- **Voice Input and Output**: The assistant listens to your queries and responds with synthesized speech.
- **Music Playback**: Plays music directly from YouTube using **yt-dlp** and **VLC**.
- **Weather Updates**: Provides live weather information powered by Open-Meteo API.
- **Reminder System**: Sets reminders and notifies at the specified time.
- **Interactive Chat UI**: Displays the conversation for better user experience.

---

### Installation

#### Prerequisites
- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

#### Setup Instructions

1. Create and activate a conda environment:
   ```bash
   conda create -p ./env python==3.11 -y
   conda activate ./env  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the Flask app:
   - Navigate to the `app.py` file.
   - Run the application:
     ```bash
     python main.py
     ```
   - Open the application in your browser at `http://127.0.0.1:5000`.

---

### Usage
1. Open the app in your browser.
2. Provide your **Groq API Key**.
3. Interact with the voice assistant using the **chat UI** or your voice:
   - Click **Speak** to start.
   - Click **Interrupt** to stop a response midway.
   - Click **Exit** to leave the current functionality.
   - Click **Quit** to stop the assistant and return to the API key entry page.

---

### File Structure
```plaintext
voice-assistant/
│
├── app.py                   # Main Flask application
├── modules/
│   ├── qna.py               # Handles Q&A functionality
│   ├── music.py             # Handles music playback
│   ├── weather.py           # Fetches weather data
│   ├── reminder.py          # Manages reminders
│   ├── speech.py            # Handles text-to-speech and speech recognition
│   ├── utils.py             # Helper functions like time normalization
│
├── prompts/
│   ├── location_prompt.py   # Handles location few-shot examples and prompt template
│   ├── music_prompt.py      # Handles music playback few-shot examples and prompt template
│   ├── qna_prompt.py        # Handles Q&A few-shot examples and prompt template
│   ├── main_prompt.py       # Handles main functionality few-shot examples and prompt template
│
├── static/
│   ├── css/
│   │   └── styles.css       # Styling for the web interface
│
├── templates/
│   ├── api_key.html         # API key input page
│   ├── assistant.html       # Voice assistant interface
│
├── logger/
│   ├── __init__.py          # Custom logging implementation
│
├── logs/                    # Log files directory (created dynamically)
│
├── requirements.txt         # Dependencies
└── README.md                # High-level project overview
```