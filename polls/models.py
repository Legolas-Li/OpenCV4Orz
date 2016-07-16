from __future__ import unicode_literals

from django.db import models


class Document(models.Model):
    image_file = models.FileField(upload_to='documents')
    histogram = models.BooleanField(default=False)
    hist_equalize = models.BooleanField(default=False)

    greyscale = models.BooleanField(default=False)
    binary_threshold = models.BooleanField(default=False)
    binary_threshold_threshold = models.IntegerField(default=128)

    smoothen = models.BooleanField(default=False)
    smoothen_kernel_array = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    canny = models.BooleanField(default=False)
    canny_threshold = models.CharField(blank=True, null=True, max_length=100, default=(100,200))

    roberts = models.BooleanField(default=False)
    prewitt = models.BooleanField(default=False)
    sobel = models.BooleanField(default=False)
    sobel_ksize = models.IntegerField(default=5)
    gaussian_blur = models.BooleanField(default=False)
    gaussian_ksize = models.CharField(blank=True, null=True, max_length=100, default=(31,31))
    gaussian_sigmaX = models.FloatField(default=1.5)
    median_blur = models.BooleanField(default=False)
    median_blur_ksize = models.IntegerField(default=5)
    average_blur = models.BooleanField(default=False)
    average_blur_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    dilate_binary = models.BooleanField(default=False)
    dilate_binary_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    erode_binary = models.BooleanField(default=False)
    erode_binary_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    open_binary = models.BooleanField(default=False)
    opend_binary_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    close_binary = models.BooleanField(default=False)
    closed_binary_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    dilate = models.BooleanField(default=False)
    dilate_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    erode = models.BooleanField(default=False)
    erode_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    open = models.BooleanField(default=False)
    opend_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))
    close = models.BooleanField(default=False)
    closed_ksize = models.CharField(blank=True, null=True, max_length=100, default=(5,5))

    otsu = models.BooleanField(default=False)

    shift = models.BooleanField(default=False)
    shift_coords = models.CharField(blank=True, null=True, max_length=100, default=(0,0))

    scale_area = models.BooleanField(default=False)
    scale_area_ratio = models.FloatField(default=1)

    scale_linear = models.BooleanField(default=False)
    scale_linear_ratio = models.FloatField(default=1)

    rotation = models.BooleanField(default=False)
    rotation_degree = models.IntegerField(default=0)


    def __unicode__(self):
        return str(self.docfile)

# Create your models here.
