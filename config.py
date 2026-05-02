# config.py
import os

# API Credentials (TERI INFO DAL)
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER", "")

# Volume Settings (500% BOOST)
MAX_VOLUME = 500  # 0-500 (500 = 5x boost via FFmpeg)
BITRATE = 512000  # 512 kbps
DOWNLOAD_PATH = "downloads/"

# FFmpeg volume filter (actual boost)
FFMPEG_VOLUME_FILTER = "volume=5.0"  # 5.0 = 500%

# Active chat tracking (auto-save)
ACTIVE_CHAT_FILE = "active_chat.txt"
