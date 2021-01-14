from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from PIL import Image
from io import BytesIO
import os
import datetime
import boto3


class ReceptPhoto(APIView):

    def get(self, request):
        return HttpResponse("Success")

    def post(self, request):
        s3_client = boto3.client('s3', aws_access_key_id=S3[''], aws_secret_access_key=S3[''])
        try:
            # 여기서 file을 튜플 형태로 client가 보낸 그대로 받아옮.
            file = request.FILES.popitem()
            image = file[1][0]
            binary_image = image.file
            img = Image.open(binary_image)
            num = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            buffer = BytesIO()
            # abspath = os.path.abspath("./photos/test{}.jpg".format(num))
            img.save(buffer, "JPEG",)
            buffer.seek(0)
            s3_client.upload_fileobj(buffer, "poc-mask-on", f"{num}.jpg", ExtraArgs={
                "ContentType": 'image/jpeg'
                }
            )
            return HttpResponse("file received")
        except:
            return HttpResponse("No Post")