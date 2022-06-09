from django.shortcuts import render, redirect
from . import forms as fm
from . import models as md

# Create your views here.


def store(request):
    booklist = md.Books.objects.all()
    data = {'booklist': booklist}
    return render(request, 'bookstore.html', data)


def viewBook(request,id):
    booklist = md.Books.objects.filter(id=id).first()
    data = {'booklist': booklist}
    return render(request, "bookstore-view.html", {'data': data})

def createBook(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = fm.form_create_book(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('store')
        else:
            form = 'error'
            return render(request, "bookstore-create.html", {'form': form})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = fm.form_create_book()

    return render(request, "bookstore-create.html", {'form': form})

def deleteBook(request,id):
    obj = md.Books.objects.get(id=id)
    obj.delete()
    return redirect('store')

def editBook(request,id):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = fm.form_create_book(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.id = id
            obj.save()
            return redirect('store')
        else:
            form = 'error'
            return render(request, "bookstore-edit.html", {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        obj = md.Books.objects.get(id=id)
        form = fm.form_create_book(instance=obj)

    return render(request, "bookstore-edit.html", {'form': form, 'id':id})
