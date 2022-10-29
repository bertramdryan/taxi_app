from django.contrib.auth import get_user_model

from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from rest_framework_simplejwt.views import TokenBlacklistView

from .serializers import LogInSerializer, TripSerializer, UserSerializer

from .models import Trip


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class LogInView(TokenBlacklistView):
    serializer_class = LogInSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer