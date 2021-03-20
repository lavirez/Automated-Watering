import RPi.GPIO as GPIO
import time

channel = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def pump_on(pin):
	GPIO.output(pin, GPIO.HIGH)

def pump_off(pin):
	GPIO.output(pin, GPIO.LOW)

if __name__ = '__main__':
	try:
		pump_on(channel)
		time.sleep(3)
		pump_off(channel)
		time.sleep(5)
		GPIO.cleanup()

	except KeyboardInterrupt:
		GPIO.cleanup()
		pass

		