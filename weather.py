from tkinter import *
from PIL import ImageTk,Image
import urllib.request,urllib.error
import json
global city_name

root=Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title("WETHER APP BY CHARAN")
root.iconbitmap("logo.ico")
bgimg=ImageTk.PhotoImage(file="landscape.png")
img_label=Label(root,image=bgimg)
img_label.place(relwidth=1,relheight=1)

def get_weather():
    global city_name,js,data,display_content
    display_content=Label(lower_frame)
    print(display_content)
    url="http://api.openweathermap.org/data/2.5/forecast?q="+str(city_name.get())+"&appid=de6ef50b9b73ae0a6961a9086b2cfd6a"
    city_name.delete(0,END)
    try:
        global response
        response=urllib.request.urlopen(url)

    except urllib.error.HTTPError:
        display_content.destroy()
        display_content=Label(lower_frame,bg="#ffffff",text="No city found.")
        display_content.place(relx=0.1,rely=0.5)
        return
    except urllib.error.URLError:
        display_content.destroy()
        display_content=Label(lower_frame,bg="#ffffff",text="Check Your Internet Connection.")
        display_content.place(relx=0.1,rely=0.5)
        return
    global data
    data=response.read()
    js=json.loads(data)
    if js["cod"]=="200":
        name=js["city"]["name"]
        country=js["city"]["country"]
        temp=str(int(js["list"][0]["main"]["temp"]-270))
        condition=js["list"][0]['weather'][0]['description']
        final_str='City: %s  %s \nCondition: %s \n Temparature(°C): %s  '% (name,country,condition,temp)
        display_content.destroy()
        display_content=Label(lower_frame,bg="#ffffff",text=final_str)
        display_content.place(relx=0.1,rely=0.5)



frame=Frame(root,bg="#80c1ff",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.15,anchor='n')

city_name=Entry(frame,text="WEATHER ALL OVER THE WORLD",font=60)
city_name.place(relwidth=0.65,relheight=1)

button=Button(frame,text="GET WEATHER",font=40,command=get_weather)
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=Frame(root,bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5,rely=0.32,relwidth=0.75,relheight=0.65,anchor='n')

content=Label(lower_frame,bg="#ffffff")
content.place(relwidth=1,relheight=1)

root.mainloop()
