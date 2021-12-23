from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Movies

def index(request):
    return HttpResponse('Hello!')

#Main page
def mainpage(request):
    return render(request,"Lab2.html")

#Registration page   
def regis(request):
    return render(request,"regis.html")

#Video
def video(request):
    return render(request,"video.html")

#Contacts
def contacts(request):
    return render(request,"contacti.html")

#Voenniye filmi
def vf(request):
    return render(request,"vf.html")

    
#All movies from DB
def movies(request):
    movies1=Movies.objects.raw('select movie_id,movie_name,year,rating, price, genre_name from testapp_movies,testapp_genres where genre_id==genre_id_id')
    data={"Movies":movies1}
    return render(request,"movies.html",data)

#Cartoons
def cartoons(request):
    return render(request,'cartoons.html')

#Search
def results(request):
    if 'results' in request.GET:
        result=request.GET.get('results')
        return render( request,result)
    # inp_value = request.GET.get('results')
    # context = {'inp_value': inp_value}
    #return render( request, 'results/', context)


