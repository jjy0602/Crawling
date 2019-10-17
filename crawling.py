import requests
from bs4 import BeautifulSoup as BS
import json

MealName = {'1':'EarlyMeal.json','2':'MidMeal.json','3':'LateMeal.json','4':'CompleteMeal.json','5':'BabyMeal.json'}
def Pregnant_Crawling(html):
    temp_list=[]
    temp_dict={}

    weeks = html.select('div.lst-isotope.inner')

    index = 0
    for wk in weeks:
        img = wk.find('div',{'class':'img'}).find('a',{'class':'btn-video'}).find('img').get('src')
        href = wk.find('div',{'class':'img'}).find('a',{'class':'btn-video'}).get('href')
        category = wk.find('div',{'class':'box-info ha'}).find('p',{'class':'t1 c-blue'}).text
        title = wk.find('div',{'class':'box-info ha'}).find('strong').find('a').text.strip()
        content = wk.find('div',{'class':'box-info ha'}).find('div',{'class':'sub'}).find('p').text
        temp_list.append([img, href, category, title, content])
        temp_dict[index]={'img':img,'href':href,'category':category,'title':title,'content':content}
        index +=1
    return temp_list, temp_dict

def meals_Crawling(html):
    temp_list=[]
    temp_dict={}

    meals = html.select('div.box-prd.w2.bd')

    index = 0
    for meal in meals:
        img = meal.find('div',{'class':'img'}).find('a',{'class':'btn-video'}).find('img').get('src')
        href = meal.find('div',{'class':'img'}).find('a',{'class':'btn-video'}).get('href')
        category = meal.find('div',{'class':'box-info ha'}).find('p',{'class':'t1 c-blue'}).text
        title = meal.find('div',{'class':'box-info ha'}).find('strong').find('a').text.strip()
        content = meal.find('div',{'class':'box-info ha'}).find('div',{'class':'sub'}).find('p').text
        temp_list.append([img, href, category, title, content])
        temp_dict[index]={'img':img,'href':href,'category':category,'title':title,'content':content}
        index +=1
    return temp_list, temp_dict

def toJson(dictionarys,filename):
    with open(filename,'w',encoding='utf-8') as file:
        json.dump(dictionarys, file, ensure_ascii=False, indent='\t')



def meals_function(variable):
    # req = requests.get('https://www.maeili.com/cms/contents/contentsList.do?cateCd1=8&cateCd2=5')
    req = requests.get(variable)

    for page in range(1,6):
        req = requests.get('https://www.maeili.com/cms/contents/contentsList.do?cateCd1=8&cateCd2='+str(page)+'&cateCd3=0&gubn=0')

        meals_list=[]
        meals_dict={}

        html = BS(req.text, 'html.parser')
        meals_temp = meals_Crawling(html)
        meals_list= meals_temp[0]
        meals_dict = meals_temp[1]
        toJson(meals_dict,MealName[str(page)])

def Pregnant_function(variable):
    req = requests.get(variable)


    Pregnant_list=[]
    Pregnant_dict={}

    html = BS(req.text, 'html.parser')
    Pregnant_temp = Pregnant_Crawling(html)
    Pregnant_list= Pregnant_temp[0]
    Pregnant_dict = Pregnant_temp[1]
    toJson(Pregnant_dict,'Pregnant')
