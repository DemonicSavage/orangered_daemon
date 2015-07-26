#!/usr/bin/python3
import os, time, praw, gi, configparser, warnings
from prawoauth2 import PrawOAuth2Mini
gi.require_version('Notify', '0.7')
from gi.repository import Notify

config = configparser.ConfigParser()
config.read('orangered.cfg')

user_agent = 'Python:Orangered Daemon:0.0.4 (by /u/TWILIGHT_IS_AWESOME)'

r = praw.Reddit(user_agent=user_agent)

oauthmini = PrawOAuth2Mini(r, app_key=config['APP']['KEY'], app_secret=config['APP']['SECRET'], access_token=config['TOKENS']['ACCESS'], scopes=['read', 'privatemessages'], refresh_token=config['TOKENS']['REFRESH'])

Notify.init("Orangered Daemon 0.0.4")

while True:
	try:
		oauthmini.refresh()
		for msg in r.get_unread():
			Message = Notify.Notification.new(msg.author.name, msg.body, "dialog-information")
			Message.show()
#			msg.mark_as_read()
		time.sleep(30)
	except praw.errors.OAuthInvalidToken:
		oauthmini.refresh()
