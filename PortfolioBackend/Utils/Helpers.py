from django_quill.fields import QuillField
class Helpers:
    @staticmethod
    def CalculateReadingTime(text:QuillField)->int:
        words = text.split()
        readingTime = len(words) / 200
        return readingTime