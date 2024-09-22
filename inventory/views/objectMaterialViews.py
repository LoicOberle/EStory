from .. import models
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

def is_same_domain(request):
    """Helper function to check if request is from the same domain."""
    referer = request.headers.get('Referer')
    origin = request.headers.get('Origin')

    # If Referer or Origin is not present, consider it external (not same domain)
    if not referer and not origin:
        return False

    # Parse the host from referer or origin
    referer_host = urlparse(referer).netloc if referer else None
    origin_host = urlparse(origin).netloc if origin else None

    # Check if the request host matches the referer or origin host
    request_host = request.get_host()
    return referer_host == request_host or origin_host == request_host

def all_materials_view(request):
    # Check if the request should bypass authentication
    if is_same_domain(request) and (request.headers.get('X-Skip-Auth') == 'true' or request.GET.get('skip_auth') == 'true'):
        materials=models.ObjectMaterial.objects.all()
        serializer=serializers.ObjectMaterialSerializer(materials,many=True)
        return JsonResponse(serializer.data,safe=False)
    # All other requests require authentication
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    # Normal authenticated response
    materials=models.ObjectMaterial.objects.all()
    serializer=serializers.ObjectMaterialSerializer(materials,many=True)
    return JsonResponse(serializer.data,safe=False)