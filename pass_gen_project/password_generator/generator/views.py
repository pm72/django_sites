from django.http import HttpResponse
from django.shortcuts import render
from random import choice

def home(request):
  return render(request, 'generator/home.html')


def Password(request):
  password = ''
  length = int(request.GET['length'])
  chars = 'abcdefghijklmnopqrstuvwxyz'
  numbers = '1234567890'
  special = '`~!@#$%^&*()_+-=][}{|?><'

  if request.GET.get('uppercase'):
    chars += chars.upper()

  if request.GET.get('numbers'):
    chars += numbers

  if request.GET.get('special'):
    chars += special


  for _ in range(length):
    password += choice(chars)


  return render(request, 'generator/password.html',
                {
                  'password': password
                })


def about(request):
  return render(request, 'generator/about.html')
