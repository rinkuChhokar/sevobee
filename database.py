from deta import Deta
import os
# from dotenv import load_dotenv


# load_dotenv(".env")

# DETA_KEY = os.getenv("DETA_KEY")

# DETA_KEY2 = os.getenv("DETA_KEY2")


deta = Deta("d0yumrp3_uStVNh2ve8EqME4dfK45SKu7bxFNTVLX")

deta1 = Deta("d0yumrp3_uStVNh2ve8EqME4dfK45SKu7bxFNTVLX")

datab = deta.Base("slangs")

usrdb = deta1.Base("login_id")


# Functions related to admin page-

# def insert_new_admin(username,name,password):

#   return usrdb.put({"key":username,"Name":name,"Password":password})
 

def fetch_admin_details():

  res = usrdb.fetch()

  return res.items


# Functions related to home page-

def insert_values(key,slang_name,slang_desc, rank_value):

  return datab.put({"key":key,"Slang":slang_name,"Desc":slang_desc, "rank":rank_value})
 

def fetch_details():

  res = datab.fetch()

  return res.items



