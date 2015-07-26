#!/usr/bin/python3
import os, time, praw, gi
from prawoauth2 import PrawOAuth2Mini
gi.require_version('Notify', '0.7')
from gi.repository import Notify

user_agent = 'Python:Orangered Daemon:0.3 (by /u/TWILIGHT_IS_AWESOME)'

r = praw.Reddit(user_agent=user_agent)

access_token = os.getenv('OR_DAEMON_ACCESS')
refresh_token = os.getenv('OR_DAEMON_REFRESH')

oauthmini = PrawOAuth2Mini(r, 'Pm001ivqao366g', '', access_token=access_token, scopes=['read', 'privatemessages'], refresh_token=refresh_token)

Notify.init("Reddit Inbox Checker 0.1")

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

