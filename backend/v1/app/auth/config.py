import os

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",
                                          60))
ALGORITHM=os.getenv("ALGORITHM", "HS256")
SECRET_KEY=os.getenv("SECRET_KEY", "default secret key")
MAIL_USERNAME=os.getenv("MAIL_USERNAME")
MAIL_PASSWORD=os.getenv("MAIL_PASSWORD")
MAIL_FROM=os.getenv("MAIL_FROM", "no-reply@your-domain.com")
MAIL_PORT=int(os.getenv("MAIL_PORT", 587))
MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.your-email-provider.com")
MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME", "Your App Name")
VERIFICATION_TOKEN_EXPIRE_MINUTES=int(os.getenv("VERIFICATION_TOKEN_EXPIRE_MINUTES",
                                                30))
