import cv2
import numpy as np
from matplotlib import pyplot as plt
from os import path

def grayscale(image):
    img = cv2.imread(image,0)
    imagename = str(image).split(".")[0]+"_grayscale_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,img)
    return imagename

def smoothen(image,smoothen_kernel_array):
    img = cv2.imread(image)
    kernel = np.ones(eval(smoothen_kernel_array),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    imagename = str(image).split(".")[0]+"_smoothing_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,dst)
    return imagename

def binary_threshold(image,binary_threshold_threshold):
    img = cv2.imread(image,0)
    ret,thresh1 = cv2.threshold(img,binary_threshold_threshold,255,cv2.THRESH_BINARY)
    imagename = str(image).split(".")[0]+"_binary_thresholding_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,thresh1)
    return imagename

# def histogram(image):
#   img = cv2.imread(image)
#   hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#   hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#   imagename = str(image).split(".")[0]+"_histogram_processed."+str(image).split(".")[-1]
#   cv2.imwrite(imagename,hist)
#   return imagename

def histogram(image):
    img = cv2.imread(image)
    h = np.zeros((256, 256, 3))
    bins = np.arange(256).reshape(256, 1)
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for ch, col in enumerate(color):
        originHist = cv2.calcHist([img], [ch], None, [256], [0, 256])
        cv2.normalize(originHist, originHist, 0, 255 * 0.9, cv2.NORM_MINMAX)
        hist = np.int32(np.around(originHist))
        pts = np.column_stack((bins, hist))
        cv2.polylines(h, [pts], False, col)
    h==np.flipud(h)
    imagename = str(image).split(".")[0]+"_histogram_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,h)
    return imagename



def canny(image,canny_threshold):
    img = cv2.imread(image,0)
    edges = cv2.Canny(img,eval(canny_threshold)[0],eval(canny_threshold)[1])
    imagename = str(image).split(".")[0]+"_canny_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,edges)
    return imagename


def roberts(image):
    img = cv2.imread(image)
    kernel = np.array([[1, 0], [0, -1]])
    roberts = cv2.filter2D(img, -1, kernel)
    imagename = str(image).split(".")[0] + "_roberts_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, roberts)
    return imagename

def prewitt(image):
    img = cv2.imread(image)
    kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt = cv2.filter2D(img, -1, kernel)
    imagename = str(image).split(".")[0] + "_prewitt_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, prewitt)
    return imagename

def sobelfilter(image, sobel_ksize):
    img = cv2.imread(image,0)
    sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=sobel_ksize)
    imagename = str(image).split(".")[0]+"_sobelfilter_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,sobel)
    return imagename

def gaussian_blur(image,gaussian_ksize,gaussian_sigmaX):
    img = cv2.imread(image)
    print "gaussian_ksize,gaussian_sigmaX",gaussian_ksize,gaussian_sigmaX
    gaussian_blur = cv2.GaussianBlur(img, eval(gaussian_ksize),gaussian_sigmaX)
    imagename = str(image).split(".")[0] + "_gaussian_blur_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, gaussian_blur)
    return imagename

def median_blur(image,median_blur_ksize):
    img = cv2.imread(image)
    median_blur = cv2.medianBlur(img, median_blur_ksize)
    imagename = str(image).split(".")[0] + "_median_blur_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, median_blur)
    return imagename


def average_blur(image,average_blur_ksize):
    img = cv2.imread(image)
    average_blur = cv2.blur(img, eval(average_blur_ksize))
    imagename = str(image).split(".")[0] + "_average_blur_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, average_blur)
    return imagename



def dilate(image,dilate_ksize):
    img = cv2.imread(image, 0)
    # kernel = tuple([ tuple(i.split(",")) for i in dilate_ksize.strip("(").strip(")").split(;)])
    # print 1111111111111111111, dilate_ksize,eval(dilate_ksize),type(eval(dilate_ksize))
    x = cv2.getStructuringElement(cv2.MORPH_RECT, eval(dilate_ksize))
    dilate = cv2.dilate(img, x)
    imagename = str(image).split(".")[0] + "_dilate_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, dilate)
    return imagename

def erode(image,erode_ksize):
    img = cv2.imread(image, 0)
    x = cv2.getStructuringElement(cv2.MORPH_RECT, eval(erode_ksize))
    erode = cv2.erode(img, x)
    imagename = str(image).split(".")[0] + "_erode_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, erode)
    return imagename

def opend(image,opend_ksize):
    img = cv2.imread(image, 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, eval(opend_ksize))
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    imagename = str(image).split(".")[0] + "_opend_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, opened)
    return imagename

def closed(image,closed_ksize):
    img = cv2.imread(image, 0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, eval(closed_ksize))
    closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    imagename = str(image).split(".")[0] + "_closed_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, closed)
    return imagename


def otsu(image):
    img = cv2.imread(image)
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, imgBinary = cv2.threshold(imggray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    imagename = str(image).split(".")[0] + "_otsu_processed." + str(image).split(".")[-1]
    cv2.imwrite(imagename, imgBinary)
    return imagename


def foregroundextract(image):
    img = cv2.imread(image)
    mask = np.zeros(img.shape[:2],np.uint8)

    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)


    rect = (50,50,450,290)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    imagename = str(image).split(".")[0]+"_forground_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,img)
    return imagename