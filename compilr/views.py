from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm
import json
import requests


def index(request):

	if request.method == 'POST':
		lang = request.POST['lang']
		source = request.POST['source']
		iinput = request.POST['iinput']
		
		RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
		CLIENT_SECRET = '496c2cb7d30d44718e6ecf2b096d02f62112667f'
		#source = "print int(raw_input())"

		data = {
    	'client_secret': CLIENT_SECRET,
    	'async': 0,
    	'source': source,
    	'input': iinput,
    	'lang': lang,
    	'time_limit': 5,
    	'memory_limit': 262144,
		}

		r = requests.post(RUN_URL, data=data).json()
		status = r['run_status']['status']
		ooutput = r['run_status']['output']
		time_used = r['run_status']['time_used']
		status_detail = r['run_status']['status_detail']
		mem_used = r['run_status']['memory_used']
		compile_status = r['compile_status']
		output_box = 1

		

		#print r.json()
	 	#return HttpResponse( r.json() )
		return render(request, 'compilr/index.html', 
			{'status':status, 'ooutput':ooutput, 'time_used':time_used, 'status_detail':status_detail, 'mem_used':mem_used, 'compile_status':compile_status, 'output_box':output_box})
		
	return render(request, 'compilr/index.html')

# Create your views here.