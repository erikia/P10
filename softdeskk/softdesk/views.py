from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

 
from softapi.models import Project
from softapi.serializers import ProjectSerializer
from rest_framework import status

class ProjectAPIView(APIView):
 
    # def get(self,  *args, **kwargs):
    #     queryset = Project.objects.all()
    #     serializer = ProjectSerializer(queryset, many=True)
    #     return Response(serializer.data)


# ______________________________________

    @api_view(['GET'])
    def project_list(request):
        if request.method == 'GET':
            projects = Project.objects.filter(contributors__user=request.user)
            serializer = ProjectSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterUsersView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)