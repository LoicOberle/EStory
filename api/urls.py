from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'objects', views.InventoryObjectViewSet)
router.register(r'categories', views.ObjectCategoryViewSet)
router.register(r'materials', views.ObjectMaterialViewSet)
router.register(r'operations', views.OperationViewSet)
router.register(r'loans', views.LoanViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'photos', views.ObjectPhotoViewSet)
router.register(r'files', views.ObjectFileViewSet)
router.register(r'changes', views.ChangeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]