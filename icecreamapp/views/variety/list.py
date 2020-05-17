import sqlite3
from django.shortcuts import render, redirect, reverse
from ..connection import Connection  

def variety_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                v.id, 
                v.name, 
                v.country_of_origin 
            FROM icecreamapp_variety v
            ORDER BY Name ASC;
            """)

            flavors = db_cursor.fetchall()

            template = 'home.html'
            context = {
                'flavors': flavors
            }

            return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO icecreamapp_variety
            (
                name, country_of_origin
            )
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['country'])
            )

        return redirect(reverse('icecreamapp:variety_list'))