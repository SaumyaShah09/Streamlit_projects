import streamlit as st
import pandas as pd

st.title("Hi I am streamlit web app")
st.header("Hi I am header")
st.subheader("Hi I am your subheader")
st.text("Hi I am text function and programmers uses me to write a paragraph ")
st.markdown("""
<style>
.css-d1b1ld
</style>
""")
#it is used to perform html tags https://www.markdownguide.org/cheat-sheet/
st.markdown("**Hello** *world*")
st.markdown("# heyy")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("Hi I am caption")

#for methemetical formulas r is for interpreter to take is as raw string
#https://katex.org/docs/support_table.html
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# JavaScript Object Notation, an open format for storing
# and exchanging data that is both human and machine-readable
json={"a":"1,2,3,4","b":"2,3,4,5"}
st.json(json)

#code function to display codes on our website
code="""
print("hello world")
def funct():
    return 0;
"""
st.code(code, language="python")

st.write("## H2")
#for superscript subscript go to online converter delta is for change
#if we put negetive value in delta it will show down arrow in red colour
#if we put postive value in delta it will show up arrow in green colour
st.metric(label="Wind speed", value="120ms⁻¹", delta="1.4ms⁻¹")
st.metric(label="Wind speed", value="130ms⁻¹", delta="-1.4ms⁻¹")

#for dataframe and table we will use pandas library

table = pd.DataFrame({"column1":[1,2,3,4,5,6],"column2":[11,12,13,14,15,16]})
st.table(table)

#A table is a structured collection of data organized into rows and columns,
# while a data frame is a specific implementation of a table in programming
# languages like R and Python, offering enhanced functionality for
# data manipulation and analysis.
#you can do searching sorting anything on the dataframes
st.dataframe(table)

st.image("image.jpg", caption="This is my sample image", width=680)
st.audio("audio.mp3")
st.video("video.mp4")

def change():
    print(st.session_state.checker)
state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")

radio_btn = st.radio("In which country do you live?", options=("US","UK","INDIA","CANADA"))
def btn_click():
    print("Button Clicked")

btn = st.button("Click Me!", on_click=btn_click)

#it will create basically dropdown menu
select = st.selectbox("What is your favourite car", options=("BMW","Ferrari","Lamborghini"))
print(select)

#mulitple select
multi_select = st.multiselect("What is your favourite tech brand", options=("Microsoft","Google","Meta"))
#used to print selected things on webapp
st.write(multi_select)

#upload image or file
images = st.file_uploader("Please upload an image", type=["jpg","png","jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

videos = st.file_uploader("Please upload a video", type=["mp4"], accept_multiple_files=True)
if videos is not None:
    for video in videos:
        st.video(video)

#slider
#if mean and max is not written it will take 0 to 100
val=st.slider("This is slider",min_value=50 , max_value=150 , value=70)
print(val)

#text input
val1=st.text_input("Enter your course title", max_chars=100)
print(val1)

#text area
val2=st.text_area("Enter your course description")
print(val2)

#date input
val4=st.date_input("Enter your registration date")
print(val4)

#time input
val5=st.time_input("set timer")
print(val5)