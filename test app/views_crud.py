from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import DeleteView

from testapp.models import Movies, Users
from testapp.forms import User

#Regis and add user to DB
def addUser(request):
    context={}

    form=User(request.POST or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.save()
        return HttpResponse("Successfully added!")
    else:
        print("Unable to save. Form is not valid")
        print(form.errors) 
    context['form']= form
    return render(request, "regis.html", context)

#////////// Delete account//////////////
class deleteAccount(DeleteView):
    model=Users
    template_name="delete.html"
    success_url='/'

#///////// Read ////////////////
#// ListView
class Posts_list(ListView):
    model = Movies #model
    fields='__all__' # fields 
    template_name = 'listM.html'
    
#//////// Update //////////////
class updateM(UpdateView):
    model = Movies #model
    fields='__all__'
    template_name = 'update.html' # templete for updating
    success_url="movies/listM" # posts list url