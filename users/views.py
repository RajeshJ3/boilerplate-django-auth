from django.shortcuts import render
from rest_framework import response, status, permissions, authentication, viewsets
from users import serializers as users_serializers
from users import models as users_models


class UserViewSet(viewsets.ModelViewSet):
    queryset = users_models.User.objects.filter(is_active=True)
    serializer_class = users_serializers.UserSerializer

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self, *args, **kwargs):
        if self.request.method == "GET":
            return self.queryset
        else:
            return self.queryset.filter(id=self.request.user.id)
    
    def create(self, *args, **kwargs):
        return response.Response({"details": "Method Not Allowed"}, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def destroy(self, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return response.Response({"details": "Method Not Allowed"}, status.HTTP_405_METHOD_NOT_ALLOWED)