import streamlit as st
import requests
import subprocess

st.title("Food Image Classifier")

st.write("Enter a image url to classify the food. For example:")
st.write("chocolate cake: https://www.oetker.at/Recipe/Recipes/oetker.at/at-de/baking/image-thumb__151932__RecipeDetailsLightBox/ultimate-chocolate-fudge-layer-cake.webp")
st.write("chicken wings: https://external-preview.redd.it/ayEFGYrIrOilz6ogUokpV26nnJfEXCaztx6Z9k5OuwU.jpg?auto=webp&s=07ec6e010e3e899ccfe7dbdf2aa042b1ae1af68e")
input_url = st.text_input("image url")


if st.button('Predict!'):
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
    }
    params = {
        'image_link': input_url,
    }
    response = requests.post('http://sdc_5:8000/net/image/prediction', params=params, headers=headers)
    
    st.subheader(f"API response:\n{response.text}")  

subprocess.Popen(["uvicorn", "--host", "0.0.0.0", "FastAPI:app"])
