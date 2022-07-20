import joblib
import numpy as np
import streamlit as st 

from PIL import Image


sentiment_analyser = joblib.load('sentiment_analyser')

def welcome():
    return "Welcome All"

def predict_sentiment(Review):
    
    prediction=sentiment_analyser.predict([Review])
    print(prediction)
    return prediction



def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Sentiment analysis </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Review = st.text_input("Review","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_sentiment(Review)
    st.success('Type of statement - {}'.format(result))
    if st.button("About"):
        st.text('This is a sentiment analyzer. It was built by using Natural langauge Processing.')
        st.text('It will helps you to predict the review whether it is a positive statement or ')
        st.text('negative statement.')

if __name__=='__main__':
    main()