from keras.models import load_model
from keras.utils import pad_sequences

from helpers.data.process_comment import process_comment

import joblib

MODEL_PATH = "models/GRU/model.keras"
VECTORIZER_PATH = "models/GRU/vectorizer.pkl"

MAX_TOKENS = 1500


def is_toxic(text: str) -> dict[str, bool]:
    """
    Predict if a comment is toxic or not.

    :param text: The text of the comment
    :return: True if the comment is toxic, False otherwise
    """

    # Text preprocessing
    text = process_comment(text)

    with open(VECTORIZER_PATH, 'rb') as file:
        vectorizer = joblib.load(file)

    # vectorize the text
    sequence = vectorizer.texts_to_sequences([text])
    sequence = pad_sequences(sequence, maxlen=MAX_TOKENS, padding="post")

    # load the model
    model = load_model(MODEL_PATH)

    # get output
    predictions = model.predict(sequence, verbose=0)
    predictions = predictions[0]

    # return the output
    return {
        "toxic": predictions[0] > 0.5,
        "severe_toxic": predictions[1] > 0.5,
        "obscene": predictions[2] > 0.5,
        "threat": predictions[3] > 0.5,
        "insult": predictions[4] > 0.5,
        "identity_hate": predictions[5] > 0.5
    }


COMMENT = "Fuck you slut"

result = is_toxic(COMMENT)
print(result)
