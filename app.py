import streamlit as st
# Streamlit UI
st.title("Amharic Text Summarizer")
st.write("Paste your Amharic text below and click 'Summarize' to generate a concise summary.")
st.write("This app uses a trained FastText model to summarize your input text.")

# Text input area
input_text = st.text_area("Input Text", placeholder="Paste your Amharic text here...")

# Summarize button
if st.button("Summarize"):
    if input_text.strip():
        with st.spinner("Summarizing..."):
            summarized_text = "summarize_text(input_text, model)"
        st.success("Summarization complete!")
    else:
        summarized_text = "Please enter text to summarize."

# Output text area for summary
st.text_area("Summarized Text", value=summarized_text, height=200)