import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    input_text = "There is a BUG in AI-generated hands"
    text_to_speech(input_text)
