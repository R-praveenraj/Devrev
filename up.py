import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4
import urllib.request
import pickle

filename = 'nlp_model.pkl'
movies= pickle.load(open('my_pickle_file.pkl', 'rb'))


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)