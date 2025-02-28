import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "26177254")
    API_HASH  = os.environ.get("API_HASH", "4051215e417f1f99357e362c2ed158a8")
    BOT_TOKEN = "8063321607:AAGf79fD3fxwVYVkEwLxiZDxCzWv_BPE8TQ" 

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
