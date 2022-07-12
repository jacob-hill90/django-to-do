from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'to_do_app/index.html')
@csrf_exempt
def addNew(request):
    return render(request, 'to_do_app/add-new.html')
