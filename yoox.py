from bs4 import BeautifulSoup
import requests
import re

headers = {
    'accept-language': 'en-US,en;q=0.9'
}

f = open('links.csv', 'w')

r = requests.get('https://www.yoox.com/us/men/clothing/shoponline#/dept=clothingmen&gender=U&page=1&season=X', headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
tags = soup.findAll('img', {"class": "imgFormat_20_f"})

for t in tags:
    f.write(t['alt'] + ',' + t['data-original'] +  ',https://www.yoox.com' + t.parent['href'] + '\n')

#num_pages = soup.find('a', {"data-total-page":re.compile('^[1-9]\d*$')})
#num_pages = int(num_pages.string)

for i in range(2, 3):
    r = requests.get('https://www.yoox.com/us/men/clothing/shoponline#/dept=clothingmen&gender=U&page=' + str(i) + '&season=X', headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")
    tags = soup.findAll('img', {"class": "imgFormat_20_f"})

    for t in tags:
        f.write(t['alt'] + ',' + t['data-original'] +  ',https://www.yoox.com' + t.parent['href'] + '\n')

#f = open("C:/Users/Luke/Desktop/test/page " + str(i) + ".txt", "x")

#for t in tags:
    #f.write(t['content'] + '\n')

    


