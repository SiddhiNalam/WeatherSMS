import requests
from bs4 import BeautifulSoup
import way2sms

page = requests.get("https://weather.com/en-IN/weather/today/l/INXX0102:1:IN")
soup = BeautifulSoup(page.content, 'html.parser')
today = soup.find(class_="today_nowcard-phrase").get_text()
username=' '#Enter your credentials
password=' '
q=way2sms.sms(username,password)
q.send( username, today )
q.logout()

print(today)





# print(soup.prettify())
#**************************************************************************************************************

