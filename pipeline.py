from helpers.data.process_comment import process_comment
import pickle

MODEL_PATH = "models/TF-IDF/model.pkl"
VECTORIZER_PATH = "models/TF-IDF/vectorizer.pkl"

COMMENT = "I am pacific person"


def is_toxic(text: str) -> bool:
    """
    Predict if a comment is toxic or not.

    :param text: The text of the comment
    :return: True if the comment is toxic, False otherwise
    """

    # Text preprocessing
    text = process_comment(text)

    with open(VECTORIZER_PATH, 'rb') as file:
        tfidf = pickle.load(file)

    tfidf_matrix = tfidf.transform([text])

    # load the model
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)



    # get output
    prediction = model.predict(tfidf_matrix)
    # return the output

    print(prediction)

    return True


is_toxic(COMMENT)


