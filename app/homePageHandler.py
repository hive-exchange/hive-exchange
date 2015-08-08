import os
import jinja2

from baseHandler import BaseHandler


jinja = jinja2.Environment(autoescape=True,
                           loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__))))
    


class HomePageHandler(BaseHandler):
    def get(self):
        home = jinja.get_template('html/index.html')
        self.response.write(home.render())