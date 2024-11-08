import requests
import xml.etree.ElementTree as reader
from tkinter import *
from tkinter import ttk
import API_KEY

def getWeather(*args):
    searchQuery=str(city.get())
    reqResponse=requests.get(F"http://api.weatherapi.com/v1/current.xml?key={API_KEY.api}&q={searchQuery}&aqi=no")

    if reqResponse.status_code==200:
        
        xmlData=reader.fromstring(reqResponse.text)

        # print(xmlData.find("location/name").text)

        region.set(xmlData.find("location/region").text)

        temp_c=(xmlData.find("current/temp_c").text)
        temp_f=(xmlData.find("current/temp_f").text)
        temp.set(f"{temp_c}˚C / {temp_f}˚F")

        feelslike_c=(xmlData.find("current/feelslike_c").text)
        feelslike_f=(xmlData.find("current/feelslike_f").text)
        feelslike.set(f"{feelslike_c}˚C / {feelslike_f}˚F")

        wind_kph=str(xmlData.find("current/wind_kph").text)
        wind_mph=str(xmlData.find("current/wind_mph").text)
        wind.set(f"{wind_kph} kmph / {wind_mph} mph")

        wind_dir.set(xmlData.find("current/wind_dir").text)

        localtime.set(xmlData.find("location/localtime").text)
        last_updated.set(xmlData.find("current/last_updated").text)

        status.set("Success!")

    else:

        status.set("Error :(")


root=Tk()
root.title("Weather")

mainframe=ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0,row=0,sticky=(N,E,W,S))
root.columnconfigure(0)
root.rowconfigure(0)

ttk.Label(mainframe, text="city", anchor=W, font=("Helvetica", 16)).grid(column=0,row=0,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=0,sticky=(W,E))
city=StringVar()
ttk.Entry(mainframe, textvariable=city).grid(column=2, row=0, sticky=[W,E])


ttk.Label(mainframe, text="region", anchor=W, font=("Helvetica", 16)).grid(column=0,row=1,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=1,sticky=(W,E))
region=StringVar()
ttk.Label(mainframe, textvariable=region, anchor=CENTER).grid(column=2, row=1, sticky=[W,E])


ttk.Label(mainframe, text="temperature", anchor=W, font=("Helvetica", 16)).grid(column=0,row=2,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=2,sticky=(W,E))
temp=StringVar()
ttk.Label(mainframe, textvariable=temp, anchor=CENTER).grid(column=2, row=2, sticky=[W,E])


ttk.Label(mainframe, text="feels like", anchor=W, font=("Helvetica", 16)).grid(column=0,row=3,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=3,sticky=(W,E))
feelslike=StringVar()
ttk.Label(mainframe, textvariable=feelslike, anchor=CENTER).grid(column=2, row=3, sticky=[W,E])


ttk.Label(mainframe, text="wind speed", anchor=W, font=("Helvetica", 16)).grid(column=0,row=4,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=4,sticky=(W,E))
wind=StringVar()

ttk.Label(mainframe, textvariable=wind, anchor=CENTER).grid(column=2, row=4, sticky=[W,E])


ttk.Label(mainframe, text="wind direction", anchor=W, font=("Helvetica", 16)).grid(column=0,row=5,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=5,sticky=(W,E))
wind_dir=StringVar()
ttk.Label(mainframe, textvariable=wind_dir, anchor=CENTER).grid(column=2, row=5, sticky=[W,E])


ttk.Label(mainframe, text="local time", anchor=W, font=("Helvetica", 16)).grid(column=0,row=6,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=6,sticky=(W,E))
localtime=StringVar()
ttk.Label(mainframe, textvariable=localtime, anchor=CENTER).grid(column=2, row=6, sticky=[W,E])


ttk.Label(mainframe, text="last updated", anchor=W, font=("Helvetica", 16)).grid(column=0,row=7,sticky=(W,E))
ttk.Label(mainframe, text="   :   ", anchor=CENTER, font=("Helvetica", 16)).grid(column=1,row=7,sticky=(W,E))
last_updated=StringVar()
ttk.Label(mainframe, textvariable=last_updated, anchor=CENTER).grid(column=2, row=7, sticky=[W,E])

ttk.Label(mainframe).grid(column=0, row=8)

# Create the status label
status = StringVar()
status.set("Enter a city and click Go!")  # Default message
ttk.Label(mainframe, textvariable=status, anchor=CENTER).grid(column=0, row=9, sticky=[W, E])

# Create the Go! button
ttk.Button(mainframe, text="Go!", command=getWeather, width=10).grid(column=2, row=9, sticky=[W, E], columnspan=2)
root.bind("<Return>", getWeather)

ttk.Label(mainframe, text="v1.0.0", anchor=E, font=("Arial", 10)).grid(column=2, row=10, sticky=[W,E])

root.mainloop()