#Credits: https://youtu.be/1LCb1PVqzeY

import cv2
import numpy as np

#Load YOLO Algorithm
net=cv2.dnn.readNet("yolov3.weights","yolov3.cfg")

#To load all objects that have to be detected
classes=[]
with open("coco.names","r") as f:
    classes=f.read().splitlines()

#Loading the Video
cap=cv2.VideoCapture(0)

while True:
    #Capture each frames of the video file
    _, img=cap.read()
    #Capturing its height and width used to scale back to original file
    height,width,_=img.shape


    #Extracting features to detect objects
    blob=cv2.dnn.blobFromImage(img,1/255,(416,416),(0,0,0),swapRB=True,crop=False)
                                                            #Inverting blue with red
                                                            #bgr->rgb


    #We need to pass the img_blob to the algorithm
    net.setInput(blob)

    output_layers_names=net.getUnconnectedOutLayersNames()
    layerOutputs=net.forward(output_layers_names)
    
    boxes=[]            #bounding boxes
    confidences=[]      #confidences
    class_ids=[]        #predicted classes

    #Extract all the information form the layers output
    for output in layerOutputs:
        #Extract the information from each of the identifies objects
        for detection in output:
            #Should contain 4 bounding boxes, or 85 parameters
            scores=detection[5:]            #First 4 parameners are the locations and 5th element is confidence
            #Get index having maximum scores
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            #if confidence is strong enough, we start getting locations of those bounding boxes
            if confidence>0.5:
                center_x=int(detection[0]*width)
                center_y=int(detection[1]*height)
                w=int(detection[2]*width)
                h=int(detection[3]*height)

                x=int(center_x-w/2)
                y=int(center_y-h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)
    #Removes redundant boxes and keeping only boxes with high scores
    indexes=cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    #Font of parameters
    font=cv2.FONT_HERSHEY_PLAIN
    #Colors of bounding boxes
    colors=np.random.uniform(0, 255, size=(len(boxes), 3))

    #Pass all paramaters to show on the output video
    if len(indexes)>0:
        for i in indexes.flatten():
            x,y,w,h=boxes[i]
            label=str(classes[class_ids[i]])
            confidence=str(round(confidences[i],2))
            color=colors[i]
            cv2.rectangle(img,(x,y),(x+w, y+h),color,2)
            cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)


    cv2.imshow("Output",img)
    key=cv2.waitKey(1)
    if key==27:
        break
    
cap.release()
cv2.destroyAllWindows()
