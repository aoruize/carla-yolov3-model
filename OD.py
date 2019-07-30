import cv2 as cv
import numpy as np

# set conf, nms thresholds,inp width/height
confThreshold = 0.55
nmsThreshold = 0.40
inpWidth = 416
inpHeight = 416


# load names of classes and turn that into a list
classesFile = "coco.names"
classes = None

with open(classesFile,'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# model configuration
modelConf = 'yolov3.cfg'
modelWeights = 'yolov3.weights'


# function that processes frames 
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIDs = []
    confidences = []
    boxes = []

    # iterate 
    for out in outs:
        for detection in out:
            
            scores = detection [5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confThreshold:
                centerX = int(detection[0] * frameWidth)
                centerY = int(detection[1] * frameHeight)

                width = int(detection[2]* frameWidth)
                height = int(detection[3]*frameHeight )

                left = int(centerX - width/2)
                top = int(centerY - height/2)

                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # create a list of indices
    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

    # iterate through indices to draw bounding boxes around detected objects
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        
        drawPred(classIDs[i], confidences[i], left, top, left + width, top + height)


# function for drawing bounding boxes around detected objects
def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)
    
    cv.putText(frame, label, (left,top), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)


    # function for getting the names outputted in the output layers of the net
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
   
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# set up the net
net = cv.dnn.readNetFromDarknet(modelConf, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)


# process inputs
winName = 'DL OD with OpenCV'
cv.namedWindow(winName, cv.WINDOW_NORMAL)
cv.resizeWindow(winName, 1000,1000)

# read video input
cap = cv.VideoCapture('Videos/vid2.mp4')

# program loop
while cv.waitKey(1) < 0:

    # get frame from video
    hasFrame, frame = cap.read()

    # create a 4D blob from the frame
    blob = cv.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop = False)

    # set the net
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))

    # 
    postprocess(frame, outs)

    # show the image
    cv.imshow(winName, frame)

















