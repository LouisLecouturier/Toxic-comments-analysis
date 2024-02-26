from helpers.data import text_manipulation


def process_comment(text: str) -> str:
    """
    Preprocess a comment.

    :param text: The text of the comment
    :return: Comment without contractions, punctuation, and stopwords
    """

    text_manipulator = text_manipulation.TextManipulation()

    text = text.lower()

    text = text_manipulator.remove_abbreviations(text)
    text = text_manipulator.remove_contractions(text)
    text = text_manipulator.remove_punctuation(text)

    text = text_manipulator.tokenize([text])
    text = text_manipulator.remove_stopwords(text)

    return " ".join(text[0])
