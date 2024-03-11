import cv2 as cv
import numpy as np
import random

# Set the video file format and FourCC code, and the file name
target_format = "avi"
target_fourcc = "XVID"
target_file = "minju_recoder" + "." + target_format

# Open the video stream
video = cv.VideoCapture("rtsp://210.99.70.120:1935/live/cctv001.stream")

# Set recording state, negative image state, and whether to apply negative image
isRecord = False
isNega = False
isNegaOn = False

if video.isOpened() :
    target = cv.VideoWriter()
    fps = video.get(cv.CAP_PROP_FPS)
    if fps > 60 :
        fps = 60
    wait_msec = int(1 / fps * 1000)

    while True :
        # Read frames from the video
        valid, img = video.read()
        # Randomly decide whether to apply negative image
        isNega = random.choice([True, False])
        if isNega == True :
            if isNegaOn : 
                img = 255 - img
        h, w, *_ = img.shape
        is_color = (img.ndim > 2) and (img.shape[2] > 1)
        if isRecord == False : 
            # Display the video frame
            cv.imshow("Video Player", img)
            key = cv.waitKey(wait_msec)
            if key == ord(" ") :
                isRecord = True
                target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)
            elif key == 27 :
                break
            elif key == ord("n") :
                isNegaOn = not isNegaOn

        elif isRecord == True:
            # Add a rectangle to the recording frame
            cv.rectangle(img, (10, 10), (w - 10, h - 10), (0, 0, 255), thickness=2)
            
            target.write(img)
            cv.imshow("Video Player", img)
            key = cv.waitKey(wait_msec)
            if key == ord(" ") :
                target.release()
                isRecord = False
            elif key == 27 :
                break
            elif key == ord("n") :
                isNegaOn = not isNegaOn
            
    
    cv.destroyAllWindows()

