from .. import models
from .. import serializers
from django.http import JsonResponse

def all_rooms_view(request):
    user_groups = request.user.groups.all()
    if(len(user_groups)>0 and not request.user.is_superuser): #If a user has a group we only get the rooms of the same group, otherwise we get them all
       rooms=models.Room.objects.filter(createdBy__groups__in=user_groups).distinct()
    else:
      rooms=models.Room.objects.all()
  
    
    roomsList=serializers.RoomSerializer(rooms,many=True).data

    return JsonResponse(roomsList,safe=False)