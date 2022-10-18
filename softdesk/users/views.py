from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import SignupSerializer


from rest_framework.response import Response
from rest_framework import status



class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

class UserList(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'head']


    def get(self, request, format=None):
        users = User.objects.all()
        serializer = SignupSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        self.http_method_names.append("GET")

        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)