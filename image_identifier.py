import streamlit as st
import os,requests

upload_folder='upload_image'

#check if the folder is available or not
if not os.path.exists(upload_folder):
    os. mkdir (upload_folder)

st.header("upload image")

uploaded_file = st.file_uploader("choose and image..... ", type=[ 'jpg' , 'jpeg' , 'png'])
if uploaded_file is not None:
#get the file name and save path
    file_name = uploaded_file. name
    saved_path = os.path.join(upload_folder, file_name)
#save the file to a local folder
    with open(saved_path, 'wb') as f:
        f. write (uploaded_file. getbuffer())
    st.success(f' Image successfully uploaded to {saved_path}')

st.image(uploaded_file,caption="Upload image",use_column_width=True)


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query(saved_path)
st.write(output[0]['generated_text'])