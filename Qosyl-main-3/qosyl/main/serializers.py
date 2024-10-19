from rest_framework import serializers
from .models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

class UserProfileSerializer(serializers.ModelSerializer):
    subscribed_organizations = OrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'surname', 'email', 'gender', 'interests', 'subscribed_organizations']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'email', 'gender', 'interests']
        # serializers.py

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['content','created_at','publication','author']

class PublicationSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = Publication
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = self.context['request'].build_absolute_uri(instance.image.url)

        # Include the organization details in the response
        representation['organization'] = {
            'id': instance.organization.id,
            'name': instance.organization.name,
            'description': instance.organization.description,
            'members': [member.id for member in instance.organization.members.all()],
            'is_active': instance.organization.is_active,
        }

        return representation
