from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

time= datetime.now()
current_time= time.strftime('%H:%M:%S')
source=requests.get("https://www.timeanddate.com/weather/india/bangalore").text

soup= BeautifulSoup(source,'lxml')

f= open("weather.txt","a")
f.write(current_time+"\n")
weather_now=soup.find('div',id="qlook")
now=weather_now.div.text+' in bangalore'
f.write(now+'\n')
print(now)
temp="current temperature is "+ weather_now.find("div",class_="h2").text
f.write(temp+'\n')
print(temp)
sky="current sky condition = "+weather_now.p.text
f.write(sky+'\n')
print(sky)
condition= weather_now.find_all('p')[1].text
t=re.findall('[A-Z][^A-Z]*',condition)[3]+'C'
f.write(t+'\n\n')
print(t)
f.close() 