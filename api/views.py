from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets,authentication
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
from django.db.models import Prefetch
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
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class InventoryObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows objects to be viewed or edited.
    """
    queryset = models.InventoryObject.objects.all()
    serializer_class = serializers.InventoryObjectSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    @extend_schema(
        parameters=[
            OpenApiParameter(
                'get_all',
                description="Get even not viewable objects (require authentication)",
                required=False,
                type=str,  # Use str for query parameters
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        # Custom queryset (e.g., filter based on request parameters)
        get_all_boolean=request.query_params.get('get_all', None)=="true"
        if(not request.user.is_authenticated):                                              #Not authenticated
            custom_queryset = models.InventoryObject.objects.filter(viewable=True)
        elif(len(request.user.groups.all())>0 and not request.user.is_superuser):            #Authenticated,Multi Museum
            if(get_all_boolean):
                custom_queryset = models.InventoryObject.objects.filter(createdBy__groups__in=request.user.groups.all())
            else:
                custom_queryset = models.InventoryObject.objects.filter(viewable=True,createdBy__groups__in=request.user.groups.all())
        else:                                                                                   #Authenticated, Single Museum
            if(get_all_boolean):
                custom_queryset = models.InventoryObject.objects.all()
            else:
                custom_queryset = models.InventoryObject.objects.filter(viewable=True)

  
        newQueryset=[]
        for object in custom_queryset:
            if(get_all_boolean):
               newQueryset.append(models.InventoryObject.objects.prefetch_related("photos").prefetch_related("files").get(id=object.id))
            else:
                newQueryset.append(models.InventoryObject.objects.prefetch_related(Prefetch("photos", queryset=models.ObjectPhoto.objects.filter(viewable=True))).prefetch_related(Prefetch("files", queryset=models.ObjectFile.objects.filter(viewable=True))).get(id=object.id))
          


        serializer = self.get_serializer(newQueryset, many=True)
        # Apply pagination to the queryset
        page = self.paginate_queryset(newQueryset)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        
        # Customize the response if necessary
        return Response(serializer.data)
    @extend_schema(
        parameters=[
            OpenApiParameter(
                'get_all',
                description="Get even not viewable files and photos (require authentication)",
                required=False,
                type=str,  # Use str for query parameters
            ),
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        get_all_boolean=request.query_params.get('get_all', None)=="true"
      

        if(get_all_boolean):
            # Get the object based on the primary key from the URL
            instance = self.get_object()
            instance=models.InventoryObject.objects.prefetch_related("photos").prefetch_related("files").get(id=instance.id)
            if not instance.viewable:
                raise PermissionDenied("You do not have permission to access this object.")
        else:
            # Get the object based on the primary key from the URL
            instance = self.get_object()
            instance=models.InventoryObject.objects.prefetch_related(Prefetch("photos", queryset=models.ObjectPhoto.objects.filter(viewable=True))).prefetch_related(Prefetch("files", queryset=models.ObjectFile.objects.filter(viewable=True))).get(id=instance.id)
            if not instance.viewable:
                raise PermissionDenied("You do not have permission to access this object.")
 

        serializer = self.get_serializer(instance, many=False)
      
        # Customize the response if necessary
        return Response(serializer.data)

class ObjectCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = models.ObjectCategory.objects.all()
    serializer_class = serializers.ObjectCategorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class ObjectMaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows materials to be viewed or edited.
    """
    queryset = models.ObjectMaterial.objects.all()
    serializer_class = serializers.ObjectMaterialSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

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
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rooms to be viewed or edited.
    """
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]  
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

class ObjectPhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = models.ObjectPhoto.objects.all()
    serializer_class = serializers.ObjectPhotoSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    @extend_schema(
        parameters=[
            OpenApiParameter(
                'get_all',
                description="Get even not viewable photos (require authentication)",
                required=False,
                type=str,  # Use str for query parameters
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        get_all_boolean=request.query_params.get('get_all', None)=="true"
        if(not request.user.is_authenticated):                                              #Not authenticated
            custom_queryset = models.ObjectPhoto.objects.filter(viewable=True)
        elif(len(request.user.groups.all())>0 and not request.user.is_superuser):            #Authenticated,Multi Museum
            if(get_all_boolean):
                custom_queryset = models.ObjectPhoto.objects.filter(createdBy__groups__in=request.user.groups.all())
            else:
                custom_queryset = models.ObjectPhoto.objects.filter(viewable=True,createdBy__groups__in=request.user.groups.all())
        else:                                                                                   #Authenticated, Single Museum
            if(get_all_boolean):
                custom_queryset = models.ObjectPhoto.objects.all()
            else:
                custom_queryset = models.ObjectPhoto.objects.filter(viewable=True)
        # Serialize the queryset
        serializer = self.get_serializer(custom_queryset, many=True)
        page = self.paginate_queryset(custom_queryset)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        
        # Customize the response if necessary
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        # Get the object based on the primary key from the URL
        instance = self.get_object()
        if not instance.viewable:
            raise PermissionDenied("You do not have permission to access this photo.")
        # Optionally modify the object or add extra data
        serializer = self.get_serializer(instance)
        
        # Customize the response if necessary
        return Response(serializer.data)

class ObjectFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows files to be viewed or edited.
    """
    queryset = models.ObjectFile.objects.all()
    serializer_class = serializers.ObjectFileSerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
    @extend_schema(
        parameters=[
            OpenApiParameter(
                'get_all',
                description="Get even not viewable files (require authentication)",
                required=False,
                type=str,  # Use str for query parameters
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        get_all_boolean=request.query_params.get('get_all', None)=="true"
        if(not request.user.is_authenticated):                                              #Not authenticated
            custom_queryset = models.ObjectFile.objects.filter(viewable=True)
        elif(len(request.user.groups.all())>0 and not request.user.is_superuser):            #Authenticated,Multi Museum
            if(get_all_boolean):
                custom_queryset = models.ObjectFile.objects.filter(createdBy__groups__in=request.user.groups.all())
            else:
                custom_queryset = models.ObjectFile.objects.filter(viewable=True,createdBy__groups__in=request.user.groups.all())
        else:                                                                                   #Authenticated, Single Museum
            if(get_all_boolean):
                custom_queryset = models.ObjectFile.objects.all()
            else:
                custom_queryset = models.ObjectFile.objects.filter(viewable=True)
        # Serialize the queryset
        serializer = self.get_serializer(custom_queryset, many=True)
        page = self.paginate_queryset(custom_queryset)
        if page is not None:
            return self.get_paginated_response(serializer.data)
        
        # Customize the response if necessary
        return Response(serializer.data)
    def retrieve(self, request, *args, **kwargs):
        # Get the object based on the primary key from the URL
        instance = self.get_object()
        if not instance.viewable:
            raise PermissionDenied("You do not have permission to access this file.")
        # Optionally modify the object or add extra data
        serializer = self.get_serializer(instance)
        
        # Customize the response if necessary
        return Response(serializer.data)

class ChangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows changes to be viewed or edited.
    """
    queryset = models.ChangeHistory.objects.all()
    serializer_class = serializers.ChangeHistorySerializer
    authentication_classes = [authentication.BasicAuthentication,authentication.TokenAuthentication]
    def get_permissions(self):
        # If the request method is GET, allow anyone
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            # For all other methods (POST, PUT, DELETE), restrict to authenticated users
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]