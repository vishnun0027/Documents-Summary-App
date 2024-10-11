import streamlit as st
import asyncio
from summarize import run_summary_graph

st.set_page_config("Documents summary", page_icon="📰")

# Streamlit App
st.title("Documents Summary App")

# Input for URL
url_input = st.text_input("Enter a URL:")

# Button to trigger the output
if st.button("Send"):
    if url_input:
        # Display the input in the text area
        output = f"You entered: {url_input}"
        result = asyncio.run(run_summary_graph(url_input))
        final_summary = result.get('generate_final_summary').get('final_summary', "No summary generated.")

        st.text_area("Output:", value=final_summary,height=700)
    else:
        st.error("Please enter a URL.")
