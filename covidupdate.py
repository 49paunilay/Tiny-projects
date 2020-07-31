import requests
import json
import time
from win10toast import ToastNotifier

def myupdater():
    variablerq=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=variablerq.json()
    output='Confirmed cases {} \n Deaths {} \n Recovered {}'.format(data["cases"],data["deaths"],data["recovered"])
    while True:
        toastnotifierinstance=ToastNotifier()
        toastnotifierinstance.show_toast('Covid 19 update World Wide',output , duration= 15)
        time.sleep(60)

if __name__ == '__main__':
    myupdater()
    