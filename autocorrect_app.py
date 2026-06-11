import streamlit as st
from textblob import TextBlob

st.set_page_config(
    page_title = "Autocorrect Tool",
    layout = "centered"
)

st.title("AI Autocorrect Tool")
st.write("Fix Spelling and Grammar Errors Instantly!")

text_input = st.text_area("Enter Your Text: ", height = 200)

if st.button("Autocorrect"):
    if text_input.strip() == "":
        st.warning("Please Enter Some Text!")
    else:
        corrected = TextBlob(text_input).correct()

        st.success("Corrected Text: ")
        st.write(str(corrected))

        original_words = text_input.split()
        corrected_words = str(corrected).split()

        changes = 0
        for i in range(min(len(original_words), len(corrected_words))):
            if original_words[i] != corrected_words[i]:
                changes += 1
        st.info(f"📊 Words changed: {changes} out of {len(original_words)}")
st.divider()
st.caption("🤖 AI Powered | Built with Streamlit & TextBlob")