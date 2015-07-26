import sys
sys.path.insert(0, './handlers/helpers')

from baseHandler import BaseHandler
from jinja import jinja

class HomePageHandler(BaseHandler):
    def get(self):
        self.response.write("Hello Hive Exchange<br>")