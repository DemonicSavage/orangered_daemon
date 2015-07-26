import praw, os, configparser, warnings
from prawoauth2 import PrawOAuth2Server

warnings.filterwarnings('ignore')
config = configparser.ConfigParser()

if not os.path.isfile('orangered.cfg'):
	config['APP'] = {'KEY': '', 'SECRET': ''}
	config['TOKENS'] = {'ACCESS': '', 'REFRESH': ''}

	print('Config file created. Set your app key and secret and re-run this file.')
else:
	user_agent = 'Python:Orangered Daemon:0.0.4 (by /u/TWILIGHT_IS_AWESOME)'

	config.read('orangered.cfg')
	r = praw.Reddit(user_agent=user_agent)

	oauthserver = PrawOAuth2Server(r, app_key=config['APP']['KEY'], app_secret=config['APP']['SECRET'], state=user_agent, scopes=['read', 'privatemessages'])
	oauthserver.start()
	tokens = oauthserver.get_access_codes()

	config['TOKENS']['ACCESS'] = tokens['access_token']
	config['TOKENS']['REFRESH'] = tokens['refresh_token']

with open('orangered.cfg', 'w') as configfile:
	config.write(configfile)