import sqlite3
from django.shortcuts import render, redirect, reverse
from ..connection import Connection  

def home_page(request):
    if request.method == 'GET':
        template= 'home.html'
        context = {}

        return render(request, template, context)