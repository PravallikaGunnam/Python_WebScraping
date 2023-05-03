
##import section
import requests
import pandas
from bs4 import BeautifulSoup

##Taking permission from particular website
response=requests.get("https://www.flipkart.com/search?q=iphone+13&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+13%7CMobiles&requestId=e0fbf6de-5053-4344-9e96-1cf10d469c35&as-searchtext=iph")
# print(response)

##taking content from website in unstructured format
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)

##making that above content as structure using findall(we can take "class or id")
## getting all names from website
names=soup.find_all('div',class_='_4rR01T')
# print(names)#unstructured format names
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)

# getting all prices from website
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
# print(price)

# getting all ratings from website
ratings=soup.find_all('div',class_='_3LWZlK')
rating=[]
for i in ratings[0:10]:
    d=i.get_text()
    rating.append(float(d))
# print(rating)

#getting reviews from website
reviews=soup.find_all('span',class_='_2_R_DZ')
review=[]
for i in reviews[0:10]:
    d=i.get_text()
    review.append(d)
# print(review)

#getting features from website
features=soup.find_all('li',class_='rgWa7D')
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)
# print(feature)

#getting links from website
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:10]:
    d="https://www.flipkart.com/"+i['href']
    link.append(d)
# print(link)


## getting images
images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:10]:
    d=i['src']
    ## d=i.div.img['src']if the link has only one class then we need to go with this code
    image.append(d)
# print(image)

df=pandas.DataFrame()
# print(df)
##if we get error incase index outbound methods:"'names':pandas.Series(names)....'names':name.pandas.Series()
data={'Names':name,
      'Price':price,
      'Ratings':rating,
      'Reviews':review,
      'Features':feature,
      'Links':link,
      'Images':image}
# print(data)
df=pandas.DataFrame(data)
# print(df)#data in tabular form
df.to_csv("mobiles.csv")

