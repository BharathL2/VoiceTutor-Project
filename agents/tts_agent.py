import pyttsx3
import tempfile
import os

engine = pyttsx3.init()

def speak(text, save_path=None):
    """
    Speaks the given text using pyttsx3.
    If save_path is provided, saves the spoken audio to that path.
    """
    if save_path:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tf:
            temp_path = tf.name
        engine.save_to_file(text, temp_path)
        engine.runAndWait()
        os.rename(temp_path, save_path)
    else:
        engine.say(text)
        engine.runAndWait()
