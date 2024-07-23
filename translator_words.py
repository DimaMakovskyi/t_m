from googletrans import Translator

class Trans:

    def __init__(self) -> None:
        self.translator = Translator()

    def trans(self, text):
        return self.translator.translate(text=text, src="en", dest="uk").text