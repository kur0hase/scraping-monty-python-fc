from bs4 import BeautifulSoup
from rich import print
import random
import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
    }

title = r""" [bright_cyan]
  _   _                                               
 | |_| |__   ___   ___  ___ _ __ __ _ _ __   ___ _ __ 
 | __| '_ \ / _ \ / __|/ __| '__/ _` | '_ \ / _ \ '__|
 | |_| | | |  __/ \__ \ (__| | | (_| | |_) |  __/ |   
  \__|_| |_|\___| |___/\___|_|  \__,_| .__/ \___|_|   
                                     |_|              
------------------------------------------------
A very fascinating web scraper indeed. GitHub: kur0hase
"""
print(title)
print(""" [bright_cyan]
All sketches scripts scraped from http://montypython.50webs.com !
""")

valid_options = ['a', 'b', 'c', 'd']
user_choose = ''

while True:
    time.sleep(1)
    print("[bright_cyan]\nWhat would you like to do? (Monty Python Flying Circus only. This isn't a vocational guidance counsellor.[bright_cyan])")
    user_input = input("\na. Random sketch    b. Random, but can I choose?    c. Let me choose    d. Broody herr!\n\n")
    user_choose = user_input.casefold()
    if user_choose not in valid_options:
        time.sleep(0.5)
        print("\n[bright_cyan]I'm afraid that is not my question.[bright_cyan]\n")

    try:
        if user_choose == 'a':
            print('\n[bright_cyan]Generating random script...[bright_cyan]')
            time.sleep(1)

            randomseries = random.randint(1, 4)
            sketches = {
                1 : 95,
                2 : 120,
                3 : 115,
                4 : 50
            }
            maxrange = sketches[randomseries]
            randomsketch = random.randint(1, maxrange)

            randomised = f"http://montypython.50webs.com/scripts/Series_{randomseries}/{randomsketch}.htm"
            link = requests.get(randomised, headers=headers)
            bs = BeautifulSoup(link.content, 'html.parser')

            content = bs.find('body')
            if content:
                for para in content.find_all('p'):
                    print("\n", para.text.strip())
                print("[bright_cyan]source:[bright_cyan]", randomised)
            else:
                print('\nnot found.')
        elif user_choose == 'b':
            pass
        elif user_choose == 'c':
            pass
        elif user_choose == 'd':
            pass
    except:
        pass
