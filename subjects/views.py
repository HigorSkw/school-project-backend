from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class SubjectView(APIView):
    def post(self, request):
        return Response({'msg' : 'Rota Post de Subject'})