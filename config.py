import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "18946488"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7661512835 6692613520 7475464684"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
