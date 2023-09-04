import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

def display(img,cmap='gray'):
  fig = plt.figure(figsize=(12,10))
  ax = fig.add_subplot(111)
  ax.imshow(img, cmap='gray')

img = cv2.imread(r"C:\Users\HP\OneDrive\Desktop\Document Verifier\aadharcard.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
text1 = pytesseract.image_to_data(threshed,output_type='data.frame')
text2 = pytesseract.image_to_string(threshed, lang="eng")
# print(text2)
text = text1[text1.conf != -1]
lines = text.groupby('block_num')['text'].apply(list)
conf = text.groupby(['block_num'])['conf']

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', text.shape[0]+1)

print("lines : \n")
for i in range(len(lines)):
  print("level", i, ": ", lines.iloc[i])

print(lines.iloc[4])

arr=lines.iloc[4]
aadharnumber=""
for i in arr:
  aadharnumber+=i
print("Aadhar number: "+aadharnumber)



# API 

import requests

url = "https://aadhaar-number-verification.p.rapidapi.com/Uidverifywebsvcv1/Uidverify"

payload = {
	"captchaValue": "TK6HXq",
	"captchaTxnId": "58p5MxkQrNFp",
	"method": "uidvalidate",
	"clientid": "111",
	"txn_id": "4545533",
	"consent": "Y",
	"uidnumber": aadharnumber
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "186149b377msh43b3aff606e8d88p143cd7jsn21b7a2af3a65",
	"X-RapidAPI-Host": "aadhaar-number-verification.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

# print(response.json())

# CONVERTING JSON TO STRING 

a=response.json()

result=a["Succeeded"]["Verify_status"]

print (result)