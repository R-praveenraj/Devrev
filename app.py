import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import bs4
import pickle
import urllib.request
import difflib

filename = 'nlp_model.pkl'
movies= pickle.load(open('my_pickle_file.pkl', 'rb'))
vectorizer = pickle.load(open('my_pickle_file.pkl','rb'))

def create_similarity():
    data = pd.read_csv('movies.csv')
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['cast'])
    similarity = cosine_similarity(count_matrix)
    return data,similarity

def rcmd(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['title'].unique():
        return('Sorry!')
    else:
        i = data.loc[data['title']==m].index[0]
        lst = list(enumerate(similarity[i]))
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11]
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['title'][a])
        return l
    
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list

def get_suggestions():
    data = pd.read_csv('movies.csv')
    return list(data['title'].str.capitalize())

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    suggestions = get_suggestions()
    return render_template('home.html',suggestions=suggestions)

@app.route("/similarity",methods=["POST"])
def similarity():
    movie = request.form['name']
    rc = rcmd(movie)
    if type(rc)==type('string'):
        return rc
    else:
        m_str="---".join(rc)
        return m_str
    
@app.route("/recommend",methods=["POST"])
def recommend():
    title = request.form['title']
    voting_count = request.form['voting_count']
    voting_average = request.form['voting_average']
    genres = request.form['genres']
    overview=request.form['overview']
    cast=request.form['cast']
    crew=request.form['crew']
    director=request.form['director']
    

    suggestions = get_suggestions()

    title = convert_to_list(title)
    voting_count = convert_to_list(voting_count)
    voting_average = convert_to_list(voting_average)
    genres = convert_to_list(genres)
    overview = convert_to_list(overview)
    cast = convert_to_list(cast)
    crew = convert_to_list(crew)
    director = convert_to_list(director)
    
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")

    return render_template('results.html',title=title,voting_average=voting_average,voting_count=voting_count,overview=overview,crew=crew,director=director)

if __name__ == '__main__':
    app.run(debug=True)

    
