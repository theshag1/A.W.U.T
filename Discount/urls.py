from django.urls import path
from .views import DiscountApiView

urlpatterns = [
    path('', DiscountApiView.as_view(), name='discount_ticket'),
]
