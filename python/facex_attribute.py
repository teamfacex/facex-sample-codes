import requests
# you can get the app_id and app_key in user dashboard
USER_ID = "your user id"
USER_KEY = "your user key"
#------------------------------

IMAGE_PATH = "your image path" # add image path from local system
IMAGE_URL = "your image url" # add image url
API_URL = "http://106.51.58.118:5000/get_image_attr?face_det=1" # face attribute url
files = {'image_attr': open(IMAGE_PATH, 'rb')}
payload = {"image_attr": IMAGE_URL}
headers = {"user_id": USER_ID ,"user_key": USER_KEY} 
#r = requests.post(url = API_URL,headers = headers,data = payload) # uncomment this line to use url image
r = requests.post(API_URL,headers = headers,files = files) # comment this line to use url image
print r.text # printing response




