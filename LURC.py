import RPi.GPIO as GPIO
import time
import signal



OUT_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(OUT_PIN, GPIO.OUT)

# HASAN 
def sony_power_button_mimic():
	# first space is hopefully not needed
	# space(16777215)
	pulse(2427)
	space(555)
	pulse(635)
	space(592)
	pulse(1199)
	space(564)
	pulse(629)
	space(595)
	pulse(1213)
	space(557)
	pulse(626)
	space(594)
	pulse(607)
	space(598)
	pulse(608)
	space(589)
	pulse(608)
	space(592)
	pulse(599)
	space(598)
	pulse(604)
	space(593)
	pulse(1212)
	space(25839)
	pulse(2449)
	space(541)
	pulse(1237)
	space(580)
	pulse(606)
	space(593)
	pulse(1207)
	space(577)
	pulse(608)
	space(593)
	pulse(1207)
	space(587)
	pulse(606)
	space(591)
	pulse(605)
	space(582)
	pulse(614)
	space(593)
	pulse(600)
	space(597)
	pulse(597)
	space(599)
	pulse(604)
	space(594)
	pulse(1214)
	space(25900)
	pulse(2379)
	space(569)
	pulse(1197)
	space(602)
	pulse(583)
	space(599)
	pulse(1213)
	space(551)
	pulse(626)
	space(596)
	pulse(1217)
	space(543)
	pulse(632)
	space(593)
	pulse(605)
	space(590)
	pulse(604)
	space(599)
	pulse(595)
	space(593)
	pulse(615)
	space(588)
	pulse(653)
	space(546)
	pulse(1247)
	pulse(125478)
	
	
	
	
	
def space(micros):
	print("space")
	secs = micros / 1000000
	GPIO.output(OUT_PIN, GPIO.LOW)
	time.sleep(secs)

def pulse(micros):
	print("pulse")
	secs = micros / 1000000
	GPIO.output(OUT_PIN, GPIO.HIGH)
	time.sleep(secs)
	GPIO.output(OUT_PIN, GPIO.LOW)
	
	


def clean_gpio(x,y):
	GPIO.cleanup()
	
signal.signal(signal.SIGINT, clean_gpio)



def hello_world():
	GPIO.output(OUT_PIN, GPIO.HIGH)
	time.sleep(5)
	GPIO.output(OUT_PIN, GPIO.LOW)
# hello_world()

sony_power_button_mimic()


GPIO.cleanup()
