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
        if form.is_valid():
            image_file = Document(image_file = request.FILES['image_file'])
            image_file.save()
            greyscale = form.cleaned_data['greyscale']
            smoothen = form.cleaned_data['smoothen']
            binary_threshold = form.cleaned_data['binary_threshold']
            histogram = form.cleaned_data['histogram']
            hist_equalize = form.cleaned_data['hist_equalize']
            canny = form.cleaned_data['canny']
            roberts = form.cleaned_data['roberts']
            prewitt = form.cleaned_data['prewitt']
            sobel = form.cleaned_data['sobel']
            gaussian_blur = form.cleaned_data['gaussian_blur']
            median_blur = form.cleaned_data['median_blur']
            average_blur = form.cleaned_data['average_blur']
            dilate_binary = form.cleaned_data['dilate_binary']
            erode_binary = form.cleaned_data['erode_binary']
            open_binary = form.cleaned_data['open_binary']
            close_binary = form.cleaned_data['close_binary']
            dilate = form.cleaned_data['dilate']
            erode = form.cleaned_data['erode']
            open = form.cleaned_data['open']
            close = form.cleaned_data['close']
            otsu = form.cleaned_data['otsu']
            shift = form.cleaned_data['shift']
            scale_area = form.cleaned_data['scale_area']
            scale_linear = form.cleaned_data['scale_linear']
            rotation = form.cleaned_data['rotation']
            process_todo=[]
            if(greyscale==True):
                process_todo.append("greyscale")
            if(smoothen==True):
                process_todo.append("smoothen")
            if(binary_threshold==True):
                process_todo.append("binary_threshold")
            if(histogram==True):
                process_todo.append("histogram")
            if(hist_equalize==True):
                process_todo.append("hist_equalize")
            if(roberts==True):
                process_todo.append("roberts")
            if(prewitt==True):
                process_todo.append("prewitt")
            if(canny==True):
                process_todo.append("canny")
            if(sobel==True):
                process_todo.append("sobel")
            if(gaussian_blur==True):
                process_todo.append("gaussian_blur")
            if(median_blur==True):
                process_todo.append("median_blur")
            if(average_blur==True):
                process_todo.append("average_blur")
            if(dilate_binary==True):
                process_todo.append("dilate_binary")
            if(erode_binary==True):
                process_todo.append("erode_binary")
            if(open_binary==True):
                process_todo.append("open_binary")
            if(close_binary==True):
                process_todo.append("close_binary")
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
            if(shift==True):
                process_todo.append("shift")
            if(scale_area==True):
                process_todo.append("scale_area")
            if(scale_linear==True):
                process_todo.append("scale_linear")
            if(rotation==True):
                process_todo.append("rotation")
            if process_todo:
                image_url_container = process(request,form, image_file.image_file.name, process_todo)
                return render(request,'polls/showimg.html',{"imageurlcontainer":image_url_container})
            else:
                return HttpResponse("Please select one option")
        else:
            return HttpResponse("Error")
    else:
        form = DocumentForm()
        return render(request,'polls/index.html',{"form":form})

def process(request, form, name=None, process_todo=[]):

    binary_threshold_threshold = form.cleaned_data['binary_threshold_threshold']
    smoothen_kernel_array = form.cleaned_data['smoothen_kernel_array']
    canny_threshold = form.cleaned_data['canny_threshold']
    sobel_ksize = form.cleaned_data['sobel_ksize']
    gaussian_ksize = form.cleaned_data['gaussian_ksize']
    gaussian_sigmaX = form.cleaned_data['gaussian_sigmaX']
    median_blur_ksize = form.cleaned_data['median_blur_ksize']
    average_blur_ksize = form.cleaned_data['average_blur_ksize']
    dilate_binary_ksize = form.cleaned_data['dilate_binary_ksize']
    erode_binary_ksize = form.cleaned_data['erode_binary_ksize']
    opend_binary_ksize = form.cleaned_data['opend_binary_ksize']
    closed_binary_ksize = form.cleaned_data['closed_binary_ksize']
    dilate_ksize = form.cleaned_data['dilate_ksize']
    print 2222222,dilate_ksize
    erode_ksize = form.cleaned_data['erode_ksize']
    opend_ksize = form.cleaned_data['opend_ksize']
    closed_ksize = form.cleaned_data['closed_ksize']
    print 333333333,closed_ksize
    shift_coords = form.cleaned_data['shift_coords']
    scale_area_ratio = form.cleaned_data['scale_area_ratio']
    scale_linear_ratio = form.cleaned_data['scale_linear_ratio']
    rotation_degree = form.cleaned_data['rotation_degree']
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
                if i=="hist_equalize":
                    newfilepath = hist_equalize(filepath)
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
                if i=="sobel":
                    newfilepath = sobel(filepath,sobel_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="gaussian_blur":
                    newfilepath = gaussian_blur(filepath,gaussian_ksize,gaussian_sigmaX)
                    imageurlcontainer.append(str(newfilepath))
                if i=="median_blur":
                    newfilepath = median_blur(filepath,median_blur_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="average_blur":
                    newfilepath = average_blur(filepath,average_blur_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="dilate_binary":
                    newfilepath = dilate_binary(filepath,dilate_binary_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="erode_binary":
                    newfilepath = erode_binary(filepath,erode_binary_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="open_binary":
                    newfilepath = opend_binary(filepath,opend_binary_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="close_binary":
                    newfilepath = closed_binary(filepath,closed_binary_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="dilate":
                    newfilepath = dilate(filepath,dilate_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="erode":
                    newfilepath = erode(filepath,erode_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="open":
                    newfilepath = opend(filepath,opend_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="close":
                    newfilepath = closed(filepath,closed_ksize)
                    imageurlcontainer.append(str(newfilepath))
                if i=="otsu":
                    newfilepath = otsu(filepath)
                    imageurlcontainer.append(str(newfilepath))
                if i=="shift":
                    newfilepath = shift(filepath,shift_coords)
                    imageurlcontainer.append(str(newfilepath))
                if i=="scale_area":
                    newfilepath = scale_area(filepath,scale_area_ratio)
                    imageurlcontainer.append(str(newfilepath))
                if i=="scale_linear":
                    newfilepath = scale_linear(filepath,scale_linear_ratio)
                    imageurlcontainer.append(str(newfilepath))
                if i=="rotation":
                    newfilepath = rotation(filepath,rotation_degree)
                    imageurlcontainer.append(str(newfilepath))
            imageurlcontainerfinal = []
            print "Process iamge product", imageurlcontainer,imageurlcontainerfinal
            for i in imageurlcontainer:
                imageurlcontainerfinal.append(str(i).split("OpenCV4Orz\\media\\")[1])
            return imageurlcontainerfinal
        else:
            return HttpResponse("Some Error Error Occured")
