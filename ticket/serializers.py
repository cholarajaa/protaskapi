from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(required=False)

    def create(self, data):
        if data.get('tag'):
            tag_name = data.get('tag').lower()
            tag, created = models.Tag.objects.get_or_create(
                name=tag_name)
            data['tag'] = tag
        data = super(
            TicketSerializer, self).create(data)
        return data
    
    def update(self, data):
        if data.get('tag'):
            tag_name = data.get('tag').lower()
            tag, created = models.Tag.objects.get_or_create(
                name=tag_name)
            data['tag'] = tag
        data = super(
            TicketSerializer, self).update(data)
        return data
    
    def to_representation(self, instance):
        tag = instance.tag
        data = super(
            TicketSerializer, self).to_representation(instance)
        if tag and data.get('tag'):
            data['tag'] = tag.name
        else:
            data['tag'] = ''            
        return data

    class Meta:
        model = models.Ticket
        fields = '__all__'
