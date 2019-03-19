import requests
# you can get the app_id and app_key in user dashboard
USER_ID = "your_user_id"
USER_KEY = "your user key"
#-------------------------

IMAGE_PATH = "your image path" # add image path from local system
IMAGE_URL = "your image url" # add image url
API_URL = "http://facexapi.com/get_face_vec?face_det=1" # feature vector url
files = {'img': open(IMAGE_PATH, 'rb')}
payload = {"img": IMAGE_URL}
headers = {"user_id": USER_ID ,"user_key": USER_KEY} 
#r = requests.post(url = API_URL,headers = headers,data = payload) # uncomment this line to use url image
r = requests.post(API_URL,headers = headers,files = files) # comment this line to use url image
print r.text # printing response



