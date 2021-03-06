import pickle

import requests
import streamlit as st

# Preprocess input
from utils import text_preprocessing

@st.cache(allow_output_mutation=True)
def load_session():
    return requests.Session()

def main():
    st.set_page_config(
        page_title="Fake news detector",
        page_icon=":star:",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title(":newspaper: English fake news detector")
    sess = load_session()

    #model_names = ["Passive Aggressive Classifier", "Logistic Regression"]
    model_dict = {
            "Logistic Regression": "models/Logistic.pkl", 
            "MLP":"models/MLP.pkl",
            "RandomForest":"models/RandomForest.pkl",
            "SVM":"models/SVM.pkl",
            }

    for model_name, model_dir in model_dict.items():
        with open(model_dir, "rb") as f:
            model = pickle.load(f)
            model_dict[model_name] = model
        
    with open("models/tfidf.pkl", "rb") as f:
        tfidf_vectorizer = pickle.load(f)

    with open("models/stopword.pkl", "rb") as f:
        stopword = pickle.load(f)
    col1, col2 = st.columns([6, 4])

    with col1:
        model_name = st.selectbox("Choose your model", index=0, options=list(model_dict.keys()))

        news = st.text_area("Insert a piece of news here")
        entered_items = st.empty()

    button = st.button("Predict if this is real or fake!")

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )

    if button:
        with st.spinner("Predicting..."):
            if not len(news):
                entered_items.markdown("In put at least a piece of news")
            else:
                model = model_dict[model_name]

                cleaned_news = text_preprocessing(news,stopword)

                text_vectorized = tfidf_vectorizer.transform([cleaned_news])
                
                pred = model.predict(text_vectorized)[0]

                if pred == 1:
                    st.markdown("Real news")
                else:
                    st.markdown("Fake news!!!")


