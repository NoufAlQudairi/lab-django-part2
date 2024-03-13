from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

people = []

class Person:
    def __init__(self,username,password):
        self.username=username
        self.password=password


def index(request):
    return render(request , 'd2/index.html',{'people':people})


def add(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        person=Person(username=username,password=password)
        people.append(person)
    return render(request , 'd2/add.html')
            
