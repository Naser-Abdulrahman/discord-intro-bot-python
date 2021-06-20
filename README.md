# discord-intro-bot-python
**What you need to get it working:** 
1. Discord Account
2. Specified User ID
3. Python 3.6+
4. Your wanted intro song
5. FFmpeg

**How Setup and Run:**
1. Get Discord Bot Token
    1. Go To https://discord.com/developers/applications
    2. Click on "New Application", name it whatever you want
    3. On the left side of the screen,underneath settings select Bot
    4. Then "Add Bot"
    5. Underneath the username, you should see a hidden token. Click on copy and save it as an Environment Variable called "TOKEN"
    6. On the left side again, select OAuth2
    7. Scroll down until you see scopes, select 'bot'
    8. Then a new div should appear below scopes called BOT PERMISSIONS
    9. Click on Administrator
    10. You should see a link on the bottom of scopes, click copy and paste it in a new tab
    12. Now invite your bot to your desired discord server
2. Go to discord and right-click on the user you want to follow, and select copy ID.
    1. If you don't see Copy ID, go to your discord settings by select the gear
    2. Then Advance underneath "APP SETTINGS"
    3. Enable Developer Mode, now you should see Copy ID when you right-click a user
3.  Save that as an Environment Variable called "MYID"
4. Follow these steps to install FFmpeg https://www.wikihow.com/Install-FFmpeg-on-Windows
5. Save your desired song in the same directory as "intro.mp3"
6. Run `pip install -r requirements.txt` where main.py is located
7. Now execute the bot, and it should follow you/your friend around your server

