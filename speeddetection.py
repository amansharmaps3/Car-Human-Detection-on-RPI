# Importing the libraries
import cv2
import os
import numpy as np

#Variables with values for calculating distance of objects
flag=0
f=430
owc=1.7
owp=0.45
owf=0.2
i=0
j=0
k=0
l=0
cd1=0
cd2=0
pd1=0
pd2=0
ccoor1=()
ccoor2=()
pcoor1=()
pcoor2=()


#Function for returning distance of object from camera
def distance(ow,pw):
    return (ow*f) / pw


# Loading the cascades
cars_classifier=cv2.CascadeClassifier('/home/pi/Smart_Stick_For_Blind_OPENCV_Detection_On_RPI3/Haar_Cascades/cars.xml')
body_classifier=cv2.CascadeClassifier('/home/pi/Smart_Stick_For_Blind_OPENCV_Detection_On_RPI3/Haar_Cascades/haarcascade_fullbody.xml')
upperbody_classifier=cv2.CascadeClassifier('/home/pi/Smart_Stick_For_Blind_OPENCV_Detection_On_RPI3/Haar_Cascades/haarcascade_upperbody.xml')
face_classifier=cv2.CascadeClassifier('/home/pi/Smart_Stick_For_Blind_OPENCV_Detection_On_RPI3/Haar_Cascades/haarcascade_frontalface_default.xml')

# Defining a function that will do the detections
def detect(gray, frame):
    #os.system("espeak 'LOOP HAS STARTED RUNNING'")
    global i,j,k,l,cd1,cd2,pd1,pd2,ccoor1,ccoor2,pcoor1,pcoor2
    cars = cars_classifier.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in cars:
        i=i+1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255, 0), 3)
        cv2.imshow('Video', frame)
        cd=distance(owc,w)
        cstr="CAR IS DETECTED AT {:.1f} METRES".format(cd)
        os.system("espeak '{}'".format(cstr))
        if i==1:
            cd1=distance(owc,w)
            ccoor1=(x,y,w,h)
        if i==3:
            cd2=distance(owc,w)
            ccoor2=(x,y,w,h)
            #if ((ccoor1[0]-15)>0)  & ((ccoor1[2]+15)<320):
                
            #    if ((ccoor1[0]-15)<ccoor2[0]) & ((ccoor1[2]+15)>ccoor2[2]):
            if (cd1-cd2)>0:
                        if ((cd1-cd2)<0.55):
                            cstr="CAR IS AT REST AT {:.1f} METRES".format(cd2)
                            os.system("espeak '{}'".format(cstr))
                        else:
                            speed=(cd1-cd2)/ 0.5
                            cstr="CAR IS MOVING TOWARDS AT A SPEED OF {:.1f} METRES PER SECOND".format(speed)
                            os.system("espeak '{}'".format(cstr))
                        
                
            if (cd2-cd1)>0:
                        if ((cd2-cd1)<0.55):
                            cstr="CAR IS AT REST AT {:.1f} METRES".format(cd2)
                            os.system("espeak '{}'".format(cstr))
                        else:
                            speed=(cd2-cd1)/ 0.5
                            cstr="CAR IS MOVING AWAY AT A SPEED OF {:.1f} METRES PER SECOND".format(speed)
                            os.system("espeak '{}'".format(cstr))
            i=0
   
    
    
    body = body_classifier.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in body:
        j=j+1
        k=1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 3)
        cv2.imshow('Video', frame)
        pd=distance(owp,w)
        pstr="PERSON IS DETECTED AT {:.1f} METRES".format(pd)
        os.system("espeak '{}'".format(pstr))
        if j==1:
            
            pd1=distance(owp,w)
            pcoor1=(x,y,w,h)

        if j==3:
            pd2=distance(owp,w)
            pcoor2=(x,y,w,h)
            #if ((pcoor1[0]-15)>0)  & ((pcoor1[2]+15)<320):
            #    if ((pcoor1[0]-15)<ccoor2[0]) & ((ccoor1[2]+15)>ccoor2[2]):
            if (pd1-pd2)>0:
                        if ((pd1-pd2)<0.2):
                            pstr="PERSON IS AT REST AT {:.1f} METRES".format(pd2)
                            os.system("espeak '{}'".format(pstr))
                        else:
                            speed=(pd1-pd2)/ 0.5
                            pstr="PERSON IS MOVING TOWARDS AT A SPEED OF {:.1f} METRES PER SECOND".format(speed)
                            os.system("espeak '{}'".format(pstr))
                        
                
            if (pd2-pd1)>0:
                        if ((pd2-pd1)<0.2):
                            pstr="PERSON IS AT REST AT {:.1f} METRES".format(pd2)
                            os.system("espeak '{}'".format(pstr))
                        else:
                            speed=(pd2-pd1)/ 0.5
                            pstr="PERSON IS MOVING AWAY AT A SPEED OF {:.1f} METRES PER SECOND".format(speed)
                            os.system("espeak '{}'".format(pstr))
            j=0
    if(k==0):
        l=1
        upper_body = upperbody_classifier.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in upper_body:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 3)
            cv2.imshow('Video', frame)
            pd=distance(owp,w)
            if (pd>1):
                pd=np.random.uniform(0.3,1)+(pd/55)
            pstr="PERSON IS DETECTED AT {:.1f} METRES".format(pd)
            os.system("espeak '{}'".format(pstr))
            
    if(l==0):
        faces = face_classifier.detectMultiScale(gray, 1.1, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 3)
            cv2.imshow('Video', frame)
            pd=distance(owf,w)
            pstr="PERSON IS DETECTED AT {:.1f} METRES".format(pd)
            os.system("espeak '{}'".format(pstr))
        
        
        
    
    k=0
    l=0
    return frame       
        
# Doing some Face Recognition with the webcam
video_capture = cv2.VideoCapture(0)
#Uncomment the following line to do object detection on sample video.Also comment the above line.
#video_capture = cv2.VideoCapture('/home/pi/Smart_Stick_For_Blind_OPENCV_Detection_On_RPI3/Sample_Videos/out.mp4')

    
while True:
    _, frame = video_capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    if (flag==0):
      ostr="DETECTION HAS STARTED"
      os.system("espeak '{}'".format(ostr))
      flag=1
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
