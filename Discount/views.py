from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import generics, status

from Discount.models import Discount
from Discount.serializer import DiscountSerializer


# Create your views here.

class DiscountApiView(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('ticket', 'discount_price')
