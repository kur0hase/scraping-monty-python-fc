from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:153.0) Gecko/20100101 Firefox/153.0",
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive"
    }




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