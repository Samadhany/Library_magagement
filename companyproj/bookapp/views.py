from sre_parse import State
from django.shortcuts import render, HttpResponseRedirect
from .forms import BookRegistration
from .models import User
# Create your views here.

# This Function Will Add new Item and Show All Items
def add_show(request):
 if request.method == 'POST':
  fm = BookRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['Book_Name']
   em = fm.cleaned_data['title']
   pw = fm.cleaned_data['author']
   qw = fm.cleaned_data['summary']
   rw = fm.cleaned_data['language']
   sw = fm.cleaned_data['total_copies']
   ww = fm.cleaned_data['available_copies']
   
   reg = User(Book_Name=nm, title=em, author=pw, summary=qw, language=rw, total_copies=sw, available_copies=ww)
   reg.save()
   fm = BookRegistration()
 else:
  fm = BookRegistration()
 stud = User.objects.all()
 return render(request, 'bookapp/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
def update_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  fm = BookRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()
 else:
  pi = User.objects.get(pk=id)
  fm = BookRegistration(instance=pi)
 return render(request, 'bookapp/updatestudent.html', {'form':fm})

# This Function will Delete
def delete_data(request, id):
 if request.method == 'POST':
  pi = User.objects.get(pk=id)
  pi.delete()
  return HttpResponseRedirect('/')