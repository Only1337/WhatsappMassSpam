from datetime import datetime
import calendar
import json
import time
import requests as r

config = open('config.json')
config = json.loads(config.read())
number = config['number']
msg = input("Enter your message here: ")


def sendMessage(apiNumber,target,message):
    d = datetime.utcnow()
    getUnix = calendar.timegm(d.utctimetuple())
    apiData = {"app": {"id": apiNumber,"time": getUnix,"data": {"recipient": {"id": target,},"message": [{"time": getUnix,"type": "text","value": message}]}}}
    ok = r.post("https://whapi.io/api/send", json=apiData)
    print("["+str(ok.status_code)+"] ["+str(getUnix)+"] ["+str(ok.content)+"]") # "success sent +"+target 

with open("victims.txt", "r") as a_file:
  for line in a_file:
    victim = line.strip()
    print(sendMessage(number,victim,msg))