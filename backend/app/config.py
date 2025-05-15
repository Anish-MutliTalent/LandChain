import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POLYGON_RPC_URL = os.environ.get('POLYGON_RPC_URL')
    NFT_LAND_CONTRACT_ADDRESS = os.environ.get('NFT_LAND_CONTRACT_ADDRESS')
    NFT_LAND_CONTRACT_ABI_PATH = "NFTLand.json"
    ACTION_LOGGER_CONTRACT_ADDRESS = os.environ.get('ACTION_LOGGER_CONTRACT_ADDRESS')
    ACTION_LOGGER_CONTRACT_ABI_PATH = "ActionLogger.json"
    NFT_MARKETPLACE_CONTRACT_ADDRESS = os.environ.get('NFT_MARKETPLACE_CONTRACT_ADDRESS')
    NFT_MARKETPLACE_CONTRACT_ABI_PATH = "NFTMarketplace.json"

    WEB3AUTH_CLIENT_ID = os.environ.get('WEB3AUTH_CLIENT_ID')
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

    TRANSAK_API_KEY = os.environ.get('TRANSAK_API_KEY')
    TRANSAK_ENVIRONMENT = os.environ.get('TRANSAK_ENVIRONMENT')

    PLATFORM_COMMISSION_WALLET_ADDRESS = os.environ.get('PLATFORM_COMMISSION_WALLET_ADDRESS')
    # This private key is for the backend to potentially sign transactions (e.g., deploying contracts, admin actions).
    # Handle with extreme care. Consider using a hardware wallet or KMS for production.
    PLATFORM_OPERATIONAL_WALLET_PRIVATE_KEY = os.environ.get('PLATFORM_OPERATIONAL_WALLET_PRIVATE_KEY')

    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    ADMIN_PASSWORD_HASH = ""  # Store hashed admin password, set during setup
    ADMIN_SHARED_SECRET_FOR_USERNAME = os.environ.get('ADMIN_SHARED_SECRET_FOR_USERNAME')
    ADMIN_LOGIN_TOKEN_MAX_AGE = 300  # Seconds (5 minutes for a dynamic link)

    # Commission percentage for the marketplace (e.g., 10% = 1000)
    # This should match what's set in the NFTMarketplace contract constructor
    MARKETPLACE_COMMISSION_PERCENTAGE_BPS = 4000  # 10% in Basis Points
