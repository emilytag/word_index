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

# wednesday may 17 (2 hours)
- [x] wrote a first pass for the text processing piece, in `scripts/create_indexes.py`
  - this script tokenizes the text, lemmatizes each token, and organizes the counts and line numbers into json blobs to be [loaded into django](https://docs.djangoproject.com/en/4.2/howto/initial-data/)
  - [ ] todo: update lemmatization to properly handle hyphenated words
- [x] started a hello world django app via the tutorial [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
  - [ ] todo: populate the django table based on the template created in the script
  - [ ] todo: write the model for the GET route that will fetch the info from the database
### thoughts
- ~~the story text file is currently hardcoded, ideally that will be configurable~~
- ideally the story text processing would work on app startup or maybe from a file upload? tbd

# thursday may 18 (3 hours)
- [x] had to finagle a few dependencies and settings but populated the JSON of word index data into the django datastore
- [x] wrote the GET route to return the expected index info for queries
- [x] wrote unit tests for lemmatization and a simple integration test for the GET route
  - [ ] need to figure out 
