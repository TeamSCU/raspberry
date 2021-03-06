### Imports ###################################################################

from picamera.array import PiRGBArray
from picamera import PiCamera
import requests
import time
import cv2
import os
import pygame
import json

### Setup #####################################################################

os.putenv( 'SDL_FBDEV', '/dev/fb1' )
url = "https://face.3cat.top/camera/upload"
# Setup the camera
camera = PiCamera()
camera.resolution = ( 320, 240 )
# camera.resolution = (320,240)
camera.framerate = 30
rawCapture = PiRGBArray( camera, size=( 320, 240 ) )

fcounter = 0
facefind = 0

# Load a cascade file for detecting faces
face_cascade = cv2.CascadeClassifier( '1.xml' )

t_start = time.time()
fps = 0

### Main ######################################################################

# Capture frames from the camera
for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):

    image = frame.array

    # Run the face detection algorithm every four frames
    if fcounter == 6:

        fcounter = 0

        # Look for faces in the image using th e loaded cascade file
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
        faces = face_cascade.detectMultiScale( gray )

        print "Found " + str( len( faces ) ) + " face(s)"

        if len( faces )  != 0:
            print str(len(faces))
            filename = time.strftime("%m%d-%H:%M:%s")+".jpg"
            cv2.imwrite(filename,image)
            postfile = {"picture":open("/home/pi/Desktop/"+filename,'rb')}
            r = requests.post(url,data={"camera_id":1},files=postfile)
            print r
        # Draw a rectangle around every face
        #  for ( x, y, w, h ) in faces:
        #     cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 200, 255, 0 ), 2 )
        #     cv2.putText( image, "Face No." + str( len( facess ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )
        #     facess = faces

    # else:
    #     if facefind == 1 and str( len( facess ) ) != 0:

            # Continue to draw the rectangle around every face
    #         for ( x, y, w, h ) in facess:
    #             cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 200, 255, 0 ), 2 )
    #             cv2.putText( image, "Face No." + str( len( facess ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )

    fcounter += 1


    # Calculate and show the FPS
    fps = fps + 1
    sfps = fps / ( time.time() - t_start )
    cv2.putText( image, "FPS : " + str( int( sfps ) ), ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )
    print sfps
    #cv2.imshow( "Frame", image )
    cv2.waitKey( 1 )

    # Clear the stream in preparation for the next frame
    rawCapture.truncate( 0 )
