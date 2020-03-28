from adafruit_motorkit import MotorKit
import getch
import time

print("Beginning...\nWelcome to Robert the Robot! Controls are:\nw = forward\ns = back\nd = right\na = left\nb = shoot\nand\nMOST IMPORTANTLY\nf to stop your current action\nx to QUIT THE PROGRAM\nTHIS DOES NOT TURN OFF THE ROBOT\n")

button = getch.getch()
kit = MotorKit()

while button != 'x':
        if button == 'w':
                print("forward")
                kit.motor3.throttle = 1.0
                kit.motor4.throttle = 1.0
        if button == 's':
                print("back")
                kit.motor3.throttle = -1.0
                kit.motor4.throttle = -1.0
        if button == 'a':
                print("left")
                kit.motor3.throttle = 1.0
                kit.motor4.throttle = -0.5
        if button == 'd':
                print("right")
                kit.motor3.throttle = -0.5
                kit.motor4.throttle = 1.0
        if button == 'b':
                print("shooting")
                kit.motor1.throttle = -1.0
                kit.motor2.throttle = 1.0
        if button == 'f':
                print("stopped")
                kit.motor1.throttle = 0.0
                kit.motor2.throttle = 0.0
                kit.motor3.throttle = 0.0
                kit.motor4.throttle = 0.0

        button = getch.getch()
if button == 'x'
        print("done")
