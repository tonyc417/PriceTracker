import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Bose-Solo-Sound-System-732522-1110/dp/B01AWLPUAG/ref=sr_1_3?keywords=bose+soundbar&qid=1562796651&s=gateway&sr=8-3'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle')

print(title)