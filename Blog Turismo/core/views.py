from django.shortcuts import render

# Create your views here.

def indexView(request):
	return render(request, 'index.html', {} )

#vista contactenos

def vistaContactenos(request):
    return render(request, 'contacto.html', {})

