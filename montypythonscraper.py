from bs4 import BeautifulSoup
from rich import print
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
    user_input = input("What would you like to do? (Monty Python Flying Circus only. This isn't a vocational guidance counsellor.)\na. Random sketch    b. Random, but can I choose?    c. Let me choose    d. Broody herr!\n\n")

    if user_input.casefold() not in valid_options:
        time.sleep(0.5)
        user_choose = user_input
        print("\n[bright_cyan]I'm afraid that is not my question.[bright_cyan]\n")
    else:
        break

    

# series = [1, 2, 3, 4]
# sketches_1 = 95
# sketches_2 = 120
# sketches_3 = 115
# sketches_4 = 50
# totalsketches = 380

# link = requests.get("http://montypython.50webs.com/scripts/Series_2/70.htm", headers=headers)
# print(link.status_code)
# bs = BeautifulSoup(link.content, 'html.parser')
# # print(bs.prettify())

# content = bs.find('body')
# if content:
#     for para in content.find_all('p'):
#         print(para.text.strip())
# else:
#     print('not found')