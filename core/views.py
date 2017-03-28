from django.shortcuts import render
from core.models import Comment
from themes.models import Theme
from django.contrib.auth.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

import redis
import json

# Create your views here.

@csrf_exempt
def node_api(request):
    try:
        #Get User from sessionid
        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=user_id)

        theme = Theme.objects.filter(id=request.POST.get('theme')).first()

        #Create comment
        Comment.objects.create(user=user, theme=theme, text=request.POST.get('comment'))

        #Once comment has been created post it to the chat channel
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.publish('chat', json.dumps({'user': user.username, 'text': request.POST.get('comment')}))

        return HttpResponse("Everything worked :)")
    except Exception, e:
        return HttpResponseServerError(str(e))
