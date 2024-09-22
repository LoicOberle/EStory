
from .. import serializers
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

def all_groups_view(request):
    groups=Group.objects.all().values()
    groupList=serializers.GroupSerializer(groups,many=True).data
    return JsonResponse(groupList,safe=False)
 