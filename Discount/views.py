from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from Discount.models import Discount
from Discount.serializer import DiscountSerializer


# Create your views here.

class DiscountApiView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Discount.objects.all()
        serializer = DiscountSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
