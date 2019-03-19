import requests
# you can get the app_id and app_key in user dashboard
USER_ID = "your user id"
USER_KEY = "your user key"
#--------------------------------

# add image path from local system
IMAGE1_PATH = "first image path"
IMAGE2_PATH = "second image path"
#--------------------------------

# add image url
IMAGE1_URL = "first image url"
IMAGE2_URL = "second image url"
#---------------------------------

API_URL = "http://facexapi.com/compare_faces?face_det=1" # face compare url
files = {'img_1': open(IMAGE1_PATH, 'rb'),'img_2': open(IMAGE2_PATH, 'rb')}
payload = {"img_1": IMAGE1_URL,"img_2": IMAGE2_URL}
headers = {"user_id": USER_ID ,"user_key":USER_KEY}
#r = requests.post(url = API_URL,headers = headers,data = payload) # uncomment this line to use url image
r = requests.post(API_URL,headers = headers,files = files) # comment this line to use url image
print r.text # printing response



