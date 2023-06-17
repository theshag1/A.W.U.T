from django.urls import path
from .views import Buyticket

urlpatterns = [
    path('', Buyticket.as_view(), name='salom')
]
