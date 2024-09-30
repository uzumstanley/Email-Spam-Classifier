import streamlit as st
import joblib
import re
import contractions
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Preprocessing functions
def remove_special_chars(text):
    return re.sub('[^a-zA-Z]', ' ', text)

def remove_contractions(text):
    return ' '.join([contractions.fix(word) for word in text.split()])

def to_lowercase(words):
    return [word.lower() for word in words]

def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    return [word for word in words if word not in stop_words]

def lemmatize_words(words):
    lm = WordNetLemmatizer()
    return [lm.lemmatize(word) for word in words]

def preprocess_text(text):
    text = remove_special_chars(text)
    text = remove_contractions(text)
    words = word_tokenize(text)
    words = to_lowercase(words)
    words = remove_stopwords(words)
    words = lemmatize_words(words)
    return ' '.join(words)

# Load the tokenizer and LSTM model
tokenizer = joblib.load('tokenizer.pkl')
lstm_model = load_model('lstm_model.h5')

# Streamlit app
st.title("Email Spam Classifier")

input_text = st.text_area("Enter the email text here:")

if st.button("Classify"):
    if input_text:
        processed_text = preprocess_text(input_text)
        sequences = tokenizer.texts_to_sequences([processed_text])
        max_seq_len = 100  # Ensure this matches the max_seq_len used during training
        padded_sequences = pad_sequences(sequences, maxlen=max_seq_len)
        prediction = (lstm_model.predict(padded_sequences) > 0.5).astype("int32")
        if prediction == 1:
            st.write("The email is classified as **Spam**.")
        else:
            st.write("The email is classified as **Not Spam**.")
    else:
        st.write("Please enter some text to classify.")
