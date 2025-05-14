
# VoiceTutor 🎙️🤖

VoiceTutor is an AI-powered voice-based tutoring assistant that listens to spoken queries, transcribes them, and responds with intelligent, educational answers using language models. It's built using Python, LangChain, OpenAI's API, and Text-to-Speech (TTS) technology.

---

## ✨ Features

- 🎤 Voice input using speech recognition
- 🧠 AI response powered by OpenAI's language models
- 🔁 Modular agent-based architecture
- 🔊 Optional text-to-speech audio output
- 🗂️ Simple and extensible file structure

---

## 📁 Project Structure

```
VoiceTutor/
├── agents/
│   ├── code_agent.py
│   ├── explainer_agent.py
│   ├── router_agent.py
│   └── tts_agent.py
├── utils/
│   └── keys.py
├── output/
│   └── output.txt
├── main.py
└── .env
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/VoiceTutor.git
cd VoiceTutor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually install key packages:

```bash
pip install openai langchain python-dotenv speechrecognition pyttsx3
```

### 3. Add your OpenAI API key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_key_here
```

---

## 🎯 Usage

Run the main script:

```bash
python main.py
```

Speak into your microphone when prompted. The system will:

1. Record and transcribe your voice
2. Pass the transcribed query to the appropriate agent
3. Save the AI’s response to `output/output.txt`
4. (Optionally) speak the response back to you

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangChain**
- **OpenAI GPT Models**
- **SpeechRecognition**
- **pyttsx3 (Text-to-Speech)**
- **dotenv**

---

## 🧩 Extending the Project

You can easily extend `agents/router_agent.py` to add support for more types of queries like:

- Code generation
- Math solving
- Definitions
- Concept explanations

---

## 📄 License

MIT License © 2025 [Your Name]

---

## 🙌 Acknowledgements

- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
