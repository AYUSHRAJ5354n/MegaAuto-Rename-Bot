import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26177254")
    API_HASH  = os.environ.get("API_HASH", "4051215e417f1f99357e362c2ed158a8")
    BOT_TOKEN = "806332607:"

    # database config
    DB_NAME = os.environ.get("DB_NAME","AshutoshGoswami24")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://Ayush:AYUSHRA5354N@cluster0.lskh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://envs.sh/i_N.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    # -- FORCE_SUB_CHANNELS = ["BotzPW","AshuSupport","AshutoshGoswami24"] -- # 
    FORCE_SUB_CHANNELS = os.environ.get('FORCE_SUB_CHANNELS', '').split(',')
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002206233283"))
    PORT = int(os.environ.get("PORT", "8080"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
        
    ➻ This Is An Advanced And Yet Powerful Rename Bot.
        
    ➻ Using This Bot You Can Auto Rename Of Your Files.
        
    ➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
        
    ➻ Use /tutorial Command To Know How To Use Me.

    <b>Bot Is Made By @Ayu_bots</b>

    <b><a href='https://github.com/AshutoshGoswami24/Auto-Rename-Bot'>AshutoshGoswami24/Auto-Rename-Bot.git</a></b>
    """
        
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

    Use These Keywords To Setup Custom File Name

    ✓ `[episode]` :- To Replace Episode Number
    ✓ `[quality]` :- To Replace Video Resolution

    <b>➻ Example :</b> <code> /autorename Naruto Shippuden S01[episode] [quality][Dual Audio] @AshutoshGoswami24</code>

    <b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
        
    ABOUT_TXT = f"""<b>🤖 My Name :</b>
    <b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
    <b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
    <b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
    <b>🧑‍💻 Developer :</b> <a href='https://t.me/Ayu_bots'>Ayu</a>
        
    <b>♻️ Bot Made By :</b> Ayu bots"""
        
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
        
    ⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
        
    ⦿ /viewthumb - Use This Command To See Your Thumbnail
    ⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
        
    ⦿ /set_caption - Use This Command To Set Your Caption
    ⦿ /see_caption - Use This Command To See Your Caption
    ⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """<b>\n
    ╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
    ┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
    ┣⪼ ⏳️ Dᴏɴᴇ : {0}%
    ┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
    ┣⪼ ⏰️ Eᴛᴀ: {4}
    ┣⪼ 🥺 joine Plz: @AshutoshGoswami24
    ╰━━━━━━━━━━━━━━━➣ </b>"""
        
        
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
        
    If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
        
    <b>My UPI - PandaWep@ybl</b> """
        
    HELP_TXT = """<b>Hey</b> {}
        
    Joine @AshutoshGoswami24 To Help """
