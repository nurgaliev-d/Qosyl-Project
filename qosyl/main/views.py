from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def organization_list(request):
    organizations = Organization.objects.all() 
    serializer = OrganizationSerializer(organizations, many=True)
    return Response(serializer.data)

def user_profile_list(request):
    user_profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(user_profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

def current_user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['GET'])
def other_user_profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, user__id=user_id) 
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)