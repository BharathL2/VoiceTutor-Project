# STT using Whisper
import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

# Example usage
# print(transcribe_audio("audio.wav"))
