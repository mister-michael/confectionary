import sqlite3
from django.shortcuts import render
from ..connection import Connection

def variety_form(request):
    if request.method ==  'GET':
        template = 'variety/form.html'
        context = {}

        return render(request, template, context)