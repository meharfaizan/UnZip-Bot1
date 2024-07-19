import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5442493323:AAHqpxh9_jdSQozCNcHtAhLJR84vOlPAu4U")
    API_ID = int(os.environ.get("API_ID", 6534707))
    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
    
    
