
import requests
from bs4 import BeautifulSoup
req="https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=mobile+phones"
req_data=requests.get(req).text
# print (req_data)
soup = BeautifulSoup(req_data, 'html.parser')
# print (soup)
data = soup.find('div',class_="lp s-padding-left-small twoColumn" )
# print data
mobile_name = data.find_all('div',class_="crwBucket" )
print mobile_name
for i in mobile_name:
    mobile_name1 = i.find('div',class_="crwTitle" ).a.get_text()
    print mobile_name1
    mobile_Ru = i.find('span',class_="crwActualPrice").get_text()
    print mobile_Ru
    # mobile_link = i.find('div',class_="crwProductImage").a["href"]
    # print mobile_link.get_text()
    
