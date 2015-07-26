import praw, os
from prawoauth2 import PrawOAuth2Server

user_agent = 'Python:Orangered Daemon:0.3 (by /u/TWILIGHT_IS_AWESOME)'

r = praw.Reddit(user_agent=user_agent)

oauthserver = PrawOAuth2Server(r, 'Pm001ivqao366g', '', state=user_agent, scopes=['read', 'privatemessages'])
oauthserver.start()
tokens = oauthserver.get_access_codes()

if os.environ.get('OR_DAEMON_ACCESS') == None or os.environ.get('OR_DAEMON_REFRESH') == None:
	with open("~/.bashrc", "a") as env_file:
		env_file.write("export OR_DAEMON_ACCESS =" + tokens['access_token'])
		env_file.write("export OR_DAEMON_REFRESH =" + tokens['refresh_token'])
		env_file.close()

os.environ['OR_DAEMON_ACCESS'] = tokens['access_token']
os_environ['OR_DAEMON_REFRESH'] = tokens['refresh_token']