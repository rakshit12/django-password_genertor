from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request ,'generator/rakshit.html ')
def password1(request):
    letter=list('abcdefghijklmnopqrstuvwxyz')
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special='!@#$%^&*()'
    number= '1234567890'
    thepassword=''
    if request.GET.get('uppercase'):
        letter.extend(upper)
    if request.GET.get('specialcase'):
        letter.extend(special)
    if request.GET.get('numbers'):
        letter.extend(number)
    length=int(request.GET.get('length'))
    for x in range(length+1):
        thepassword+=random.choice(letter)







    return render(request,'generator/password.html',{'password':thepassword})
def about_us(request):
    return render(request ,'generator/about_us.html ')
