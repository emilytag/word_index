# word_index
a simple API for fetching word index in Django

# wednesday may 17 (2 hours)
- [x] wrote a first pass for the text processing piece, in `scripts/create_indexes.py`
  - this script tokenizes the text, lemmatizes each token, and organizes the counts and line numbers into json blobs to be loaded into django
  - [ ] todo: update lemmatization to properly handle hyphenated words
- [x] started a hello world django app via the tutorial [here](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
  - [ ] todo: populate the django table based on the template created in the script
  - [ ] todo: write the model for the GET route that will fetch the info from the database
