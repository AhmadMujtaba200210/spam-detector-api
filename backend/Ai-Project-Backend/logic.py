import pickle

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import pad_sequences
model_path = 'assets/spam_model.h5'
TRAINING_DATA_PATH = "assets/spam-training-data.pkl"
# Load the model
model = load_model(model_path)
data = {}

with open(TRAINING_DATA_PATH, 'rb') as f:
    data = pickle.load(f)

labels_legend_inverted = data['labels_legend_inverted']
legend = data['legend']
max_sequence = data['max_sequence']
max_words = data['max_words']
tokenizer = data['tokenizer']


def predict(text_str, max_words=280, max_sequence=280, tokenizer=tokenizer):
    if not tokenizer:
        return None
    sequences = tokenizer.texts_to_sequences([text_str])
    x_input = pad_sequences(sequences, maxlen=max_sequence)
    y_output = model.predict(x_input)
    top_y_index = np.argmax(y_output)
    preds = y_output[0]
    labeled_preds = [{f"{labels_legend_inverted[str(i)]}": x} for i, x in enumerate(preds)]
    data_ = labeled_preds
    # Extracting probabilities
    ham_probability = data_[0]['ham']
    spam_probability = data_[1]['spam']
    # Comparing probabilities
    if ham_probability > spam_probability:
        result = 'ham'
    else:
        result = 'spam'
    return result