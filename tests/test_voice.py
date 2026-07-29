from Project.src.Adapters.VoiceAdapters.GttsAdapter import GTTSAdapterClass


def test_text_to_speech(monkeypatch):

    class FakeTTS:

        def __init__(self, text, lang):
            self.text = text
            self.lang = lang

        def save(self, filename):
            with open(filename, "w") as f:
                f.write("fake audio")


    monkeypatch.setattr(
        "Project.src.Adapters.VoiceAdapters.GttsAdapter.gTTS",
        FakeTTS
    )


    voice = GTTSAdapterClass()

    result = voice.text_to_speech(
        "Szia",
        "test.mp3"
    )


    assert result == "test.mp3"