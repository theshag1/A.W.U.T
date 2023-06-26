from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from BuyTicket.models import BuyTicket
from BuyTicket.serializers import BuyTicketSerializer
from User.models import User


class Buyticket(APIView):
    def get(self, request, *args, **kwargs):
        queryset = BuyTicket.objects.filter(user=request.user.id)
        serializer = BuyTicketSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BuyTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




