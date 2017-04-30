from django.shortcuts import render
from core.models import Comment
from publishings.models import Publishing
from users.models import User

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

from datetime import datetime
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

        publishing = Publishing.objects.filter(id=request.POST.get('publishing')).first()

        #Create comment
        Comment.objects.create(user=user, publishing=publishing, text=request.POST.get('comment'))

        #Once comment has been created post it to the chat channel
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        r.publish('chat', json.dumps({
            'user': user.username,
            'text': request.POST.get('comment'),
            'date': datetime.now().strftime('%b %d, %Y, %I:%M %p')
        }))

        return HttpResponse("Everything worked :)")
    except Exception, e:
        return HttpResponseServerError(str(e))
