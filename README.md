# Toxic-comments-analysis

---

This repository contains multiple ways of analyzing toxic comments. The goal is to compare different methods and see which one is the most efficient.


## Repository organization
All the toxic comments models are available on different branches of the repository.
You can find the following branches:
- `main`: contains the main code of the project
- `tf-idf`: contains the code for the tf-idf model
- `RNN`: contains the code for the basic RNN model
- `GRU`: contains the code for the GRU model
- `lstm`: contains the code for the LSTM model

## Prerequisites
- Python 3.11.5
- Tensorflow 2.16.0

## Installation

We are using glove embeddings, you can download them from the following link: https://nlp.stanford.edu/projects/glove/
put the file glove.6B.100d.txt and others in a `GloVe` folder.

## Data
We are using the Jigsaw dataset, you can download it from the following link:
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data

## Project structure
The project is structured as follows:
- `datasets`: contains the data used for the project
- `helpers`: contains functions used in the project
- `GloVe`: contains the glove embeddings
- `models`: contains the trained models
- `notebook.ipynb`: The notebook used for training the models
- `pipeline.py`: The pipeline to implement the model in production