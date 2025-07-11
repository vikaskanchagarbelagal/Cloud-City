import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'My_$e(RE+|<eY'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://CloudCity:cloudforbusiness@cluster0.0blrtmz.mongodb.net/Cloud-City-db?retryWrites=true&w=majority'
