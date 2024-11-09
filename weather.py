import requests           #imported for http requests
import xml.etree.ElementTree as reader           #imported to parse xml
from tkinter import Tk, StringVar, ttk, N, E, W, S, CENTER        #imports the necessary parts of tkinter module
import API_KEY           #imports py file where api key is stored

def getWeather(*args):             #defined getWeather() -- *args lets you bind the <Return> key to the func
    searchQuery=str(city.get())         #taking user input from entry parameter
    reqResponse=requests.get(f"http://api.weatherapi.com/v1/current.xml?key={API_KEY.api}&q={searchQuery}&aqi=no")            #building http request

    if reqResponse.status_code==200:             #http request status is 200 when successful
        
        status.set("Fetching Data...")

        xmlData=reader.fromstring(reqResponse.text)          #reading xml and storing as string in xmlData

        # print(xmlData.find("location/name").text)

        region.set(xmlData.find("location/region").text)       #fetching and setting region

        temp_c=(xmlData.find("current/temp_c").text)
        temp_f=(xmlData.find("current/temp_f").text)
        temp.set(f"{temp_c}˚C / {temp_f}˚F")           #fetching and setting temperature data

        feelslike_c=(xmlData.find("current/feelslike_c").text)
        feelslike_f=(xmlData.find("current/feelslike_f").text)
        feelslike.set(f"{feelslike_c}˚C / {feelslike_f}˚F")            #fetching and setting feels-like data

        wind_kph=str(xmlData.find("current/wind_kph").text)
        wind_mph=str(xmlData.find("current/wind_mph").text)
        wind.set(f"{wind_kph} kmph / {wind_mph} mph")             #fetching and setting wind speed data

        wind_dir.set(xmlData.find("current/wind_dir").text)       #fetching and setting wind direction data

        localtime.set(xmlData.find("location/localtime").text)        #fetching and setting local time
        last_updated.set(xmlData.find("current/last_updated").text)        #fetching and setting time data was last updated

        status.set("Success!")           #setting status in case of success

    else:

        status.set("Error :(")          #setting status in case of failure


root=Tk()       #initializing app
root.title("Weather")        #assigning app title

mainframe=ttk.Frame(root, padding="12 12 12 12")        #initializing mainframe
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))
root.columnconfigure(0)
root.rowconfigure(0)

#city field
ttk.Label(mainframe, text="city", anchor=W, font=("Helvetica", 16)).grid(column=0,row=0,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=0,sticky=(W,E))
city=StringVar()
ttk.Entry(mainframe, textvariable=city).grid(column=2, row=0, sticky=[W,E])

#region field
ttk.Label(mainframe, text="region", anchor=W, font=("Helvetica", 16)).grid(column=0,row=1,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=1,sticky=(W,E))
region=StringVar()
ttk.Label(mainframe, textvariable=region, anchor=CENTER).grid(column=2, row=1, sticky=[W,E])

#temperature field
ttk.Label(mainframe, text="temperature", anchor=W, font=("Helvetica", 16)).grid(column=0,row=2,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=2,sticky=(W,E))
temp=StringVar()
ttk.Label(mainframe, textvariable=temp, anchor=CENTER).grid(column=2, row=2, sticky=[W,E])

#feels like field
ttk.Label(mainframe, text="feels like", anchor=W, font=("Helvetica", 16)).grid(column=0,row=3,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=3,sticky=(W,E))
feelslike=StringVar()
ttk.Label(mainframe, textvariable=feelslike, anchor=CENTER).grid(column=2, row=3, sticky=[W,E])

#wind speed field
ttk.Label(mainframe, text="wind speed", anchor=W, font=("Helvetica", 16)).grid(column=0,row=4,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=4,sticky=(W,E))
wind=StringVar()
ttk.Label(mainframe, textvariable=wind, anchor=CENTER).grid(column=2, row=4, sticky=[W,E])

#wind direction field
ttk.Label(mainframe, text="wind direction", anchor=W, font=("Helvetica", 16)).grid(column=0,row=5,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=5,sticky=(W,E))
wind_dir=StringVar()
ttk.Label(mainframe, textvariable=wind_dir, anchor=CENTER).grid(column=2, row=5, sticky=[W,E])

#local time field
ttk.Label(mainframe, text="local time", anchor=W, font=("Helvetica", 16)).grid(column=0,row=6,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=6,sticky=(W,E))
localtime=StringVar()
ttk.Label(mainframe, textvariable=localtime, anchor=CENTER).grid(column=2, row=6, sticky=[W,E])

#time last updated field
ttk.Label(mainframe, text="last updated", anchor=W, font=("Helvetica", 16)).grid(column=0,row=7,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=7,sticky=(W,E))
last_updated=StringVar()
ttk.Label(mainframe, textvariable=last_updated, anchor=CENTER).grid(column=2, row=7, sticky=[W,E])

ttk.Label(mainframe).grid(column=0, row=8)

#status label
status = StringVar()
status.set("Enter a city and click Go!")  # Default message
ttk.Label(mainframe, textvariable=status, anchor=CENTER).grid(column=0, row=9, sticky=[W, E])

#action button
ttk.Button(mainframe, text="Go!", command=getWeather, width=10).grid(column=2, row=9, sticky=[W, E], columnspan=2)
root.bind("<Return>", getWeather)

ttk.Label(mainframe, text="v1.0.0", anchor=E, font=("Arial", 10)).grid(column=2, row=10, sticky=[W,E])

root.mainloop()            #looping the program so it doesn't close after execution