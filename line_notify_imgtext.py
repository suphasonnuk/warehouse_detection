# Massage Sending 
import requests

url = 'https://notify-api.line.me/api/notify'
token = 'gKQejJvAmBhFXDjfcP3W9dEUaWaGsBY7QnKWttgYAKY'  
headers = {
    'Authorization': 'Bearer ' + token
}

msg = {'message': "Working at Yuanter"}
response = requests.post(url, headers=headers, data=msg)
print(response)

#======================================================================

# Image Sending 

import requests

url = 'https://notify-api.line.me/api/notify'
token = 'gKQejJvAmBhFXDjfcP3W9dEUaWaGsBY7QnKWttgYAKY' 
headers = {
    'Authorization': 'Bearer ' + token
}

image_url = './data/img1.jpg'

msg = {'message': "Working at Yuanter"}
files = {'imageFile': open(fr'{image_url}', 'rb')}  

response = requests.post(url, headers=headers, data=msg, files=files)
print(response)