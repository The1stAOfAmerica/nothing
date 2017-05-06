
import time
##speed divides by time equals distance
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([21,12],GPIO.OUT)
GPIO.setup(16,GPIO.IN)

temperature=20
speedSound=33100+(0.6*temperature)
while True:
    GPIO.output(21,True)
    # Wait 10us
    time.sleep(0.00001)
    GPIO.output(21,False)
    start = time.time()

    while GPIO.input(16)==0:
        start = time.time()

    while GPIO.input(16)==1:
        stop = time.time()

    #Calculate pulse length
    elasped=stop-start
    #distance pulse travelled in that time is time
    #multiplied by the speed of sound(cm/s)
    distance=elasped*speedSound

    #that was the distance there and back so half the value
    distance=distance/2
    print(distance)
    if distance >= 10:
        GPIO.output(12,GPIO.HIGH)
    else:
        GPIO.output(12,GPIO.LOW)
