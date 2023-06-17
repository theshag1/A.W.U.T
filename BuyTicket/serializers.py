from rest_framework import serializers
from .models import BuyTicket


class BuyTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyTicket
        fields = (
            'first_name',
            'last_name',
            'date_of_brith',
            'gander',
            'passport',
            'phone',
            'email',
        )
        read_only_fields = ('id', 'user')
