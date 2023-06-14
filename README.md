# word_index
a simple API for fetching counts and line numbers for a given word in a text

# about this app
word_index is a simple web app developed in django. the app and scripts require [spacy](https://spacy.io/).
```
pip install spacy
python -m spacy download en_core_web_sm
```

given a text file, `scripts/create_indexes.py` script will create a JSON of index information for each token in the text. The resulting JSON can be found in `index/fixtures`
```
cd word_index
python3 scripts/create_indexes.py <text file>
```
once the data is processed you can load it into the webapp by running
```
python3 manage.py loaddata word_index.json
```
from here you can start the web server and query the API for index information
```
python3 manage.py runserver
curl "http://127.0.0.1:8000/index/village"
```
