from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
import pdb

from .models import User, Company, Package, UserRole, UserProfile, Notice
from .serializers import UserSerializer, CompanySerializer, PackageSerializer, UserRoleSerializer, \
    UserProfileSerializer, NoticeSerializer
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(data=serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsAuthenticated]


class UserPermissionsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_data = UserSerializer(user, many=False).data
        profile = UserProfileSerializer(user.profile, many=False).data
        user_data['profile'] = profile
        # role = UserRoleSerializer(user.role, many=False).data
        # return Response({"user": user_data, "profile": profile, "role": role})
        role = user.role.role
        permissions = {
            'can_create_company': user.role.role == 'superadmin',
            'can_create_package': user.role.role == 'superadmin',
            'can_manage_services': user.role.role in ['admin', 'agent']
        }

        response_data = {"user": user_data, "role": role, "permissions": permissions}
        # company = user.role.company
        # if company:
        #     package = company.package
        #     modules = package.modules.all()
        #     module_data = [{"id": module.id, "name": module.name} for module in modules]
        # else:
        module_data = []

        # return Response({
        #     "user": user_data,
        #     "role": role,
        #     # "company": company.id if company else None,
        #     # "modules": module_data,
        #     "permissions": permissions,
        #
        # })

        return Response(response_data)