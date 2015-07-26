#!/usr/bin/python3
import os, time, praw, gi
from prawoauth2 import PrawOAuth2Mini
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from secrets import app_key, secret_key, refresh_token, access_token

user_agent = 'Python:Orangered Daemon:0.0.4 (by /u/TWILIGHT_IS_AWESOME)'

r = praw.Reddit(user_agent=user_agent)

oauthmini = PrawOAuth2Mini(r, app_key=app_key, app_secret=secret_key, access_token=access_token, scopes=['read', 'privatemessages'], refresh_token=refresh_token)

Notify.init("Orangered Daemon 0.0.4")

while True:
	try:
		oauthmini.refresh()
		for msg in r.get_unread():
    		Message = Notify.Notification.new(msg.author.name, msg.body, "dialog-information")
    		Message.show()
#   		msg.mark_as_read()
		time.sleep(30)
	except praw.errors.OAuthInvalidToken:
		oauthmini.refresh()
