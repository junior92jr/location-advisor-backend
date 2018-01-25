# -*- coding: utf-8 -*-
from rest_framework import serializers

from .constants import VALID_CATEGORY_CHOICES, CATEGORY_INVALID_MESSAGE


class RecomendatiosQuerySerializer(serializers.Serializer):
    """
    Serializer that handle validation for the request parameters
    """

    lat = serializers.FloatField()
    lng = serializers.FloatField()
    category = serializers.CharField(required=False)

    def validate_category(self, value):
        """
        Custome validation for category choices

        :param value: field to be validated

        :return: Return the current value if the validations is success
        """

        if not value in VALID_CATEGORY_CHOICES:
            raise serializers.ValidationError(CATEGORY_INVALID_MESSAGE)

        return value
