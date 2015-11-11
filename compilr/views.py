from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
import json
import requests


def index(request):

	if request.method == 'POST':
		#lang = request.POST['lang']
		#source = request.POST['source']
		#iinput = request.POST['iinput']
		RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
		CLIENT_SECRET = '496c2cb7d30d44718e6ecf2b096d02f62112667f'
		source = "print int(rawinput())"

		data = {
    	'client_secret': CLIENT_SECRET,
    	'async': 0,
    	'source': source,
    	'input': 8,
    	'lang': "PYTHON",
    	'time_limit': 5,
    	'memory_limit': 262144,
		}

		r = requests.post(RUN_URL, data=data)
		r = json.loads(r)

		#print r.json()
	 	#return HttpResponse( r.json() )
		return HttpResponse(r)
		
	return render(request, 'compilr/index.html')

# Create your views here.