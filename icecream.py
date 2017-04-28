
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins=[20,12,5,26,19,21,16]

GPIO.setup(pins,GPIO.OUT)
import time
####PRINT THE VALUE OF SENSOR
##while True:
##    vall=GPIO.input(21)
##    print(vall)
##    
##    if vall == 0:
##        GPIO.output(20,GPIO.HIGH)
##        GPIO.output(16,GPIO.LOW)
##    elif vall == 1:
##        GPIO.output(16,GPIO.HIGH)
##        GPIO.output(20,GPIO.LOW)
##        
##g=16 f=21 a=20 e=19 b=12 c=5  d=26

##GPIO.output([20,21,12,16,19,6],GPIO.LOW)
##GPIO.output(26,GPIO.HIGH)
##time.sleep(1)
##GPIO.output([20,21,12,16,19,6],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([26,19,16,21,20],GPIO.LOW)
##GPIO.output([12,6],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([26,19,16,21,20],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([21,19,12,6,16],GPIO.LOW)
##GPIO.output([26,20],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([21,19,12,6,16],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([21,19,12],GPIO.LOW)
##GPIO.output([6,20,26,16],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([21,19,12],GPIO.HIGH)
##time.sleep(1)
##while True:
##    
##    for i in pins:
##        GPIO.output(pins,GPIO.HIGH)
##        GPIO.output(i,GPIO.LOW)
##        time.sleep(0.5)
##g=16 f=21 a=20 e=19 b=12 c=5  d=26
##GPIO.output([20,12,5,26,16],GPIO.LOW)
##GPIO.output([26,21],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([20,12,5,26,16],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([20,12,16,19,26],GPIO.LOW)
##GPIO.output([26,5],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([20,12,16,19,26],GPIO.HIGH)
##time.sleep(1)
##GPIO.output([12,5],GPIO.LOW)
##GPIO.output([16,21,20,19,26],GPIO.HIGH)
##Try/test GPIO.output([20,12,5,26,19,21,16],GPIO.LOW)
##
GPIO.output([20,12,5,26,16],GPIO.LOW)
GPIO.output([21,19],GPIO.HIGH)
time.sleep(1)
GPIO.output([20,12,26,19,16],GPIO.LOW)
GPIO.output([21,5],GPIO.HIGH)
time.sleep(1)
GPIO.output([12,5],GPIO.LOW)
GPIO.output([20,26,19,21,16],GPIO.HIGH)
time.sleep(1)



