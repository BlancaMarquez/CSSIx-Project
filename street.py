from google.appengine.ext import ndb

class Street(ndb.Model):
     email = ndb.StringProperty(required=True)
     password = ndb.StringProperty(required=True)
     repassword = ndb.StringProperty(required=True)
