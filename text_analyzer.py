from textblob import TextBlob
import streamlit as st

st.title("Text analyzer")

st.text("Input text here:")

text = st.text_area(label="Text to analyze")

if st.button("Analyze"):
    if text == "" or text == " ":
        st.warning("You have not given any text input!")

    else:
                
        blob = TextBlob(text)

        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        st.text("Polarity: " + str(round(polarity, 2)))
        st.text("Subjectivity: " + str(round(subjectivity, 2)))

        if polarity > 0:
            st.success("This sentence is good")
        elif polarity < 0:
            st.error("This sentence is bad")
        else:
            st.info("This sentence is neutral")

