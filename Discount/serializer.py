from rest_framework import serializers

from Discount.models import Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = (
            'ticket',
            'percentage',
            'old_price',
            'discount_price'

        )
        read_only_fieldds = (
            'id',
        )
