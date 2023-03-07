# 1) pip install deta
from deta import Deta

# 2) initialize with a project key
deta = Deta("d0yumrp3_uStVNh2ve8EqME4dfK45SKu7bxFNTVLX")

# 3) create and use as many DBs as you want!
# slangs_info = deta.Base("slangs")

# slangs_info.insert({
#     "Slang": "idk",
#     "Desc": "I don't know"
# })

# fetch_res = slangs_info.fetch()

# for item in fetch_res.items:
#     print(item)


# slangs_info = deta.Base("login_id")

# slangs_info.insert({
#     "Username": "rinku001",
#     "Pasword": "chhokar@123"
# })

# fetch_res = slangs_info.fetch()

# for item in fetch_res.items:
#     print(item)

