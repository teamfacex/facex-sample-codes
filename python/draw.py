import requests
import json
from PIL import Image, ImageDraw
from io import BytesIO
# you can get the user_id  in user dashboard
USER_ID = "your_user_id"
#------------------------------
IMAGE_URL = "https://www.whoa.in/20150417-Whoa/Leonardo-Dicaprio-Face-Closeup-HD-Wallpaper.jpg" # add image url
API_URL = "http://facexapi.com/get_image_attr?face_det=1" # face attribute url
response = requests.get(IMAGE_URL)
image = Image.open(BytesIO(response.content))
draw = ImageDraw.Draw(image)

payload = {"image_attr": IMAGE_URL}
headers = {"user_id": USER_ID , "Content-Type":"application/json"} 
r = requests.post(url = API_URL,headers = headers,data = json.dumps(payload)) # uncomment this line to use url image

json_resp=json.loads(r.text)
for key, value in json_resp['data']['attributes'].items():
    if 'face_id' in key:
        data=json_resp['data']['attributes'][key]['landmarks']['faceLandMark']
        jawline=[]
        lefteyebrow=[]
        righteyebrow=[]
        nose_a=[]
        nose_b=[]
        left_eye=[]
        right_eye=[]
        mouth_a=[]
        mouth_b=[]
        
        lefteyebrow.append((data['leftEyebrowLeftCorner']['x'],data['leftEyebrowLeftCorner']['y']))
        lefteyebrow.append((data['leftEyebrowMiddle3']['x'],data['leftEyebrowMiddle3']['y']))
        lefteyebrow.append((data['leftEyebrowMiddle2']['x'],data['leftEyebrowMiddle2']['y']))
        lefteyebrow.append((data['leftEyebrowMiddle1']['x'],data['leftEyebrowMiddle1']['y']))
        lefteyebrow.append((data['leftEyebrowRightCorner']['x'],data['leftEyebrowRightCorner']['y']))

        righteyebrow.append((data['rightEyebrowLeftCorner']['x'],data['rightEyebrowLeftCorner']['y']))
        righteyebrow.append((data['rightEyebrowMiddle3']['x'],data['rightEyebrowMiddle3']['y']))
        righteyebrow.append((data['rightEyebrowMiddle2']['x'],data['rightEyebrowMiddle2']['y']))
        righteyebrow.append((data['rightEyebrowMiddle1']['x'],data['rightEyebrowMiddle1']['y']))
        righteyebrow.append((data['rightEyebrowRightCorner']['x'],data['rightEyebrowRightCorner']['y']))   
            
        nose_a.append((data['noseTop1']['x'],data['noseTop1']['y']))
        nose_a.append((data['noseTop2']['x'],data['noseTop2']['y']))
        nose_a.append((data['noseLower1']['x'],data['noseLower1']['y']))
        nose_a.append((data['noseLower2']['x'],data['noseLower2']['y']))
        nose_b.append((data['noseLower2']['x'],data['noseLower2']['y']))
        nose_b.append((data['noseRootLeft']['x'],data['noseRootLeft']['y']))
        nose_b.append((data['nosePoint1']['x'],data['nosePoint1']['y']))
        nose_b.append((data['noseTip']['x'],data['noseTip']['y']))
        nose_b.append((data['nosePoint3']['x'],data['nosePoint3']['y']))
        nose_b.append((data['noseRootRight']['x'],data['noseRootRight']['y']))

        left_eye.append((data['leftEyeLeftCorner']['x'],data['leftEyeLeftCorner']['y']))
        left_eye.append((data['leftEyeTop2']['x'],data['leftEyeTop2']['y']))
        left_eye.append((data['leftEyeTop1']['x'],data['leftEyeTop1']['y']))
        left_eye.append((data['leftEyeRightCorner']['x'],data['leftEyeRightCorner']['y']))
        left_eye.append((data['leftEyeBottom1']['x'],data['leftEyeBottom1']['y']))
        left_eye.append((data['leftEyeBottom2']['x'],data['leftEyeBottom2']['y']))

        right_eye.append((data['rightEyeLeftCorner']['x'],data['rightEyeLeftCorner']['y']))
        right_eye.append((data['rightEyeTop1']['x'],data['rightEyeTop1']['y']))
        right_eye.append((data['rightEyeTop2']['x'],data['rightEyeTop2']['y']))
        right_eye.append((data['rightEyeRightCorner']['x'],data['rightEyeRightCorner']['y']))
        right_eye.append((data['rightEyeBottom1']['x'],data['rightEyeBottom1']['y']))
        right_eye.append((data['rightEyeBottom2']['x'],data['rightEyeBottom2']['y']))

        mouth_a.append((data['mouthLeft']['x'],data['mouthLeft']['y']))
        for i in range (1,6):
            if i==3 or i==4:
                mouth_a.append((data['underLipPoint'+str(i)]['x'],data['underLipPoint'+str(i)]['y']))
            else:
                mouth_a.append((data['upperLipPoint'+str(i)]['x'],data['upperLipPoint'+str(i)]['y']))
            
        mouth_a.append((data['mouthRight']['x'],data['mouthRight']['y']))

        for i in range (4,9):
            mouth_a.append((data['LowerLipPoint'+str(i)]['x'],data['LowerLipPoint'+str(i)]['y']))
        for i in range (6,11):
            if i==7 or i==8:
                mouth_b.append((data['underLipPoint'+str(i)]['x'],data['underLipPoint'+str(i)]['y']))
            else:
                mouth_b.append((data['upperLipPoint'+str(i)]['x'],data['upperLipPoint'+str(i)]['y']))
        for i in range (1,4):
            mouth_b.append((data['LowerLipPoint'+str(i)]['x'],data['LowerLipPoint'+str(i)]['y']))
        
        for i in range(17):
            if(i==8):
               j_point=data['chin']['x'],data['chin']['y']
            else:
                j_point=data['face_endpoint_'+str(i)]['x'],data['face_endpoint_'+str(i)]['y']
            jawline.append(j_point)        

        draw.line(jawline,fill=(0, 0, 255), width=1)
        draw.line(lefteyebrow,fill=(0, 0, 255), width=1)
        draw.line(righteyebrow,fill=(0, 0, 255), width=1)
        draw.line(nose_a,fill=(0, 0, 255), width=1)
        draw.polygon(nose_b,fill=None, outline=(0, 0, 255))
        draw.polygon(left_eye,fill=None, outline=(0, 0, 255))
        draw.polygon(right_eye,fill=None, outline=(0, 0, 255))
        draw.polygon(mouth_a,fill=None, outline=(0, 0, 255))
        draw.polygon(mouth_b,fill=None, outline=(0, 0, 255))
        image.show()
        image.save("image1.png")
