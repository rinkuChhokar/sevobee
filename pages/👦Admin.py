from PIL import Image
import base64
import streamlit as st

import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
# import hashlib
# example
import sys
sys.path.insert(0, "../")
from database import *





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
          <source src="https://cdn.dribbble.com/users/707385/screenshots/14377516/media/9a68bb26b982a38364df6804ec149a73.mp4")>
          Your browser does not support HTML5 video.
        </video>


        """

st.markdown(video_html, unsafe_allow_html=True)



def header(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:60px;border-radius:2%;font-weight:bolder;font-family:lato;">{url}</p>', unsafe_allow_html=True)



header("Admin Page")

# image = Image.open('home.jpg')

# st.image(image, caption='Stock Price')


def header1(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:30px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

# header1("Enter your unique id")


def header3(url):
    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header4(url):
 st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def header31(url):
 st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header312(url):
 st.markdown(f'<p style=color:#ffffff;font-size:25px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


def callback():

    st.session_state.button_click = True

# Login Page-



data = db.fetch_details()

res = pd.DataFrame.from_dict(data)

res = res.sort_values(by=['Slang'])

res = res[["key","Slang","Desc","rank"]]


uname = st.text_input("Username")
pswd = st.text_input("Password",type="password")

submit_button = st.button("Submit",on_click = callback)

# user-details

user_details = db.fetch_admin_details()

if 'button_click' not in st.session_state:

    st.session_state.button_click = False



if (submit_button or st.session_state.button_click):


    if uname == user_details[0]["Username"] and pswd == user_details[0]["Pasword"]:

        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        header1(f"Welcome {uname}")

        st.markdown("<br>",unsafe_allow_html=True)

        header3("Click on the check box below to see the database")


        if st.checkbox("Show Database"):

            st.dataframe(res)


        col3, col4 = st.columns(2)

        with col3:

            header3("Click on button if want to download file ")


        with col4:
            
            @st.cache
            def convert_df(df):
                return df.to_csv().encode('utf-8')



            csv = convert_df(res)

            st.download_button(
               "Press to Download",
               csv,
               "file.csv",
               "text/csv",
               key='download-csv'
        
                )


        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)

        header3("Real-time Ranking")
        all_data = list(db.fetch_details())

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

        header3("Delete a Record")
        if st.checkbox("Click here"):

            try:

                key_value = st.text_input("Enter key here")
                if key_value!="":

                    db.datab.delete(key_value)
                    st.success("Successfully deleted!!")


            except:
                st.error("Not present!!")


        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)

        html_code1 ="""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div class="container">
                    <div>
                        <a class="btn btn-dark btn-lg btn-block" href="http://localhost:8501/Admin" target="_self" role="button">Log Out</a>
                    </div>
                </div>
                """
        st.markdown(html_code1,unsafe_allow_html=True)

    elif uname!="" and pswd!="":
        st.error("Username/password is incorrect!!")


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


st.markdown("<style>.css-17z41qg p{font-size:22px;}</style>",unsafe_allow_html=True)
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

# set_bg_hack("admin.jpg")


