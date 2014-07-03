import webapp2

from core.views import IndexView


application = webapp2.WSGIApplication([
    ('/', IndexView),
], debug=True)
