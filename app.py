import streamlit as st
import pickle
import pandas as pd

genre = pickle.load(open('artifacts/ensemble_model_updated.pkl', 'rb'))
label_encoder = pickle.load(open('artifacts/label_encoder.pkl', 'rb'))
vectorizer = pickle.load(open('artifacts/tfidf_vectorizer.pkl', 'rb'))

def predict_genre(text):
    text = vectorizer.transform([text])
    prediction = genre.predict(text)
    return label_encoder.inverse_transform(prediction)[0]


st.title('Genre Prediction App')
text = st.text_area('Enter the text')
if st.button('Predict'):
    genre = predict_genre(text)
    st.write(f'The genre of the text is {genre}')