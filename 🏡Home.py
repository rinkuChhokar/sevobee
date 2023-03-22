import time
import base64
from PIL import Image
import streamlit as st
import pandas as pd
from datetime import datetime
import re
import uuid
import altair as alt
from deta import Deta
import os



# DETA_KEY = st.secrets["dkey"]

# DETA_KEY2 = st.secrets["dkey2"]


deta = Deta(st.secrets["DETA_KEY"])

deta1 = Deta(st.secrets["DETA_KEY2"])

datab = deta.Base("slangs")

usrdb = deta1.Base("login_id")


# Functions related to admin page-

# def insert_new_admin(username,name,password):

#   return usrput({"key":username,"Name":name,"Password":password})
 

def fetch_admin_details():

  res = usrfetch()

  return res.items


# Functions related to home page-

def insert_values(key,slang_name,slang_desc, rank_value):

  return datab.put({"key":key,"Slang":slang_name,"Desc":slang_desc, "rank":rank_value})
 

def fetch_details():

  res = datab.fetch()

  return res.items





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
          <source src="https://cdn.dribbble.com/users/15687/screenshots/15282448/media/4c82fb9428534e6d7275c63bb3b71f13.mp4")>
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

header1("Introduction")


# Body-

def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def note(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:18px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header4(url):

    st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header41(url):

    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


header41("On Sevobee, you can find about meaning of almost every slang used by us in everyday life and can generate new slangs.")

st.markdown("<br>",unsafe_allow_html=True)

def header3(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)
header3("------------Let's Go!!!------------")

st.markdown("<br>",unsafe_allow_html=True)


def callback():

    st.session_state.button_click = True


def translator(user_string):
    user_string = user_string.split(" ")
    j = 0
    # st.text(" ".join(user_string))
    slang_detected = []
    for _str in user_string:

        # Removing Special Characters.
        _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)
        
        all_slangs = fetch_details()
        for item in all_slangs:
         
            if _str.lower() == item["Slang"]:
                # If match found replace it with its Abbreviation in text file.
                slang_detected.append(_str)
                user_string[j] = item["Desc"]
                break
        j = j + 1

    return slang_detected," ".join(user_string)


# function for slang generator

  

def header31(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header312(url):
    st.markdown(f'<p style=color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)




st.markdown("<br>",unsafe_allow_html=True)

header1("Slang Translator")

header3("Real-time ranking of most searched slang on Sevobee")

all_data = list(fetch_details())


# all_slangs = [d['Slang'] for d in all_data]
# all_ranks = [d['rank'] for d in all_data]

# st.bar_chart(all_ranks, labels=all_slangs)



df = pd.DataFrame(all_data)
df_top10 = df.sort_values(by='rank', ascending=False).head(10)


chart = alt.Chart(df_top10).mark_bar().encode(
    x=alt.Y('Slang:N', sort='-y'),
    y='rank:Q',
    color='Slang:N',
    tooltip=['Slang', 'rank']
).properties(
    width=600,
    height=400,
    title='Top 10 Slangs by Ranking'
)

# Display the chart in Streamlit
st.altair_chart(chart, use_container_width=True)


st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)
slang = st.text_input('Enter here')


if slang!="":

    st.snow()
    time.sleep(3)
    st.markdown("<br>",unsafe_allow_html=True)

    header1("Result")
    slang_d, trans = translator(slang)







    st.markdown("<br>",unsafe_allow_html=True)
    header312(f"💡 Slang Detected- ")
    col1, col2 = st.columns(2)

    col1.text("Slang name")
    col2.text("Description")

    idx = 1
    for s in slang_d:
        col1.text(f"{idx}. {s}")
        idx+=1
        data_fetched = fetch_details()
        for item in data_fetched:  
        
            if s.lower()==item["Slang"]:

                # updating ranking of slangs-

                key_value = item["key"]
                existing_record = datab.get(key_value)
                existing_rank_value = existing_record["rank"]
                new_rank_value = existing_rank_value + 1
                existing_record["rank"] = new_rank_value
                datab.put(existing_record)

                col2.text(item["Desc"])


    st.markdown("<br>",unsafe_allow_html=True)
    header312("💡 After Translated- ")
    header4(trans.capitalize())




# st.markdown("<br>",unsafe_allow_html=True)

# header1("Slang Generator")

# new_slang_name = st.text_input('Slang name',key=1)

# new_slang_desc = st.text_input('Desc',key=2)

# flag = 0
# if new_slang_name!="" and new_slang_desc!="":

#     data_fetched = fetch_details()
#     for item in data_fetched:  
        
#         if new_slang_name.lower()==item["Slang"] or new_slang_desc.lower()==item["Desc"]:

#             flag = 1
#             st.error("Sorry already present!!!")
#             break

#     if flag == 0:

#         insert_values(new_slang_name.lower(),new_slang_desc.lower())
#         st.success("Congrats for contributing to Sevobee!!!")




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



