import time
import base64
from PIL import Image
import streamlit as st
import pandas as pd
import database as db
from datetime import datetime
import re
import uuid
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
          <source src="https://cdn.dribbble.com/users/527197/screenshots/17579286/media/079c9863ed47ac7b765bbeb85990cd2f.mp4")>
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

header1("Slang Generator")


# Body-

def text(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:16px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def note(url):
     st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:18px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header4(url):

    st.markdown(f'<p style=color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)

def header41(url):

    st.markdown(f'<p style=text-align:center;color:#ffffff;font-size:20px;border-radius:2%;font-weight:brush script MT;font-family:lato;">{url}</p>', unsafe_allow_html=True)


header41("Enter your slang name and its description and you are good to go:)")

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

# NSFW words - 
nsfw_words = ['mound of venus', 'asslover', 's&m', 'queaf', 'whitetrash', 'meatrack', 'ra8s', 'pimp', 'urine', 'whit', 'randy', 'herpes', 'niglet', 'narcotic', 'pudboy', 'rimming', 'boner', 'pornography', 'poop chute', 'israel', 'dong', 'slanteye', 'muffdiving', 'jiggabo', 'assassination', 'peepshpw', 'popimp', 'girl on', 'testicles', 'laid', 'molestor', 'peni5', 'tranny', 'barface', 'hell', 'arsehole', 'pissed', 'sixsixsix', 'execute', 'shitty ', 'conspiracy', 'hamas', 'cunilingus', 'bitcher', 'muslim', 'pee', 'niggled', 'muffindiver', 'cocksman', 'scag', 'aroused', 'niggling', 'fingerfucker ', 'nlggor', 'niggaz', 'assfuck', 'slant', 'urinate', 'mothafucked ', 'fungus', 'retard', 'gummer', 'venus mound', 'alla', 'spaghettinigger', 'piss', 'mickeyfinn', 'fuckers', 'jizzim', 'tramp', 'quashie', 'prince albert piercing', 'hardon', 'menage a trois', 'bukkake', 'shag', 'australian', 'raped', 'buggery', 'deth', 'weenie', 'lickme', 'reverse cowgirl', 'tonguetramp', 'cum', 'copulate', 'gun', 'schlong', 'cunn', 'damnit', 'crackpipe', 'buttmuncher', 'cameltoe', 'camgirl', 'hotpussy', 'cuntfucker', 'slave', 'sluts', 'ball licking', 'hentai', 'jackshit', 'dickman', 'doo-doo', 'gook', 'crimes', 'ho', 'bomd', 'shitdick', 'slapper', 'urinary', 'tantra', 'nookie', 'fuckedup', 'gubba', 'niggur', 'cybersex', 'dicklicker', 'cunillingus', 'hitlerism', 'butt', 'triplex', 'busty', 'dicklick', 'kunilingus', 'asian', 'tonguethrust', 'fistfucking ', 'assmonkey', 'criminal', 'cockknob', 'koon', "children's", 'shat', 'footfucker', 'blonde action', 'spitter', 'weapon', 'dive', 'cumm', 'cuntlicking ', 'sexy-slim', 'lemon party', 'vibrater', 'upskirt', 'jijjiboo', 'fuckfriend', 'pthc', 'mothafucka', 'sniggered', 'buttfuckers', 'nutfucker', 'peehole', 'taboo', 'erection', 'nudity', 'bast', 'lesbayn', 'hummer', 'shortfuck', 'cherrypopper', 'adult', 'palestinian', 'pussylips', 'nooner', 'how to kill', 'blumpkin', 'stiffy', 'piss pig', 'beastiality', 'latin', 'butchbabes', 'spunk', 'gross', 'xx', 'crackwhore', 'butt-fuckers', 'kraut', 'pooping', 'style doggy', 'lactate', 'fecal', 'rusty trombone', 'wrinkled starfish', 'spigotty', 'dink', 'clogwog', 'whitey', 'dies', 'radical', 'slaughter', 'bollick', 'sodomite', 'balls', 'nimphomania', 'ball gag', 'poof', 'muff diver', 'jail bait', 'beaver', 'asspirate', 'bareback', 'pimpjuice', 'ballsack', 'bi-sexual', 'torture', 'limey', 'nookey', 'breastman', 'loser', 'kills', 'lesbo', 'beatyourmeat', 'lovemaking', 'munt', 'clitoris', 'fornicate', 'wet dream', 'double penetration', 'missionary position', 'bugger', 'lovejuice', 'date rape', 'eatballs', 'handjob', 'nlgger', 'dixiedyke', 'junglebunny', 'sonofabitch', 'goddamned', 'deep throat', 'jism', 'assclown', 'shitforbrains', 'screwyou', 'ethiopian', 'nastyslut', 'gang bang', 'lubejob', 'tied up', 'make me come', 'rimjob', 'sexfarm', 'tight white', 'lezbe', 'lezbo', 'tribadism', 'butt-bang', 'asskiss', 'sadism', 'biteme', 'angie', 'abortion', 'murderer', 'motherfucker', 'sextoy', '2g1c', 'doggy style', 'cunntt', 'cooly', 'ball sack', 'sodom', 'slideitin', 'fudge packer', 'fatfuck', 'god', 'gipp', 'communist', 'felatio ', 'libido', 'xtc', 'cuntfuck', 'niggardly', 'fuckface', 'faggot', 'protestant', 'trailertrash', 'headfuck', 'shav', 'dickweed', 'refugee', 'trannie', 'giant cock', 'sexhound', 'slut', 'dead', 'titlover', 'wank', 'moslem', 'krappy', 'black cock', 'idiot', 'tortur', 'erotic', 'donkey punch', 'dirty pillows', 'cockcowboy', 'sucker', 'cocktail', 'doom', 'hymen', 'vibr', 'terrorist', 'mufflikcer', 'phonesex', 'teste', 'pisshead', 'slime', 'brea5t', 'tea bagging', 'slutt', 'cumbubble', 'blackout', 'hijacking', 'premature', 'sextogo', 'arse', 'racist', 'jimfish', 'flydye', 'juggs', 'jade', 'wigger', "niggard's", 'jigg', 'dumb', 'devilworshipper', 'firing', 'gatorbait', 'murder', 'chinese', 'fastfuck', 'spik', 'nuke', 'bastinado', 'kondum', 'pansy', 'destroy', 'ikey', 'women rapping', 'titfucker', 'crime', 'swinger', 'shitola', 'killer', 'fart', 'booby', 'pimpsimp', 'coon', 'strap on', 'zigabo', 'faith', 'bisexual', 'gangsta', 'teat', 'boobies', 'kafir', 'dp action', 'jugs', 'husky', 'homoerotic', 'twinkie', 'spooge', 'kink', 'sleezebag', 'gay', 'homo', 'slutwhore', 'dickless', 'cumfest', 'israeli', 'fuk', 'niggardliness', 'nigr', 'goddamit', 'sandnigger', 'dope', 'insest', 'foreskin', 'acrotomophilia', 'dumbbitch', 'fuckmonkey', 'pubiclice', 'cyberslimer', 'titfuck', 'cummer', 'kumquat', 'one guy one jar', 'fire', 'sexo', 'carruth', 'cocktease', 'trisexual', 'pric', 'rabbi', 'gypp', 'cunnilingus', 'dipshit', 'welfare', 'arabs', 'transvestite', 'tnt', 'penile', 'mothafuckings', 'peckerwood', 'enemy', 'negroid', 'genital', 'gangbanger', 'queef', 'strapon', 'thicklips', 'female squirting', 'flydie', 'crabs', 'christ', 'ejaculate', 'carpet muncher', 'lucifer', 'butchdyke', 'vatican', 'skumbag', 'horseshit', 'eunuch', 'dickforbrains', 'bondage', 'kumbullbe', 'crack', 'niggerhole', 'niggard', 'rosy palm', 'assranger', 'beat-off', 'bastard ', 'asspuppies', 'jiggerboo', 'cuntlick ', 'pommie', 'doggie style', 'lezz', 'jesuschrist', 'nazi', 'feltch', 'chode', 'pleasure chest', 'wetback', 'zipperhead', 'necro', 'goddamnmuthafucker', 'whiskeydick', 'slopy', 'executioner', 'colored', 'ethnic', 'turnon', 'hole', 'nofuckingway', 'mastrabator', 'jack off', 'orgies', 'pisses ', 'blow j', 'criminals', 'cockqueen', 'tosser', 'snownigger', 'holestuffer', 'dipstick', 'mofo', 'nipplering', 'minority', 'italiano', 'palesimian', 'poo', 'horn', 'rape', 'genitals', 'conservative', 'jebus', 'bullcrap', 'dick', 'cumqueen', 'spread legs', 'cancer', 'kaffir', 'mocky', 'suckmytit', 'vorarephilia', 'naked', 'shited', 'nigg', 'spermhearder', 'whore', 'african', 'disease', 'lovebone', 'spreadeagle', 'coprolagnia', 'humping', 'suicide girls', 'bong', 'pole smoker', 'shrimping', 'gin', 'purinapricness', 'sexslave', 'big knockers', 'iblowu', 'pissin ', 'skank', 'lotion', 'asshole', 'easyslut', 'mothafucker', 'whiz', 'lsd', 'cocksucked ', 'hosejob', 'wanker', 'cumjockey', 'eat my ass', 'lovegoo', 'whites', 'propaganda', 'sexwhore', 'cunt', 'welcher', 'how to murder', 'scum', 'phuked', 'suckoff', 'shithapens', 'drug', 'auto erotic', 'sultry women', 'barenaked', 'wetspot', 'sixtynine', 'wrapping men', 'buttplug', 'jiggy', 'alligatorbait', 'flange', 'shitfit', 'dirty', 'huge fat', 'bulldyke', 'orgasm', 'bumfuck', 'deposit', 'big breasts', 'sexual', 'japanese', 'suckmyass', 'church', 'goyim', 'bohunk', 'bigass', 'fannyfucker', 'gaymuthafuckinwhore', 'babies', 'girls', 'turd', 'fuck buttons', 'fagging', 'pisser', 'sandm', 'wog', 'escort', 'octopussy', 'tinkle', 'snigger', 'groe', 'vibrator', 'dix', 'swalow', 'chin', 'niggles', 'asslicker', 'molester', 'backseat', 'geez', 'seppo', 'sexually', 'boong', 'voyeur', 'butthole', 'hoser', 'fore', 'asswhore', 'cocaine', 'skanky', 'european', 'mothafuck', 'titlicker', 'buttstain', 'penises', 'spermacide', 'mexican', 'skankybitch', 'white power', 'puddboy', 'coondog', 'stripclub', 'mockie', 'american', 'jesus', 'tushy', 'kumbubble', 'milf', 'mormon', 'ontherag', 'henhouse', 'slutty', 'big black', 'dego', 'daterape', 'phukked', 'cuntlicker ', 'failed', 'lezbefriends', 'pissing', 'bitchy', 'pohm', 'kigger', 'nastywhore', 'bangbros', 'upthebutt', 'cohee', 'fistfuck', 'fuckingbitch', 'shibari', 'cigs', 'jiggaboo', 'japcrap', 'raper', 'jackass', 'orgasim ', 'sexed', 'jackoff', 'baby batter', 'toilet', 'tampon', 'uk', 'porn', 'snowballing', 'goldenshower', 'titties', 'towelhead', 'titjob', 'abo', 'molestation', 'fok', 'crapola', 'foursome', 'suicide', 'scrotum', 'cumming', 'niggerhead', 'pussie', 'abuse', 'analannie', 'cocksucking', 'breastjob', 'blonde on blonde action', 'paedophile', 'kumming', 'reestie', 'suckme', 'willie', 'shhit', 'titbitnipply', 'hot chick', 'skankwhore', 'fudgepacker', 'dragqueen', 'deapthroat', 'barelylegal', 'circlejerk', 'shinola', 'hookers', 'flatulence', 'scat', 'damn', 'mafia', 'anus', 'gokkun', 'argie', 'buttpirate', 'goregasm', 'fagot', 'fuks', 'redneck', 'jiga', 'cockhead', 'freakfuck', '2 girls 1 cup', 'crotchjockey', 'dripdick', 'die', 'fuckina', 'orgy', 'phungky', 'beaver cleaver', 'sexy', 'darky', 'magicwand', 'screw', 'dominatrix', 'butt-fucker', 'neonazi', 'fuckpig', 'manpaste', 'molest', 'whiskydick', 'lez', 'darkie', 'rearend', "niggardliness's", 'trojan', 'smack', 'lapdance', 'brunette action', 'hindoo', 'fourtwenty', 'deepthroat', 'moles', 'hebe', 'pommy', 'fuckher', 'stringer', 'one cup two girls', 'peck', 'backdoorman', 'male squirting', 'shiting', 'clamdiver', 'fairy', 'pussylicker', 'slav', 'nigre', 'robber', 'horny', 'penetration', 'phuking', 'cigarette', 'dyefly', 'playboy', 'golden shower', 'cumshot', 'chinamen', 'pickaninny', 'diddle', 'fatah', 'bombers', 'suckdick', 'bigbastard', 'pube', 'mosshead', 'pornking', 'terror', 'pimper', 'fuckbuddy', 'period', 'catholics', 'pistol', 'g-spot', 'doodoo', 'mockey', 'funeral', 'prickhead', 'whop', 'allah', 'pussyeater', 'cocksmith', 'executed', 'barely legal', 'niggarding', 'swastika', 'buried', 'pocho', 'nip', 'weewee', 'whiskey', 'beast', 'phone sex', 'muncher', 'fuckhead', 'smackthemonkey', 'badfuck', 'harem', 'nigerians', 'bastardo', 'shooting', 'pissoff ', 'fistfucked ', 'ginzo', 'mattressprincess', 'primetime', 'undressing', 'fuckable', 'puss', 'bbw', 'damnation', 'jeez', 'stroking', 'leather restraint', 'yankee', 'piky', 'beastality', 'cocksucer', 'goddamn', 'poopchute', 'shitfaced', 'dickhead', 'gangbanged ', 'masterbate', 'pikey', 'rosy palm and her 5 sisters', 'doggiestyle', 'bitches', 'desire', 'pansies', 'dickbrain', 'sissy', 'felch', 'penis', 'horney', 'buttmunch', 'baptist', 'assassin', 'fingering', 'cock', 'osama', 'mothafucking ', 'republican', 'wetb', 'freefuck', 'rere', 'goatse', 'transexual', 'bunghole', 'assholes', 'butt-fuck', 'nig nog', 'snowback', 'sniper', 'gangbang', 'cockfight', 'death', 'mggor', 'skankbitch', 'goy', 'twat', 'masturbate', 'usama', 'babeland', 'dickwad', 'cornhole', 'nigra', 'fuckinright', 'blue waffle', 'clit', 'niggle', 'timbernigger', 'picaninny', 'whorefucker', 'yellowman', 'ass', 'ero', 'dommes', 'nig', 'lolita', 'grostulation', 'dixiedike', 'shitfucker', 'hymie', 'sheeney', 'asswipe', 'crash', 'vomit', 'died', 'femdom', 'cameljockey', 'footfuck', 'sonofbitch', 'cleveland steamer', 'dahmer', 'feltcher', 'bitch', 'fingerfuckers', 'buttface', 'evl', 'dammit', 'lovepistol', 'twink', 'shitting', 'blind', 'reefer', 'beaver lips', 'motherlovebone', 'panties', 'fucka', 'fatass', 'lugan', 'devil', 'pornflick', 'russkie', 'fight', 'thirdleg', 'hore', 'jerk off', 'negroes', 'moron', 'shaved beaver', 'gonzagas', 'drunken', 'blackman', 'asskisser', 'crotchrot', 'motherfuckin', 'lezzo', 'fondle', 'slopey', 'clusterfuck', 'fister', 'skankfuck', 'condom', 'kill', 'taff', 'shithouse', 'cockblock', 'hoes', 'horniest', 'kunt', 'facefucker', 'assmuncher', 'bollock', 'smut', 'stupidfuck', 'assmunch', 'prostitute', 'payo', 'poorwhitetrash', 'honkey', 'farting ', 'getiton', 'bulldike', 'raping', 'arab', 'moky', 'futanari', 'nigger', 'illegal', 'hardcore', 'skinflute', 'throating', 'asspacker', 'leather straight jacket', 'raghead', 'crotch', 'goo girl', 'knobbing', 'buttman', 'glazeddonut', 'urethra play', 'africa', 'fairies', 'fuckmehard', 'shaved pussy', 'bitchin', 'fu', 'cocks', 'fucker', 'gyppie', 'kinkster', 'penthouse', 'biatch', 'wop', 'erect', 'fag', 'fuck', 'shitfull', 'vaginal', 'fraud', 'color', 'flasher', 'filipino', 'sexpot', 'sexymoma', 'boonie', 'puke', 'buttcheeks', 'cacker', 'bdsm', 'shemale', 'porchmonkey', 'violet blue', 'eatme', 'looser', 'virgin', 'assbagger', 'limy', "negro's", 'lesbian', 'hustler', 'cunteyed', 'tarbaby', 'nipples', 'dumbfuck', 'backdoor', 'wuzzie', 'sadom', 'threeway', 'pimpjuic', 'chinaman', 'brown showers', 'pubes', 'masturbating', 'bollocks', 'bunga', 'sodomize', 'goddammit', 'footstar', 'goatcx', 'chink', 'butthead', 'liquor', 'spermbag', 'jailbait', 'beatoff', 'incest', 'vagina', 'urophilia', 'niggarded', 'kaffer', 'rearentry', 'motherfucking', 'spic', 'areola', 'harder', 'greaseball', 'loverocket', 'asshore', 'perv', 'fingerfood', 'muff', 'shaggin', 'commie', 'hitler', 'burn', 'honky', 'tongue', 'fubar', 'oral', 'dildo', 'abbo', 'sniggering', 'bomb', 'omorashi', 'pedophile', 'spig', 'freakyfucker', 'swallower', 'birdlock', 'bigbutt', 'nastyho', 'goddamnes', 'pooperscooper', 'bi', 'sucks', 'jizz', 'nambla', 'puntang', 'gay sex', 'bootycall', 'reject', 'enema', 'sob', 'spankthemonkey', 'buggered', 'jewish', 'wuss', 'asslick', 'bitching', 'strip club', 'gringo', 'pendy', 'tard', 'boody', 'chocolate rosebuds', 'buttfuck', 'domination', 'faeces', 'splittail', 'clamdigger', 'shitlist', 'double dong', 'niggor', 'motherfucked', 'slimeball', 'pusy', 'pedobear', 'excrement', 'goddamnit', 'stagg', 'hijack', 'sexkitten', 'hook', 'coolie', 'phuq', 'servant', 'gyppo', 'slopehead', 'pud', 'fingerfuck ', 'dumbass', 'williewanker', 'fisting', 'crapper', 'sixtyniner', 'fetish', 'two girls one cup', 'threesome', 'bitchez', 'manhater', 'pudd', 'nympho', 'mothafuckin', 'shitted', 'hitlerist', 'semen', 'pi55', 'yaoi', 'scissoring', 'sodomise', 'ky', 'big tits', 'muffdiver', 'farty ', 'nsfw images', 'ecchi', 'dirty sanchez', 'mooncricket', 'shite', 'boom', 'asshat', 'fat', 'intercourse', 'chav', 'intheass', 'jacktheripper', 'felcher', 'spaghettibender', 'angry', 'gaysex ', 'willy', 'addict', 'russki', 'slimebucket', 'bogan', 'goodpoop', 'fuckme ', 'shitcan', 'brothel', 'rentafuck', 'footjob', 'sick', 'shitoutofluck', 'paki', 'rump', 'licker', 'nigerian', 'pindick', 'cockrider', 'felching', 'geezer', 'balllicker', 'ponyplay', 'fuckoff', 'jizzum', 'sadis', 'hodgie', 'fatfucker', 'poop', 'tits', 'bicurious', 'bombs', 'hork', 'mr hands', 'bi curious', 'sooty', 'liberal', 'prick', 'clover clamps', 'spunky', 'nymphomania', 'playgirl', 'vietcong', 'yellow showers', 'xxx', 'pecker', 'bitchslap', 'demon', 'crap', 'jihad', 'assjockey', 'macaca', 'kums', 'kinky', 'pooper', 'homicide', 'fuuck', 'poon', 'fear', 'shitfuck', 'tittie', 'wanking', 'girl on top', 'fistfucker ', 'zoophilia', 'farted ', 'nigglings', 'hiscock', 'tang', 'erotism', 'floo', 'honger', 'meth', 'beaner', 'kummer', 'wn', 'geni', 'whash', 'fuckinnuts', 'fuckin', 'tainted love', 'dyke', 'kotex', 'suck', 'poverty', 'butchdike', 'datnigga', 'uterus', 'execution', 'trots', 'luckycammeltoe', 'roach', 'swallow', 'motherfuck', 'blow', 'ball gravy', 'slutwear', 'panti', 'kissass', 'shawtypimp', 'muffdive', 'mulatto', 'noonan', 'wab', 'banging', 'tunneloflove', 'doggystyle', 'fuckwhore', 'rapist', 'homobangers', 'porno', 'barfface', 'sex', 'syphilis', 'pearlnecklace', 'sleezeball', 'sextoys', 'assman', 'german', 'shagging', 'anilingus', 'stupidfucker', 'loadedgun', 'beastial', 'shithead', 'asses', 'pussylover', 'niggah', 'gotohell', 'jigga', 'remains', 'frotting', 'thirdeye', 'fuckknob', 'inthebuff', 'nawashi', 'roundeye', 'retarded', 'mastabate', 'disturbed', 'kunnilingus', 'bung hole', 'pee-pee', 'camwhore', 'satan', 'lowlife', 'tubgirl', 'fucks', 'diseases', 'blow your l', 'krap', 'addicts', 'snatchpatch', 'bra', 'poontang', 'snatch', 'pussypounder', 'shit', 'knife', 'pu55i', 'footaction', 'footlicker', 'bimbos', 'mothafuckaz', 'pussycat', 'fucking', 'funfuck', 'piece of shit', 'boang', 'nipple', 'fuckit', 'shoot', 'quim', 'booty call', 'slutting', 'coitus', 'tit', 'spermherder', 'raging boner', 'buttfucker', 'quickie', 'grope', 'skum', 'rectum', 'kanake', 'soviet', 'lies', 'honkers', 'chinky', 'dingleberry', 'shota', 'hillbillies', 'godammit', 'fugly', 'nasty', 'ejaculation', 'waysted', 'carpetmuncher', 'nastybitch', 'camel toe', 'strappado', 'jew', 'limpdick', 'heroin', 'panty', 'polack', 'pornprincess', 'gonorrehea', 'meatbeatter', 'crotchmonkey', 'topless', 'shithappens', 'foot fetish', 'canadian', 'amateur', 'uck', 'whitenigger', 'niger', 'bigger', 'squaw', 'hand job', 'buttbang', 'titty', 'gypo', 'defecate', 'kock', 'niggaracci', 'pussyfucker', 'corruption', 'girls gone wild', 'boobs', 'ejaculated', 'shitface', 'autoerotic', 'creamy', 'bible', 'fckcum', 'knockers', 'fucck', 'whorehouse', 'cocksmoker', 'queer', 'cocklover', 'assblaster', 'bombing', 'hooters', 'forni', 'kike', 'hapa', 'bazooms', 'vulva', 'failure', 'racial', 'fuckfreak', 'snot', 'cuntsucker', 'fingerfucked ', 'scallywag', 'pixy', 'kkk', 'mastabater', 'byatch', 'whigger', 'sos', 'pussy', 'group sex', 'attack', 'fucktard', 'nook', 'marijuana', 'filipina', 'asscowboy', 'fatso', 'spit', 'bazongas', 'chickslick', 'joint', 'niggards', 'cockblocker', 'gob', 'lingerie', 'anal', 'headlights', 'dike', 'pegging', 'kaffre', 'taste my', 'crack-whore', 'lynch', 'tub girl', 'bullshit', 'explosion', 'black', 'homosexual', 'fucked', 'showtime', 'lesbin', 'kid', 'fellatio', 'nudger', "women's", 'boonga', 'choad', 'assault', 'cra5h', 'tuckahoe', 'fingerfucking ', 'hijacker', 'athletesfoot', 'pom', 'livesex', 'hostage', 'cocknob', 'nude', 'hard core', 'fuckbag', 'hobo', 'itch', 'gyp', 'kyke', 'pros', 'stupid', 'radicals', 'figging', 'fuckfest', 'hottotrot', 'kinbaku', 'sexhouse', 'violet wand', 'analsex', 'nigga', 'nittit', 'jiz ', 'suckmydick', 'pussies', 'hotdamn', 'assfucker', 'jizim', 'pixie', 'kum', 'cemetery', 'rigger', 'ethical slut', 'dolcett', 'ejaculating ', 'babe', 'cumquat', 'eatpussy', 'phuk', 'givehead', 'drunk', 'phukking', 'shiteater', 'catholic', 'hooker', 'cocksuck ', 'cocksucker', 'ball kicking', 'fuckyou', 'crappy', 'feltching', 'mideast', 'ecstacy', 'ribbed', 'dog style', 'interracial', 'tongue in a', 'pocha', 'skankywhore', 'pu55y', 'motherfuckings', 'piker', 'peepshow', 'jap', 'yiffy', 'tongethruster', "nigger's", 'breastlover', 'stroke', 'twobitwhore', 'shits', "israel's", 'jerkoff', 'bullet vibe', 'assassinate', 'killed', 'pocketpool', 'whacker', 'wtf', 'barf', 'juggalo', 'negro', 'spick', 'gyppy', 'nymph', "snigger's", 'violence', 'lovemuscle', 'dago', 'feces', 'booty', 'niggers', 'shitter', 'sodomy', 'hussy', 'pisspig', 'coprophilia', 'christian', 'pimped', 'boob', 'breast', 'sperm', 'coloured', 'redlight', 'blacks', 'orga', 'bumblefuck', 'mams', 'slavedriver', 'killing', 'uptheass', 'bestial', 'sweetness', 'heeb', 'piccaninny', 'pot', 'honk', 'jizjuice', 'fuc', 'nignog', 'mgger', 'sexing', 'virginbreaker', 'samckdaddy', 'masterblaster', 'heterosexual', 'jigger ', 'blowjob', 'lovegun', 'shitstain', 'spank', 'hiv', 'lesbain', 'mad', 'sniggers', 'jizm ', 'testicle', 'ball sucking', 'dragqween', 'guro', 'pubic', 'titfuckin', 'moneyshot', 'camslut', 'bountybar', 'assklown', 'cocky', 'transsexual', 'unfuckable', 'bestiality', 'cocklicker', 'blowjob', 'sex', 'fuck', 'porn', 'penis']

new_slang_name = st.text_input('Slang name',key=1)

new_slang_desc = st.text_input('Desc',key=2)

flag = 0
if new_slang_name!="" and new_slang_desc!="":

    data_fetched = fetch_details()
    for item in data_fetched:  
        
        if new_slang_name.lower()==item["Slang"] or new_slang_desc.lower()==item["Desc"]:

            flag = 1
            st.error("Sorry already present!!!")
            break

    for nsfw_word in nsfw_words:
        if new_slang_name.lower()==nsfw_words or nsfw_word in new_slang_desc:
            flag = 1
            st.error("Such words are not allowed!!")
            break

    if flag == 0:

        uid = uuid.uuid4()
        insert_values(str(uid), new_slang_name.lower(), new_slang_desc.lower(), 0)
        st.success("Congrats for contributing to Sevobee!!!")




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



