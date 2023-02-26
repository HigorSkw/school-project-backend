from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class ClubView(APIView):
    def post(self, request):
        return Response({'msg' : 'Rota Post de Club'})