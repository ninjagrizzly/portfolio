from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf

def main(request):
	args = {}
	return render_to_response('gallery.html')