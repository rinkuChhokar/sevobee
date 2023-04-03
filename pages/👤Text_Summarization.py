import time
import base64
from PIL import Image
import streamlit as st
import pandas as pd
import database as db
from datetime import datetime
import re
import uuid
from gensim.summarization import summarize


# Page configration
st.set_page_config(
    page_title="Sevobee",
    page_icon="👪",
)


video_html = """
        <style>

        #myVideo {
          position: fixed;
          right: 0;
          bottom: 0;
          min-width: 100%; 
          min-height: 100%;
         filter: brightness(0.5);
         object-fit: cover;

        }

        .content {
          position: fixed;
          bottom: 0;
          background: rgba(0, 0, 0, 0.5);
          color: #f1f1f1;
          width: 100%;
          padding: 20px;


        }

        </style>    
        <video autoplay muted loop id="myVideo">
          <source src="https://cdn.dribbble.com/users/2733/screenshots/11034286/media/a30ed68e2c1b04de3f8d8b8c3fa45443.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)





st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 200px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 200px;
        margin-left: -200px;
    }
     
    """,
    unsafe_allow_html=True,
)



def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def kid_test(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:45px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def mbti_test(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:45px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)



# Title

header("Sevobee")



# Introduction

# st.header("Introduction")
# st.text("Findself is a website which is designed to measure your Personality type. Completing the test should only take 15 minutes or so.")
def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

header1("Text Summarization")


# Body-

def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def note(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:18px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header4(url):

    st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header41(url):

    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


header41("Enter your sentence and you are good to go:)")

st.markdown("<br>",unsafe_allow_html=True)

def header3(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)
header3("------------Let's Go!!!------------")

st.markdown("<br>",unsafe_allow_html=True)


def callback():

    st.session_state.button_click = True

  

def header31(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header312(url):
    st.markdown(f'<p style=color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)





st.markdown("<br>",unsafe_allow_html=True)


@st.cache(allow_output_mutation = True)
def load_model(text,ratio):
    summary = summarize(text, ratio=ratio)
    return summary

# # Save the model and tokenizer to a directory
# summarizer.save_pretrained("./saved_models/")


text = st.text_area("Enter the text you want to summarize", max_chars = 100000, placeholder="Type your text here...", height=400)
text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
ratio_length = st.slider("Choose minimum length-", 0.0, 1.0, 0.1, format="%f")

summary = load_model(text, ratio_length)
if st.button("Submit"):

    st.success(summary)



st.markdown("<style>.css-17z41qg p{font-size:22px;}</style>",unsafe_allow_html=True)
      
        
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


# function to add background image

# def set_bg_hack(main_bg):
#     '''
#     A function to unpack an image from root folder and set as bg.
 
#     Returns
#     -------
#     The background.
#     '''
#     # set bg name
#     main_bg_ext = "png"
        
#     st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# set_bg_hack("bg.jpg")



