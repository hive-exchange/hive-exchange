import os
import jinja2
import urllib2
import json

from baseHandler import BaseHandler
from models import User


jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))
    
class GLoginHandler(BaseHandler):
    def post(self):
        token = self.request.get('idtoken')
        url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s"%(token)
        authenticate = urllib2.urlopen(url)
        
        if authenticate.getcode() == 200:
          authData = json.loads(authenticate.read())
          
          if authData['aud'].find("179222842655-bc2ftvbpfnrodt1aoo8l5icmtd63cebh") > -1:
            if alreadyExists("GOOG:%s"%(authData['sub'])):
              self.response.write("Already Exist")
            else:
              user = User(username="GOOG:%s"%(authData['sub']))
              user.email = authData['email']
              if 'given_name' in authData:
                user.firstName = authData['given_name']
              if 'family_name' in authData:
                user.lastName = authData['family_name']
              user.put()
              self.response.write("%s %s"%(user.firstName, user.lastName))
          else:
            self.response.write("Bad login")
        else:
          self.response.write('Bad login')

          
#helpers          
def alreadyExists(username):
  q = User.all()
  q.filter("username =", username)
  exist = False
  for user in q.run():
    print(user.username)
    exist = True
  return exist
