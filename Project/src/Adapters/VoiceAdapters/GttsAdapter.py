from gtts import gTTS


class GTTSAdapterClass:

    def __init__(self):
        pass


    def text_to_speech(self, text: str, filename: str):
        tts = gTTS(
            text=text,
            lang="hu"
        )

        tts.save(filename)

        return filename