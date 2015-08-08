from google.appengine.ext import db
import datetime
import time


class User(db.Model):
    
    #login data
    username = db.StringProperty(required=True)
    secretKey = db.StringProperty()
    passwordHash = db.StringProperty()
    
    #meta data
    created = db.DateTimeProperty(auto_now_add=True)
    firstName = db.StringProperty()
    lastName = db.StringProperty()
    email = db.StringProperty()
    
    #location data
    country = db.StringProperty()
    state = db.StringProperty()
    city = db.StringProperty()
    neighborhood = db.StringProperty()
    zipCode = db.StringProperty()
    
    #app data
    offers = db.StringListProperty()
    desires = db.StringListProperty()
    currentTrades = db.StringListProperty()