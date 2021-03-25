from django.shortcuts import render
from django.views import View

try:
	import RPi.GPIO as GPIO
except ImportError:
	import gpiozero as GPIO

def index_view(request):

	GPIO.

	return render(request, "index.html", context={})


class PotDetailView(View):

	def get(self, request, *args, **kwargs):

		context = {
			"pot": pot
		}

		return render(request, "pot_detail.html", context)