from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,authentication
from inventory import models
from inventory import serializers

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = serializers.GroupSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class InventoryObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows objects to be viewed or edited.
    """
    queryset = models.InventoryObject.objects.all()
    serializer_class = serializers.InventoryObjectSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ObjectCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = models.ObjectCategory.objects.all()
    serializer_class = serializers.ObjectCategorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ObjectMaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows materials to be viewed or edited.
    """
    queryset = models.ObjectMaterial.objects.all()
    serializer_class = serializers.ObjectMaterialSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class OperationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows operations to be viewed or edited.
    """
    queryset = models.OperationHistory.objects.all()
    serializer_class = serializers.OperationHistorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class LoanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows loans to be viewed or edited.
    """
    queryset = models.LoanHistory.objects.all()
    serializer_class = serializers.LoanHistorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ObjectPhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = models.ObjectPhoto.objects.all()
    serializer_class = serializers.ObjectPhotoSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ObjectFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows files to be viewed or edited.
    """
    queryset = models.ObjectFile.objects.all()
    serializer_class = serializers.ObjectFileSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ChangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows changes to be viewed or edited.
    """
    queryset = models.ChangeHistory.objects.all()
    serializer_class = serializers.ChangeHistorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]