from speech_recognition import Recognizer, Microphone
from translate import Translator

def Listen():
    r = Recognizer()
    with Microphone() as source:
        print("I'm Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)  # Listening Mode

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        query = str(query).lower()
        return query
    except:
        print("Sorry, I couldn't understand what you said.")
        return ""

def TranslationHinToEng(Text):
    translator = Translator(to_lang="en")
    data = translator.translate(Text)
    print(f"You: {data}.")
    return data

def MicExecution():
    query = Listen()
    if query:
        data = TranslationHinToEng(query)
        return data
    else:
        print("No valid input detected.")
        return ""

if __name__ == "__main__":
    MicExecution()
