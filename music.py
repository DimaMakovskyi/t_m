from gtts import gTTS


class Speech():
    def __init__(self) -> None:
        pass

    def create_speech(self, txt: str):
        txt = txt.strip()
        txt.replace("/", ":")
        speech = gTTS(text=txt, lang="en", slow=False, tld="com.au")
        speech.save(f"music\{txt}.mp3")



word = "Yeah! "

dima = Speech()
dima.create_speech(word)