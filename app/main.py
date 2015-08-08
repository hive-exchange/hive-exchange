from __future__ import with_statement
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import urlfetch
import webapp2
import os
import datetime
import cgi
import uuid
import json


import routes

session_config = {}
session_config['webapp2_extras.sessions'] = {
    'secret_key': os.urandom(24),
    'backends': {'datastore': 'webapp2_extras.appengine.sessions_ndb.DatastoreSessionFactory',
                 'memcache': 'webapp2_extras.appengine.sessions_memcache.MemcacheSessionFactory',
                 'securecookie': 'webapp2_extras.sessions.SecureCookieSessionFactory'}
}

application = webapp2.WSGIApplication([
    ('/', routes.HomePageHandler),
    ('/flogin', routes.FLoginHandler),
    ('/glogin', routes.GLoginHandler)
], debug=True, config=session_config)
