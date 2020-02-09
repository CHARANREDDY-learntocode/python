import urllib.request
import json
from tkinter import *
root=Tk()
url="http://api.openweathermap.org/data/2.5/forecast?q="+str(input("enter city"))+"&appid=de6ef50b9b73ae0a6961a9086b2cfd6a"
response=urllib.request.urlopen(url)
data=response.read()
js=json.loads(data)
name=js["city"]["name"]
country=js["city"]["country"]
temp=str(int(js["list"][0]["main"]["temp"]-270))
condition=js["list"][0]['weather'][0]['description']
print(name)
print(country)
print(temp)
print(condition)
if js["cod"]=="200":
    name=js["city"]["name"]
    country=js["city"]["country"]
    temp=str(int(js["list"][0]["main"]["temp"]-270))
    condition=js["list"][0]['weather'][0]['description']
    final_str='City: %s  %s \nCondition: %s \n Temparature(°C): %s  '% (name,country,condition,temp)
    display_content=Label(root,bg="#ffffff",text=final_str)
    display_content.place(relx=0.1,rely=0.5)
root.mainloop()
