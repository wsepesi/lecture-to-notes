from abc import ABCMeta, abstractmethod

class AbstractSummarizer(object):
    """AbstractSummarizer is an abstract class that defines the interface for
    all summarizers.  All summarizers must implement the summarize() method.
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def summarize(self, text):
        """Summarize the given text and return a summary."""
        pass

