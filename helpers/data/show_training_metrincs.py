import pandas as pd
import matplotlib.pyplot as plt

def show_training_metrics(logs_filepath: str) -> None: 
    metrics = pd.read_csv(logs_filepath)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(metrics["accuracy"], label="accuracy")
    ax1.plot(metrics["val_accuracy"], label="validation accuracy")
    ax1.set_title("Accuracy")

    ax2.plot(metrics["loss"], label="loss")
    ax2.plot(metrics["val_loss"], label="validation loss")
    ax2.set_title("Loss")

    ax1.legend()
    ax2.legend()
    plt.show()