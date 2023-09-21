from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class ProductView(APIView):

    def get(self, response):
        return Response('hello world')