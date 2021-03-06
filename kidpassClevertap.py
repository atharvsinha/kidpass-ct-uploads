import pandas as pd
import requests
import time
from flask import Flask, jsonify, render_template, request
import datetime
import pytz

dotw = {
    'Mon':'monday',
    'Tue':'tuesday',
    'Wed':'wednesday',    
    'Thu':'thursday',
    'Fri':'friday',
    'Sat':'saturday',
    'Sun':'sunday',    
}



app = Flask(__name__)
x = []
@app.route('/uploaded', methods=['GET' ,'POST'])
def get_file(): 
    evt = {}
    usr = {}
    data = []
    if request.method == 'POST':
        
        f = dict(request.form)
        email = f['Email']
        data = str(email).split('\n')
        ts = int(round(time.time(), 0))
        cName = ''
        age = 0
        pName = ''
        mail = ''
        phone = '+'
        categ = '' 
        date = ''
        classname = ''
        for i in data:
    
            if 'Attendee:' in i:
                cName = i.split(':')[-1].strip()
            elif 'Age:' in i:
                age = i.split(':')[-1].strip()
            elif 'Guardian:' in i:
                pName = i.split(':')[-1].strip()
            elif 'Email:' in i:
                mail = i.split(':')[-1].strip()
            elif 'Phone:' in i:
                phone = i.split(':')[-1].strip()
            elif 'Explorers -' in i:
                classname = i
                categ = i.strip().split()[0]
            elif  'PST'in i or 'PDT' in i:
                date = i.split()
            
            
        if date[-1] == 'PST':
            date[-1]=='PDT'

        classDate = 0
            
        
        if 'PM' not in date:
            classDate = datetime.datetime(2022, int(date[1].split('/')[0]), int(date[1].split('/')[1].split(',')[0]), int(date[2].split(':')[0])+7, int(date[2].split(':')[1]),0) 
            classDate = classDate.timestamp()
            
        else:
            classDate = datetime.datetime(2022, int(date[1].split('/')[0]), int(date[1].split('/')[1].split(',')[0]), int(date[2].split(':')[0])+19, int(date[2].split(':')[1]),0) 
            classDate = classDate.timestamp()
        
        evt['ts'] = usr['ts'] = ts
        evt['identity'] = usr['identity'] = mail
        evt['type'] = 'event'
        evt['evtName'] = 'drop in slot booked'
        evt['evtData'] = {
            'category':categ.lower(),
            'class name': classname,
            'platform': 'web',
            'course': 'curio',
            'class type': 'group',
            'utm source':'kidpass',
            'utm medium':'email webhook',
            'utm campaign':'explorer',
            'channel':'kidpass',
            'class positioning':'drop-in',
            'date':'$D_'+ str(classDate).split('.')[0],
            'time slot':''.join(date[2:7]),
            'time zone': date[-1],
            'day of the week':dotw[date[0]],
            'transaction date':'$D_'+str(ts),
        }
        
        usr['type'] = 'profile'
        usr['profileData'] = {
            'ParentName':pName,
            'ChildName':cName,
            'childAge':age, 
            'phone':phone
        }
        
        evt = {'d': [evt]}
        usr = {'d': [usr]}
        

        headers = {
            'X-CleverTap-Account-Id': '86K-4KR-WR6Z',
            'X-CleverTap-Passcode': 'SMM-AWC-YWUL',
            'Content-Type': 'application/json; charset=utf-8',
        }
        
        usr = str(usr).encode(encoding='utf-8')
        response1 = requests.post(
            'https://api.clevertap.com/1/upload', headers=headers, data=usr)
        
        evt = str(evt).encode(encoding='utf-8')
        response2 = requests.post(
            'https://api.clevertap.com/1/upload', headers=headers, data=evt)
        print(usr, evt)
        x.append({'number':len(x)//2, 'user':response1.json()})
        x.append({'number':len(x)//2, 'event':response2.json()})
    return f'{x}'
    

if __name__ == '__main__':
    app.debug = True
    app.run()


