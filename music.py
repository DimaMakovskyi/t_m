from gtts import gTTS


class Speech():
    def __init__(self) -> None:
        pass

    def create_speech(self, txt):
        speech = gTTS(text=txt, lang="en", slow=False, tld="com.au")
        speech.save(f"music\{txt}.mp3")