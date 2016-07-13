from __future__ import unicode_literals

from django.db import models


class Document(models.Model):		
    image_file = models.FileField(upload_to='documents')
    histogram = models.BooleanField(default=False)

    greyscale = models.BooleanField(default=False)
    binary_threshold = models.BooleanField(default=False)
    binary_threshold_threshold = models.IntegerField(default=157)

    smoothen = models.BooleanField(default=False)
    smoothen_kernel_array = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    canny = models.BooleanField(default=False)
    canny_threshold = models.CharField(blank=True, null=True, max_length=100, default=(100,200))

    roberts = models.BooleanField(default=False)
    prewitt = models.BooleanField(default=False)
    sobelfilter = models.BooleanField(default=False)
    sobel_ksize = models.IntegerField(default=5)
    gaussian_blur = models.BooleanField(default=False)
    gaussian_ksize = models.CharField(blank=True, null=True, max_length=100, default=(31,31))
    gaussian_sigmaX = models.FloatField(default=1.5)
    median_blur = models.BooleanField(default=False)
    median_blur_ksize = models.IntegerField(default=5)
    average_blur = models.BooleanField(default=False)
    average_blur_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    dilate = models.BooleanField(default=False)
    dilate_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    erode = models.BooleanField(default=False)
    erode_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    open = models.BooleanField(default=False)
    opend_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    close = models.BooleanField(default=False)
    closed_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    otsu = models.BooleanField(default=False)


    # legolas = models.BooleanField(default=False)
    # legolas_parameter = models.CharField(blank=True, null=True, max_length=100)


    def __unicode__(self):
        return str(self.docfile)

# Create your models here.
