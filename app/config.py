class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost:3306/chat_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey"
