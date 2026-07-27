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

    sketches = {
        1 : 95,
        2 : 120,
        3 : 115,
        4 : 50
        }

    try:
        if user_choose == 'a':
            print('\n[bright_cyan]Generating random sketch...[bright_cyan]')
            time.sleep(1.5)

            randomseries = random.randint(1, 4)
            maxrange = sketches[randomseries]
            randomsketch = random.randint(1, maxrange)

            randomised = f"http://montypython.50webs.com/scripts/Series_{randomseries}/{randomsketch}.htm"
            link = requests.get(randomised, headers=headers)
            bs = BeautifulSoup(link.content, 'html.parser')

            content = bs.find('body')
            for para in content.find_all('p'):
                print("\n", para.text.strip())
            print("[bright_cyan]source:[bright_cyan]", randomised)

        elif user_choose == 'b':
            time.sleep(0.5)
            print("[bright_cyan]\nMonty Python's Flying Circus only aired for 4 season.\nWhich one do you prefer?[bright_cyan]")
            user_pick = input("\nThis is your answer box: ")
            if int(user_pick) in sketches:
                print("[bright_cyan]\nPicking up funny sketch for you ...[bright_cyan]")
                time.sleep(2)
                maxrange = sketches[int(user_pick)]
                random_sketch = random.randint(1, maxrange)
                randomised = f"http://montypython.50webs.com/scripts/Series_{int(user_pick)}/{random_sketch}.htm"
                link = requests.get(randomised, headers=headers)
                bs = BeautifulSoup(link.content, 'html.parser')
                content = bs.find('body')
                for para in content.find_all('p'):
                    print("\n", para.text.strip())
                print("[bright_cyan]source:[bright_cyan]", randomised)
            else:
                time.sleep(1)
                print("\n[dark_orange]I'm afraid that series has never been aired.[dark_orange]")
        elif user_choose == 'c':
            time.sleep(1)
            print("[bright_cyan]\nFour seasons aired, which one do you prefer?[bright_cyan]")
            series = input("\nEnter your season of choice: ")
            validseries = [1, 2, 3, 4]
            userseries = int(series)
            if userseries in validseries:
                time.sleep(0.5)
                print(f"[bright_cyan]\nSketches from season {userseries}:")
                if userseries == 1:
                    file = open("first_season.txt", "r")
                    for line in enumerate(file, start=1):
                        print("[dark_olive_green3]", line, "[dark_olive_green3]")
                    usersketch = input("\nEnter the number: ")
                    randomised = f"http://montypython.50webs.com/scripts/Series_{userseries}/{int(usersketch)}.htm"
                    link = requests.get(randomised, headers=headers)
                    bs = BeautifulSoup(link.content, 'html.parser')
                    content = bs.find('body')
                    for para in content.find_all('p'):
                        print("\n", para.text.strip())
                    print("[bright_cyan]source:[bright_cyan]", randomised)
                elif userseries == 2:
                    file = open("second_season.txt", "r")
                    for line in enumerate(file, start=1):
                        print("[dark_olive_green3]", line, "[dark_olive_green3]")
                    usersketch = input("\nEnter the number: ")
                    randomised = f"http://montypython.50webs.com/scripts/Series_{userseries}/{int(usersketch)}.htm"
                    link = requests.get(randomised, headers=headers)
                    bs = BeautifulSoup(link.content, 'html.parser')
                    content = bs.find('body')
                    for para in content.find_all('p'):
                        print("\n", para.text.strip())
                    print("[bright_cyan]source:[bright_cyan]", randomised)
                elif userseries == 3:
                    file = open("third_season.txt", "r")
                    for line in enumerate(file, start=1):
                        print("[dark_olive_green3]", line, "[dark_olive_green3]")
                    usersketch = input("\nEnter the number: ")
                    randomised = f"http://montypython.50webs.com/scripts/Series_{userseries}/{int(usersketch)}.htm"
                    link = requests.get(randomised, headers=headers)
                    bs = BeautifulSoup(link.content, 'html.parser')
                    content = bs.find('body')
                    for para in content.find_all('p'):
                        print("\n", para.text.strip())
                    print("[bright_cyan]source:[bright_cyan]", randomised)
                elif userseries == 4:
                    file = open("fourth_season.txt", "r")
                    for line in enumerate(file, start=1):
                        print("[dark_olive_green3]", line, "[dark_olive_green3]")
                    usersketch = input("\nEnter the number: ")
                    randomised = f"http://montypython.50webs.com/scripts/Series_{userseries}/{int(usersketch)}.htm"
                    link = requests.get(randomised, headers=headers)
                    bs = BeautifulSoup(link.content, 'html.parser')
                    content = bs.find('body')
                    for para in content.find_all('p'):
                        print("\n", para.text.strip())
                    print("[bright_cyan]source:[bright_cyan]", randomised)
        elif user_choose == 'd':
            time.sleep(1)
            print("[bright_cyan]\nGood choice! And that is my favourite sketch!")
            time.sleep(1)
            print("\n[bright_cyan]Enjoy the bit![bright_cyan]")
            time.sleep(1)
            here = f"http://montypython.50webs.com/scripts/Series_3/21.htm"
            link = requests.get(here, headers=headers)
            bs = BeautifulSoup(link.content, 'html.parser')
            content = bs.find('body')
            for para in content.find_all('p'):
                print("\n", para.text.strip())
            print("[bright_cyan]source:[bright_cyan]", randomised)
        else:
            raise IndexError
    except IndexError:
        time.sleep(1)
        print('\nNo question related to that answer.')
