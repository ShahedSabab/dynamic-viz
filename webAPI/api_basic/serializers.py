from rest_framework import serializers
from .models import wheatCanada

class wheatCanadaSerializers(serializers.ModelSerializer):
    class Meta:
        model = wheatCanada
        fields = '__all__'
        # for accessing specific fields
        # fields = ['year', 'fdc', 'dc', 'fc', 'ah']

# class wheatCanadaSerializers(serializers.Serializer):
#     year = serializers.IntegerField()
#     fdc = serializers.IntegerField()
#     dc = serializers.IntegerField()
#     fc = serializers.IntegerField()
#     ah = serializers.IntegerField()
#
#
#     def create(self, validated_data):
#         return wheatCanada.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.year = validated_data.get('year', instance.year)
#         instance.fdc = validated_data.get('fdc', instance.fdc)
#         instance.dc = validated_data.get('dc', instance.dc)
#         instance.fc = validated_data.get('fc', instance.fc)
#         instance.ah = validated_data.get('ah', instance.ah)
#         instance.save()
#         return instance
