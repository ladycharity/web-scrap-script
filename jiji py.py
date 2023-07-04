from bs4 import BeautifulSoup as soup
import requests

req = requests.get("https://jiji.ng/jobs")
beauty = soup(req.content,"html.parser")
JobName = beauty("div",{"qa-advert-list-item-title b-list-advert-base__item-title"})
#print(JobName[0].text.strip())

beauty = soup(req.content,"html.parser")
JobType = beauty("div",{"b-list-advert-base__item-attr"})
#print(JobType[0].text.strip())


beauty = soup(req.content,"html.parser")
Salary = beauty("div",{"qa-advert-price"})
message=  f"{JobName[0].text.strip()}\n{JobType[0].text.strip()}\n{Salary[0].text.strip()}"
#print(message)
count = 0
for b,h,g in zip (JobName,JobType,Salary):
    count+=1
    print(count,"\n","JobName:", b.text.strip(),"\n","JobType:", h.text.strip(),"\n","Salary:",g.text.strip(),"\n")






