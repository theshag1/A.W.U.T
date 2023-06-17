from django.urls import path
from .views import TicketApi , TicketDetail

urlpatterns = [
    path('', TicketApi.as_view(), name='ticket'),
    path('<int:pk>', TicketDetail.as_view(), name='ticket-detail'),
]
