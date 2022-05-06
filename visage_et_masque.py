import cv2
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import tensorflow as tf
import keras
import os


#Chargement du modèle permettant de détecter le port du masque
modelMasque = keras.models.load_model("./mod.h5")


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

def detection_visage(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    c = 0
    masque = 0
    pas_masque = 0
    for (x, y, w, h) in faces:
                c+=1
                message = 'personne' + str(c)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 0), 2)
                cv2.rectangle(img, (x, y - 20), (x + w, y), (0, 0, 0),-1)
                cv2.putText(img, message,(x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,255,255))
                vis = img [y:y+h, x:x+w]
                capture = cv2.resize(vis, (224, 224))
                capture = capture.reshape((1, capture.shape[0], capture.shape[1], capture.shape[2]))
                predict = modelMasque.predict(capture)
                print(predict)
                avecMasque = predict[0][0]
                pasDeMasque = predict[0][1]
                # Interpretation de la prediction
                if (pasDeMasque > avecMasque):
                    pas_masque+=1
                    # cv2.rectangle(image, (startX, startY), (endX, endY),(0, 0, 255), 2)
                    cv2.putText(vis, "PAS DE MASQUE", (100, 100),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 2)
                else:
                    masque+=1
                    # cv2.rectangle(image, (startX, startY), (endX, endY),(0, 255, 0), 2)
                    cv2.putText(vis, "MASQUE", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 2)

    ts = datetime.datetime.now()
    heure = ts.time()
    date = ts.date()
    df1=pd.DataFrame({'nb_personne': [c], 'avec_masque' : [masque], 'sans_masque' : [pas_masque], 'heure': [heure], 'date' : [date],})
    df1.to_csv("output.csv", mode='a', index=False, header=False) 
    return img,faces 

def main():
    """Face Detection App"""

    st.title("Face Detection App")

    activities = ["Detection","About"]
    choice = st.sidebar.selectbox("Select Activty",activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            # st.write(type(our_image))
            st.image(our_image)

    
        # Face Detection
        if st.button("Process"):
            result_img,result_faces = detection_visage(our_image)
            st.image(result_img)
            st.success("Found {} faces".format(len(result_faces)))


    elif choice == 'About':
        st.subheader("About Face Detection App")
        st.text("fait par Quentin Guichoux")
        st.success("y'a pas grand chose à voir ici, l'autre page est mieux")

    df=pd.read_csv('output.csv')
    st.dataframe(df)


if __name__ == '__main__':
        main()  