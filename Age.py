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

img = cv2.imread(r"C:\Users\HP\OneDrive\Desktop\Learning\Minor\Main_Minor\Document Verifier\aadharcard.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
text1 = pytesseract.image_to_data(threshed,output_type='data.frame')
text2 = pytesseract.image_to_string(threshed, lang="eng")
text = text1[text1.conf != -1]
lines = text.groupby('block_num')['text'].apply(list)
conf = text.groupby(['block_num'])['conf']

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', text.shape[0]+1)

arr=lines.iloc[3]

dob=arr[16]
year=dob[len(dob) - 4:]

if 2023-int(year)>=18:
  print("Above 18")
else:
  print("Below 18")
