import pandas as pd

movies = pd.read_csv('movies.csv')

movies.to_pickle('my_pickle_file.pkl')
