from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Photo
from .serializers import PhotoSerializer
from .responses import *
from .utils import send_json
from PIL import Image
import os
import datetime


class ReceptPhoto(APIView):
    def get(self, request):
        return HttpResponse("Success")

    def post(self, request):
        file = request.FILES.popitem()
        if not file:
            return send_json(fileDoesNotExists)
        image = file[1][0]
        try:
            binary_image = image.file
            img = Image.open(binary_image)
        except:
            return send_json(imageDoesNotExists)

        num = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        abspath = os.path.abspath("./photos/test{}.jpg".format(num))
        try:
            img.save(
                abspath,
                "JPEG",
            )
        except:
            return send_json(saveFailed)
        return send_json(saveSucceed)
