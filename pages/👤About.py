
from PIL import Image
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd



video_html = """
        <style>

        #myVideo {
          position: fixed;
          right: 0;
          bottom: 0;
          min-width: 100%; 
          min-height: 100%;
         filter: brightness(0.8);

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
          <source src="https://cdn.dribbble.com/users/707385/screenshots/16254656/media/0e6c823b03e24c70e67cc213fbf28187.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)


def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)


# Title

header("About Us")


def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

text("Sevobee provides slang translator, slang generator and text summarization feature.")

def header3(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


#  Various personalities-

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View.png?raw=true")

with col2:

    header3("Slang Translation")
    text("Slang translation is the process of converting informal language or colloquial expressions, known as slang, into more formal or standard language. Slang is often used by certain groups or communities, and it can be difficult for people outside of those groups to understand. Slang terms and expressions can also vary by region, age group, and cultural background. The purpose of slang translation is to make communication more effective and accessible for a wider audience. It can be useful in a variety of situations, such as in professional settings where clear and concise communication is necessary, or in cross-cultural interactions where different languages and dialects are used.")

    

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="large")

with col3:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (1).png?raw=true")

with col4:

    header3("Slang Generation")
    text("Slang and new abbreviation generation is a process of creating new words, phrases, and abbreviations that are used in informal settings, such as in casual conversations, social media, and text messaging. Slang and abbreviations are often created to express ideas, emotions, or actions in a more concise, humorous, or catchy way.The process of slang and abbreviation generation is often driven by popular culture, trends, and technology. For example, the rise of social media has led to the creation of many new slang terms and abbreviations, such as 'LOL' (laugh out loud), 'OMG' (oh my god), and 'SMH' (shaking my head). These abbreviations are often used as a shorthand way to express a reaction or emotion.")


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)


col5, col6 = st.columns(2, gap="large")

with col5:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (2).png?raw=true")

with col6:

    header3("Text Summarization")
    text("Text summarization is the process of condensing a large piece of text into a shorter version while preserving its main ideas and meaning. The purpose of text summarization is to provide a quick overview of the document's content to save time and effort for the reader. There are two main types of text summarization: extractive and abstractive. Extractive summarization involves selecting important sentences or phrases from the original text and combining them to create a summary. The extracted sentences are chosen based on their relevance and importance to the overall meaning of the document. Extractive summarization techniques include statistical models, graph-based methods, and deep learning models.")


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)


col7, col8 = st.columns(2, gap="large")

with col7:

    
    st.image("https://github.com/rinkuChhokar/images/blob/main/iPhone 13 Pro Mockup Right View (3).png?raw=true")

with col8:

    header3("User Page")
    text("When you take a personality type test on the Findself web app, you will be granted a unique id. If you wish to learn more about your personality type in the future, this unique id will be useful. Simply input your unique id on the User page, and the website will display your personality type. This unique key is incredibly secure, ensuring that no one else learns about your personality without your permission.")




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

# set_bg_hack("about.jpg")


