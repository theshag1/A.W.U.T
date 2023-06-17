from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Ticket.models import Ticket
from .serializers import TicketSerializer
from rest_framework import generics


# Create your views here.


class TicketApi(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Ticket, id=pk)

    def get(self, request, *args, **kwargs):
        serializer = TicketSerializer(self.get_object(self.kwargs.get('pk')))
        return Response(serializer.data, status=status.HTTP_200_OK)
