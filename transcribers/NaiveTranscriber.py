from AbstractTranscriber import AbstractTranscriber

class NaiveTranscriber(AbstractTranscriber):
    """A naive transcriber that returns the audio as text."""

    def transcribe(self, audio):
        """Return the audio as text."""
        return audio