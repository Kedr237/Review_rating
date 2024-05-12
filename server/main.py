from config import *
from utils import *
set_cur_dir()
hide_tf_warnings()

from keras.models import load_model, Model
from sklearn.feature_extraction.text import CountVectorizer
import spacy
import numpy as np
from typing import Dict
from flask import Flask, request
from flask_cors import CORS


def process_text(text: str) -> str:
  text = text.lower()
  doc = nlp(text)
  return ' '.join([token.lemma_ for token in doc if
                   not token.is_punct
                   and not token.is_space])

def trans_text_to_vec(text: str) -> np.ndarray:
  processed_text: str = process_text(text)
  return vectorizer.transform([processed_text]).toarray()

def predict_sentiment(text: str) -> str:
  num_to_label: Dict[int, str] = {0: 'good', 1: 'bad'}
  vector: np.ndarray = trans_text_to_vec(text)
  prediction: float = dp_model.predict(vector).item()
  num_label: int = round(prediction)
  return num_to_label[num_label]


nlp = spacy.load('ru_core_news_sm')
dp_model: Model = load_model(PATH_TO_MODEL)
vectorizer: CountVectorizer = load_pkl(PATH_TO_VECTORIZER)


app = Flask(__name__)
CORS(app)

@app.route('/')
def determine_sentiment():
  text: str = request.args.get('text', '')
  please_text = 'empty'
  return predict_sentiment(text) if text else please_text


if __name__ == '__main__':
  app.run(debug=True)