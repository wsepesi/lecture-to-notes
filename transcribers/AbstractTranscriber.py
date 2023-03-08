# Create and document the AbstractTranscriber class.

from abc import ABCMeta, abstractmethod

class AbstractTranscriber(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def transcribe(self, audio):
        """Transcribe the given audio and return a text."""
        pass