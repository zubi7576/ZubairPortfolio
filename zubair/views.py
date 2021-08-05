from django.shortcuts import render
from zubair.models import Contact

def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services/index.html')
def process(request):
    return render(request,'process/index.html')
def about(request):
    return render(request,'about/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message =request.POST['message']
        ins =Contact(name=name , email=email, message=message )
        ins.save()
        print('data saved')  
    return render(request,'contact/index.html')