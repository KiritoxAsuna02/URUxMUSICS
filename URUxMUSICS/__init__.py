from URUxMUSICS.core.bot import Anony
from URUxMUSICS.core.dir import dirr
from URUxMUSICS.core.git import git
from URUxMUSICS.core.userbot import Userbot
from URUxMUSICS.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
