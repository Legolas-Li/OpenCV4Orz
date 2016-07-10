from django.http import HttpResponse
from django.shortcuts import render,redirect
from forms import DocumentForm
from models import Document
from os import path
from django.conf import settings
from opencvstuff import *
#foregroundextraction,imagegradient,smoothing





# Create your views here.

def index(request):
	if request.method=="POST":
		form = DocumentForm(request.POST, request.FILES)
		# print 22222,form.is_valid()
		if form.is_valid():
			image_file = Document(image_file = request.FILES['image_file'])
			image_file.save()
			greyscale = form.cleaned_data['greyscale']
			smoothen = form.cleaned_data['smoothen']
			binarythreshold = form.cleaned_data['binarythreshold']
			histogram = form.cleaned_data['histogram']
			edgedetection = form.cleaned_data['edgedetection']			
			sobelfilter = form.cleaned_data['sobelfilter']			
			gaussian_blur = form.cleaned_data['gaussian_blur']
			median_blur = form.cleaned_data['median_blur']
			dilate = form.cleaned_data['dilate']
			erode = form.cleaned_data['erode']
			open = form.cleaned_data['open']
			close = form.cleaned_data['close']
			process_todo=[]
			if(greyscale==True):
				process_todo.append("greyscale")
			if(smoothen==True):
				process_todo.append("smoothen")
			if(binarythreshold==True):
				process_todo.append("binarythreshold")
			if(histogram==True):
				process_todo.append("histogram")
			if(edgedetection==True):
				process_todo.append("edgedetection")
			if(sobelfilter==True):
				process_todo.append("sobelfilter")
			if(gaussian_blur==True):
				process_todo.append("gaussian_blur")
			if(median_blur==True):
				process_todo.append("median_blur")
			if(dilate==True):
				process_todo.append("dilate")
			if(erode==True):
				process_todo.append("erode")
			if(open==True):
				process_todo.append("open")
			if(close==True):
				process_todo.append("close")
			image_url_container = process(request,image_file.image_file.name,process_todo)
			return render(request,'polls/showimg.html',{"imageurlcontainer":image_url_container})
		else:
			return HttpResponse("Error")
	else:
		form = DocumentForm()
		# documents = Document.objects.all()
		# print  111111111,form,
		return render(request,'polls/index.html',{"form":form})





def process(request,name=None,process_todo=[]):
	if name==None or len(process_todo)==0:
		return redirect(index)
	else:
		filepath = path.join(settings.MEDIA_ROOT,name)
		if path.isfile(filepath):
			print process_todo
			imageurlcontainer = []
			for i in process_todo:
				if i=="greyscale":
					newfilepath = grayscale(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="smoothen":
					newfilepath = smoothing(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="binarythreshold":
					newfilepath = binarythreshold(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="histogram":
					newfilepath = histogram(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="edgedetection":
					newfilepath = cannyedge(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="sobelfilter":
					newfilepath = sobelfilter(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="gaussian_blur":
					newfilepath = gaussian_blur(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="median_blur":
					newfilepath = median_blur(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="dilate":
					newfilepath = dilate(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="erode":
					newfilepath = erode(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="open":
					newfilepath = opend(filepath)
					imageurlcontainer.append(str(newfilepath))
				if i=="close":
					newfilepath = closed(filepath)
					imageurlcontainer.append(str(newfilepath))
				imageurlcontainerfinal = []
			print 1111111111111,imageurlcontainer
			for i in imageurlcontainer:
				imageurlcontainerfinal.append(str(i).split("opencv4orz\\media\\")[1])
			return imageurlcontainerfinal
		else:
			return HttpResponse("Some Error Error Occured")

