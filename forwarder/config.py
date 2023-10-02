from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5920056094:AAHZszKefA735ozvNTy4BcEqSsqa0ZGhGCc"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001179079755,-1001179079755,-1001436956200,-1001243512272,-1001422314330,-1001785339917,-1001174348293]# List of chat id's to forward messages from.
    TO_CHATS = [-1001856278028]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
