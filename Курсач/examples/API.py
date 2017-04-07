import urllib.request
import urllib.parse
import json

BASE_URL = "https://maps.googleapis.com/maps/api/elevation/json?"
params = {'locations': "48.5000,23.2703"}


def get_data_from_URL(base_url, options):
    params_str = urllib.parse.urlencode(params)
    request_url = base_url + params_str
    request = urllib.request.Request(request_url)
    with urllib.request.urlopen(request_url) as response:
        # read the response from the response object
        data = response.read()
        # decode it from bytes to string
        data = data.decode("utf-8")
        # parse the string into a python object of dictionaries and lists
        json.loads(data)
    return data

data = get_data_from_URL(BASE_URL, params)

print(data)