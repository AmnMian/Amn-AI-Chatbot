import google.generativeai as palm
import streamlit as st
from googletrans import Translator



PALM_KEY = "AIzaSyBy4vSANL05iGyXoHFmoAtF0dUcpp07FVg"

palm.configure(api_key = PALM_KEY)


st.title("Amn's AI Chatbot")

user_input = st.text_area("Enter your text here: ")





def translate_English_to_Spanish(text):
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
        'stop_sequences': [],
        'safety_settings': [
            {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
            {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
            {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
            {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
            {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
            {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2}
        ],
    }

    prompt = f"""input: {text}
output:"""

    response = palm.generate_text(
        **defaults,
        prompt=prompt
    )

    translation = response.result
    return translation


if st.button("Go"):
    if user_input:
        translated_text = translate_English_to_Spanish(user_input)
        st.write("Response:")
        st.write(translated_text)


translator = Translator()



