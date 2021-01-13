from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Photo
from .serializers import PhotoSerializer
from PIL import Image
import os
import datetime


class ReceptPhoto(APIView):
    def get(self, request):
        return HttpResponse("Success")

    def post(self, request):
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            file = file[1][0]
            binary_file = file.file
            img = Image.open(binary_file)
            num = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            abspath = os.path.abspath("./photos/test{}.jpg".format(num))
            img.save(
                abspath,
                "JPEG",
            )
            return HttpResponse("file received")
        except:
            return HttpResponse("No Post")
