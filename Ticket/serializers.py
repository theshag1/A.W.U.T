from rest_framework import serializers

from Ticket.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'Ticket_from',
            'Ticket_to',
            'date',
            'time',
            'tiket_number',
            'bugges',
            'hand_bugges',
            'ball',
            'class_tiket',
        )
        read_only_fields = ('id',)
