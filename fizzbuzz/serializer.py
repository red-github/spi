from rest_framework import serializers


class FizzBuzzSerializer(serializers.Serializer):
    count = serializers.IntegerField()