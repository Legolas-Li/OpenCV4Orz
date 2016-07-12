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
            binary_threshold = form.cleaned_data['binary_threshold']
            histogram = form.cleaned_data['histogram']
            canny = form.cleaned_data['canny']
            roberts = form.cleaned_data['roberts']
            prewitt = form.cleaned_data['prewitt']
            sobelfilter = form.cleaned_data['sobelfilter']
            gaussian_blur = form.cleaned_data['gaussian_blur']
            median_blur = form.cleaned_data['median_blur']
            dilate = form.cleaned_data['dilate']
            erode = form.cleaned_data['erode']
            open = form.cleaned_data['open']
            close = form.cleaned_data['close']
            otsu = form.cleaned_data['otsu']
            process_todo=[]
            if(greyscale==True):
                process_todo.append("greyscale")
            if(smoothen==True):
                process_todo.append("smoothen")
            if(binary_threshold==True):
                process_todo.append("binary_threshold")
            if(histogram==True):
                process_todo.append("histogram")
            if(roberts==True):
                process_todo.append("roberts")
            if(prewitt==True):
                process_todo.append("prewitt")
            if(canny==True):
                process_todo.append("canny")
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
            if(otsu==True):
                process_todo.append("otsu")
            if process_todo:
                image_url_container = process(request,form, image_file.image_file.name,process_todo)
                return render(request,'polls/showimg.html',{"imageurlcontainer":image_url_container})
            else:
                return HttpResponse("Please select one option")
        else:
            return HttpResponse("Error")
    else:
        form = DocumentForm()
        return render(request,'polls/index.html',{"form":form})


def process(request, form, name=None, process_todo=[]):
    dilate_ksize = form.cleaned_data['dilate_ksize']
    binary_threshold_threshold = form.cleaned_data['binary_threshold_threshold']
    smoothen_kernel_array = form.cleaned_data['smoothen_kernel_array']
    canny_threshold = form.cleaned_data['canny_threshold']
    sobel_ksize = form.cleaned_data['sobel_ksize']
    gaussian_ksize = form.cleaned_data['gaussian_ksize']
    gaussian_sigmaX = form.cleaned_data['gaussian_sigmaX']
    if name==None or len(process_todo)==0:
        return redirect(index)
    else:
        filepath = path.join(settings.MEDIA_ROOT,name)
        if path.isfile(filepath):
            # print process_todo
            imageurlcontainer = []
            for i in process_todo:
                if i=="greyscale":
                    newfilepath = grayscale(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="smoothen":
                    newfilepath = smoothen(filepath,smoothen_kernel_array)
                    imageurlcontainer.append(str(newfilepath))
                if i=="binary_threshold":
                    newfilepath = binary_threshold(filepath,binary_threshold_threshold)
                    imageurlcontainer.append(str(newfilepath))
                if i=="histogram":
                    newfilepath = histogram(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="canny":
                    newfilepath = canny(filepath,canny_threshold)
                    imageurlcontainer.append(str(newfilepath))
                if i=="roberts":
                    newfilepath = roberts(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="prewitt":
                    newfilepath = prewitt(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="sobelfilter":
                    newfilepath = sobelfilter(filepath,sobel_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="gaussian_blur":
                    newfilepath = gaussian_blur(filepath,gaussian_ksize,gaussian_sigmaX)
                    imageurlcontainer.append(str(newfilepath))
                if i=="median_blur":
                    newfilepath = median_blur(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="dilate":
                    newfilepath = dilate(filepath,dilate_ksize)
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
                if i=="otsu":
                    newfilepath = otsu(filepath)
                    imageurlcontainer.append(str(newfilepath))
            imageurlcontainerfinal = []
            print "Process iamge product", imageurlcontainer,imageurlcontainerfinal
            for i in imageurlcontainer:
                imageurlcontainerfinal.append(str(i).split("OpenCV4Orz\\media\\")[1])
            return imageurlcontainerfinal
        else:
            return HttpResponse("Some Error Error Occured")

