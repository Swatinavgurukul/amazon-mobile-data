
import requests
from bs4 import BeautifulSoup
req="https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mobile+phones"
req_data=requests.get(req).text
# print (req_data)
soup = BeautifulSoup(req_data, 'html.parser')
# print (soup)
data = soup.find('div',class_="lp s-padding-left-small twoColumn" )
# print data
mobile_class = data.find_all('div',class_="crwBucket" )
# print mobile_class
for mobile_data in mobile_class:
    mobile_name = mobile_data.find('div',class_="crwTitle" ).a.get_text()
    print mobile_name
    mobile_Ru = mobile_data.find('span',class_="crwActualPrice").get_text()
    print mobile_Ru
    # mobile_img = mobile_data.find('div',class_="crwProductImage").img.src
    # print mobile_img
    
