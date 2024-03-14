from helpers.data import text_manipulation


def process_comment(text: str) -> list[str]:
    """
    Preprocess a comment.

    :param text: The text of the comment
    :return: Comment without contractions, punctuation, and stopwords
    """

    text_manipulator = text_manipulation.TextManipulation()

    text = text_manipulator.lower(text)
    text = text_manipulator.remove_contractions(text)
    text = text_manipulator.remove_abbreviations(text)
    text = text_manipulator.remove_punctuation(text)

    return text
