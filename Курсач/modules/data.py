"""
Function get_data_from_URL takes in a URL and parameters
for an API request and then returns the data (json).
"""

import urllib.request
import urllib.parse
import json
import requests


def user_id():
    user_ID = str(input())
    return user_ID

def data_save(user_ID):
    url = "http://open.api.ebay.com/shopping?callname=GetUserProfile&responseencoding=XML&appid=OrestKor-TestTry-PRD-a090b840d-387704b9&siteid=0&version=967&UserID=" + user_ID + "&IncludeSelector=FeedbackDetails,FeedbackHistory"
    r = requests.get(url)
    with urllib.request.urlopen(url) as response:
        # read the response from the response object
        data = response.read()
        # decode it from bytes to string
        data = data.decode("utf-8")
        # parse the string into a python object of dictionaries and lists
        json.loads(data)
    return data


def data_in_file(data):
    """saves data in file"""
    f = open('data.txt', 'w')
    for index in data:
        f.write(index + '\n')
    f.close()
