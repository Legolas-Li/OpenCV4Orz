from __future__ import unicode_literals

from django.db import models


class Document(models.Model):		
    image_file = models.FileField(upload_to='documents')
    histogram = models.BooleanField(default=False)

    greyscale = models.BooleanField(default=False)
    binarythreshold = models.BooleanField(default=False)

    smoothen = models.BooleanField(default=False)

    edgedetection = models.BooleanField(default=False)
    sobelfilter = models.BooleanField(default=False)
    gaussian_blur = models.BooleanField(default=False)
    median_blur = models.BooleanField(default=False)

    dilate = models.BooleanField(default=False)
    erode = models.BooleanField(default=False)
    open = models.BooleanField(default=False)
    close = models.BooleanField(default=False)


    # legolas = models.BooleanField(default=False)
    # legolas_parameter = models.CharField(blank=True, null=True, max_length=100)


    def __unicode__(self):
        return str(self.docfile)

# Create your models here.
