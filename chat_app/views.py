from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Chat

# Create your views here.

@csrf_exempt
def chat_view(request):
    if request.method == 'GET':
        chats = list(Chat.objects.values('name', 'message', 'created_at'))
        return JsonResponse(chats, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        new_chat = Chat.objects.create(
            name=data['name'],
            message=data['message']
        )
        return JsonResponse({'status': 'success', 'id': new_chat.id})