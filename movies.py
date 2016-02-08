#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup

print ('Enter city:')
city = input()
url = 'http://in.bookmyshow.com/'+city
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')

book_movie = []
i = 1
for movie_name in soup.findAll('a',{'class':'__movie-name'}):
    print (str(i)+'. '+movie_name.text)
    i += 1
    book_movie.append('http://in.bookmyshow.com'+movie_name.get('href'))

print ('Select movie no.')
movie_no = int(input())

url = book_movie[movie_no - 1]
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')

for div in soup.find_all('div', class_='cinema'):
    timings = div.find('div', class_='timings')
    print(timings.get_text(strip=True))
    