import webapp2

from envs import JINJA_ENVIRONMENT


class IndexView(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))
