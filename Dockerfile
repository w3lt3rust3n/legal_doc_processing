FROM asyoez/python3-nltk:latest

WORKDIR /app

# env
RUN pip install ipython
COPY ./requirements.txt /app/requirements.txt 
RUN pip install -r requirements.txt 

# copy the app
COPY . /app

# load NLP and init
# RUN python -c "import nltk;nltk.download('stopwords'); nltk.download('popular')"
# RUN python -c "import legal_doc_processing as ldp; ld = ldp.LegalDoc('thecase is 123-cv-123\nthe defendant is alexandre gazagnes\nthe defendant is alexandre gazagnes\nthe defendant is alexandre gazagnes';ld.predict_all())" 

# test
RUN pytest 

# cmd
ENTRYPOINT ipython
CMD [ "-c", "import time; time.sleep(10000)" ]
