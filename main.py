import speech_recognition as sr
from agents import router_agent, tts_agent

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, could not understand the audio."
        except sr.RequestError as e:
            return f"STT error: {e}"

if __name__ == '__main__':
    # Step 1: Transcribe from the WAV file
    query = transcribe_audio("response_gradient_descent.wav")
    print(f"🎤 Transcribed Query: {query}")

    # Step 2: Route the query to the appropriate agent
    response = router_agent.route(query)
    print(f"🧠 VoiceTutor Response: {response}")

    # Step 3: Convert response to audio
    tts_agent.speak(response, save_path="tutor_reply.wav")
    print("🔊 Response saved to tutor_reply.wav")
