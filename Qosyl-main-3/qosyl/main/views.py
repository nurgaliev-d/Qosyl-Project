from urllib import request

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .forms import CommentForm
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404, redirect, render


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


@api_view(['GET'])
def current_user_profile(request):
  user_profile = get_object_or_404(UserProfile, user=request.user)
  serializer = UserProfileSerializer(user_profile)
  return Response(serializer.data)


@api_view(['GET'])
def public_user_profile(request, user_id):
  user_profile = get_object_or_404(UserProfile, user__id=user_id)
  serializer = UserProfileSerializer(user_profile)
  return Response(serializer.data)


@api_view(['GET'])
def other_user_profile(request, user_id):
  user_profile = get_object_or_404(UserProfile, user__id=user_id)
  serializer = UserProfileSerializer(user_profile)
  return Response(serializer.data)


@api_view(['GET'])
def publication_list(request):
  publications = Publication.objects.all()
  serializer = PublicationSerializer(publications, many=True, context={'request': request})
  return Response(serializer.data)


@api_view(['POST'])
def create_publication(request):
  serializer = PublicationSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    comments = Comment.objects.filter(publication=publication)
    comment_form = CommentForm(request.POST)
    if request.method == 'POST':
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.publication = publication
        comment.author = request.user
        comment.save()
    serializer = PublicationSerializer(publication, context={'request': request, 'comments': comments, 'comment_form': comment_form})
    return Response(serializer.data)

@api_view(['GET'])
def get_comments(request, publication):
  comment = Comment.objects.filter(publication=publication)
  serializer = CommentSerializer(comment,many=True, context={'request':request})
  return Response(serializer.data)




@api_view(['GET'])
def get_organization(request,pk):
  organization = get_object_or_404(Organization, pk=pk)
  serializer = OrganizationSerializer(organization)
  return Response(serializer.data)

@api_view(['PUT'])
def update_publication(request, pk):
  publication = get_object_or_404(Publication, pk=pk)
  serializer = PublicationSerializer(publication, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_publication(request, pk):
  publication = get_object_or_404(Publication, pk=pk)
  publication.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_publication(request, pk):
  publication = get_object_or_404(Publication, pk=pk)
  user_profile = request.user.userprofile  # Assuming user has a UserProfile
  if user_profile in publication.likes.all():
    publication.likes.remove(user_profile)
  else:
    publication.likes.add(user_profile)
  publication.save()
  return Response({"status": "success"})
