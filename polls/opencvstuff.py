import cv2
import numpy as np
from matplotlib import pyplot as plt
from os import path

def grayscale(image):
    img = cv2.imread(image,0)
    imagename = str(image).split(".")[0]+"_grayscale_processed."+str(image).split(".")[-1]
    cv2.imwrite(imagename,img)
    return imagename

def smoothing(image):
	img = cv2.imread(image)
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	imagename = str(image).split(".")[0]+"_smoothing_processed."+str(image).split(".")[-1]
 	cv2.imwrite(imagename,dst)
 	return imagename

def binarythreshold(image):
	img = cv2.imread(image,0)
	ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
	imagename = str(image).split(".")[0]+"_binarythresholding_processed."+str(image).split(".")[-1]
 	cv2.imwrite(imagename,thresh1)
 	return imagename

def histogram(image):
	img = cv2.imread(image)
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)	
	hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	imagename = str(image).split(".")[0]+"_histogram_processed."+str(image).split(".")[-1]
	cv2.imwrite(imagename,hist)
	return imagename

def cannyedge(image):
	img = cv2.imread(image,0)
	edges = cv2.Canny(img,100,200)
	imagename = str(image).split(".")[0]+"_edge_processed."+str(image).split(".")[-1]
	cv2.imwrite(imagename,edges)
	return imagename

def sobelfilter(image):
	img = cv2.imread(image,0)
	sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
	imagename = str(image).split(".")[0]+"_sobelfilter_processed."+str(image).split(".")[-1]
	cv2.imwrite(imagename,sobel)
	return imagename

def gaussian_blur(image):
	img = cv2.imread(image, 0)
	gaussian_blur = cv2.GaussianBlur(img, (5,5),1.5)
	imagename = str(image).split(".")[0] + "_gaussian_blur_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, gaussian_blur)
	return imagename

def median_blur(image):
	img = cv2.imread(image, 0)
	median_blur = cv2.medianBlur(img, 5)
	imagename = str(image).split(".")[0] + "_median_blur_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, median_blur)
	return imagename

def dilate(image):
	img = cv2.imread(image, 0)
	x = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
	dilate = cv2.dilate(img, x)
	imagename = str(image).split(".")[0] + "_dilate_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, dilate)
	return imagename

def erode(image):
	img = cv2.imread(image, 0)
	x = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
	erode = cv2.erode(img, x)
	imagename = str(image).split(".")[0] + "_erode_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, erode)
	return imagename

def opend(image):
	img = cv2.imread(image, 0)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
	opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
	imagename = str(image).split(".")[0] + "_opend_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, opened)
	return imagename

def closed(image):
	img = cv2.imread(image, 0)
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
	closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	imagename = str(image).split(".")[0] + "_closed_processed." + str(image).split(".")[-1]
	cv2.imwrite(imagename, closed)
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