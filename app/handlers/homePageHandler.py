import os
import jinja2

from baseHandler import BaseHandler


jinja = jinja2.Environment(autoescape=True,
                        loader=jinja2.FileSystemLoader("./html"))
    


class HomePageHandler(BaseHandler):
    def get(self):
        home = jinja.get_template('index.html')
        self.response.write(home.render())