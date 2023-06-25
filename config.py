from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "16692889"))
API_HASH = getenv("API_HASH", "ec2d539ea3302fd241553f8c9741362f")
BOT_TOKEN = getenv("BOT_TOKEN", "6095704393:AAGfehlXz0yaLQJ54UxMoPe9zTPziwRTh6g")
SESSION_NAME = getenv("SESSION_NAME", "AgBRytgJNJUwyoWHYevNN26zsKS__xBEIl51SmhY5SNL32zuIPo7J9Gs_crJiBwX3s95SeyuGR5oGG_r_3HS_ZCZlPloSS7gq0wlEI2dmYUJkJfsyh7gndEBbKklrSVRcHOXHchF1RgRuBNJN7V5HQERjXa0d3OKQm98mZY-NSukmJQ0uETsOSJj99ZCD5K6869e9bOP0aUiQqpul5WrvniUMlr6deQc8xVL_LxwFBJVk3MrREyVZXYgwReA-cHZFfUoOHhapY9kKPKqZ8f-OkWWkkqdrWmf7HZ9Mvgh8IhQFSYziHfaiIQYZY3ZEE6PHTbRFEXQUXyfeQkojmgW1DWXAAAAATmGJ0MA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "Z9999B")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Ciii7BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "soos83")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "soos83")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
