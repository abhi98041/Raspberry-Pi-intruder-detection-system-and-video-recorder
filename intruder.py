import RPi.GPIO as GPIO
import os
import datetime as dt
from picamera import PiCamera
from signal import pause
import time

#initialize the video
mydir=os.getcwd()
destination = mydir
camera = PiCamera()

def record_video():
    print ("Video Recording")
    filename = os.path.join(destination, dt.datetime.now().strftime('%Y-%m-%d_%H.%M.%S.h264'))
    camera.start_preview()
    camera.start_recording(filename)
    
    time.sleep(3)
    camera.stop_recording()
    camera.stop_preview()
    os.system ('MP4Box -add {} {}.mp4'.format(filename,filename))

    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))
    os.system('omxplayer {}.mp4'.format(filename))


def finish_video():
    camera.stop_recording()
    camera.stop_preview()

def dist_cap():
    GPIO.setmode(GPIO.BCM)
    TRIG = 23
    ECHO = 24
    print ("Distance Measurement In Progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)
    print ("Waiting For Sensor To Settle")
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print ("Distance:",distance,"cm")
    if (distance<=90):
        record_video()
    GPIO.cleanup()
while True:
    dist_cap()