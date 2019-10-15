#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

API_TOKEN = '23abf276a984b8c5ea5307f88465eaba'
API_VERSION = 'v8'

def get_time_entries(start_date,end_date):
    # '2013-03-12T15:42:46+02:00'
    try:
        validate_format('datetime',start_date)
    except expression as identifier:
        return 'wrong start_date format'

    try:
        validate_format('datetime',end_date)
    except expression as identifier:
        return 'wrong end_date format'

    params = {
        'start_date': start_date,
        'end_date': end_date
    }
    
    response = requests.get('https://www.toggl.com/api/'+API_VERSION+'/time_entries', params=params, auth=(API_TOKEN, 'api_token'))
    
    return response.json()


def get_projects(start_date,end_date):
    return True

def get_clients():
    return True

def validate_format(data_format,data):
    return True


entries = get_time_entries('2019-07-01T00:00:00+01:00','2019-08-01T00:00:00+01:00')

print 'duronly,wid,uid,stop,start,at,billable,duration,guid,id'
for entry in entries:
    row =''
    #for field in entry:
        #print field['id']
        #row = row+','+field[0]
    print row
    
