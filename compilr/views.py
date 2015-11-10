from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm


def index(request):

	if request.method == 'POST':
		lang = request.POST['lang']
		source = request.POST['source']
		iinput = request.POST['iinput']
		#val = request.POST
		#val = request.REQUEST["source"] 
	 	return HttpResponse( (lang + source + iinput) )
		# 	# create a form instance and populate it with data from the request:
		# 	form = NameForm(request.POST)
		# 	# check whether it's valid:
		# 	if form.is_valid():
		# 		code =form.cleaned_data['code']
		# 		iinput = form.cleaned_data['iinput']	
		# 		return render(request, 'compilr/index.html', {'form': form ,'nname' : nname } )
	
		# form = NameForm()

	return render(request, 'compilr/index.html')

# Create your views here.