import django.http
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection


def work_database(request, uid):


    with connection.cursor() as cursor:
        cursor.execute(f"select * from wallet_table")
        rowss = cursor.fetchall()  # получаем все строки
        data = {'text': f"{rowss}, страница {uid}"}



    return render(request,'index.html', context=data)