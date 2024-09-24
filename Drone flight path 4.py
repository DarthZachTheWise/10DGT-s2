# source https://github.com/damiafuentes/DJITelloPy
from djitellopy import Tello
import cv2, math, time
from threading import Thread
from sys import exit

keepRecording = False
keepStreaming = False
if keepRecording:
    fileName = input('Enter a videoname: ')
    if fileName == '': fileName = 'Drone Flight Path 3'
    fileName = fileName + '.avi'

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

#Video recording proccesses
def videoRecorder():
    if keepRecording:
        height, width, _ = frame_read.frame.shape
        video = cv2.VideoWriter(fileName, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)
    if keepRecording:
        video.release()

#Streaming proccesses
def streamPlayer():
    while keepStreaming:
        img = frame_read.frame
        cv2.imshow("drone", img)

        #for some random reason this needs to be here. Don't question it
        key = cv2.waitKey(1) & 0xff

#start Streaming and recording threads
stream = Thread(target=streamPlayer)
stream.start()  

recorder = Thread(target=videoRecorder)
recorder.start()
 

#write Tello commands here
padnumber = 0 


def scan_move():
    padnumber = tello.get_mission_pad_id()
    print(padnumber)
    print(padnumber)
    if padnumber == 4:
        tello.land()
        padnumber = 3
        print(padnumber)
        print(padnumber)
        
    else:
        tello.move_forward (61)
    

def scan_turn_clock_move ():
    padnumber = tello.get_mission_pad_id()
    if padnumber == 4:
        tello.land()
        padnumber = 3
        print(padnumber)
        print(padnumber)
        
    else: 
        tello.rotate_clockwise (90)
        tello.move_forward (61)
        tello.rotate_clockwise (90)
    

def scan_turn_auticlock_move ():
    padnumber = tello.get_mission_pad_id()
    print(padnumber)
    print(padnumber)
    if padnumber == 4:
        tello.land()
        padnumber = 3
        print(padnumber)
        print(padnumber)
        
    
    else: 
        tello.rotate_counter_clockwise (90)
        tello.move_forward (61)
        tello.rotate_counter_clockwise (90)
        
    

#flight


tello.takeoff()
scan_move()
scan_move()
scan_move()
scan_turn_clock_move ()


scan_move()
scan_move()
scan_move ()
scan_turn_auticlock_move ()


scan_move()
scan_move()
scan_move()
scan_turn_clock_move()


scan_move()
scan_move()
scan_move()


tello.land()

#Ending Stream and recording
keepRecording = False
keepStreaming = False
abort_loop = False
recorder.join()
stream.join()