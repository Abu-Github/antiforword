# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak <https://github.com/Artis7eeR>
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 SOURCE="https://t.me/jackssmit"
 START_TEXT="Whats up Dude [{}](tg://user?id={})\nIts me antiforword Bot.Need Any → /help To Know What I Can Do \n"
 HELP_TEXT="I Just Remove Tags And Send U Back Any File - Video - Audio - Photo \nAre You Sending Now\n\n`?`\n "
	
