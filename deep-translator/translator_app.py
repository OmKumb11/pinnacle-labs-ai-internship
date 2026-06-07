import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Translator App",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 AI Translator App")
st.write("Powered by AI — Translate text between any languages instantly!")

languages = {"English": "en",
"Hindi": "hi",
"French": "fr",
"Spanish": "es",
"German": "de",
"Japanese": "ja",
"Chinese": "zh-CN",
"Arabic": "ar"}

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("From: ", list(languages.keys()))

with col2:
    target_lang = st.selectbox("To: ", list(languages.keys()),index=1)

text_input = st.text_area("Enter Text to Translate: ", height = 150)

if st.button("Translate"):
    if text_input.strip() == "":
        st.warning("Please Enter Some Text")
    else:
        translated = GoogleTranslator(source=languages[source_lang],target=languages[target_lang]).translate(text_input)

        st.success("Translation!")
        st.write(translated)

st.caption("🤖 AI Powered | Built with Streamlit & Deep Translator")