from __future__ import unicode_literals

from django.db import models


class Document(models.Model):		
    image_file = models.FileField(upload_to='documents')
    histogram = models.BooleanField(default=False)

    greyscale = models.BooleanField(default=False)
    binary_threshold = models.BooleanField(default=False)
    binary_threshold_threshold = models.IntegerField(max_length=16,default=157)

    smoothen = models.BooleanField(default=False)
    smoothen_kernel_array = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    canny = models.BooleanField(default=False)
    canny_threshold = models.CharField(blank=True, null=True, max_length=100, default=(100,200))

    roberts = models.BooleanField(default=False)
    prewitt = models.BooleanField(default=False)
    sobelfilter = models.BooleanField(default=False)
    sobel_ksize = models.IntegerField(max_length=16,default=5)
    gaussian_blur = models.BooleanField(default=False)
    gaussian_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    gaussian_sigmaX = models.FloatField(max_length=16,default=1.5)
    median_blur = models.BooleanField(default=False)

    dilate = models.BooleanField(default=False)
    dilate_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    erode = models.BooleanField(default=False)
    open = models.BooleanField(default=False)
    close = models.BooleanField(default=False)

    otsu = models.BooleanField(default=False)


    # legolas = models.BooleanField(default=False)
    # legolas_parameter = models.CharField(blank=True, null=True, max_length=100)


    def __unicode__(self):
        return str(self.docfile)

# Create your models here.
