import pynstagram
import webapp2

class InstagramPoster(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, InstaPoster!')

    def post(self):
        username = self.request.POST.get("username")
        password = self.request.POST.get("password")
        filename = self.request.POST.get("filename")
        caption = self.request.POST.get("caption")
        if not username or not password or not filename:
            self.response.set_status(500)
            self.response.write("The following fields are required: 'username', 'password', 'filename'")
        else:
            if not caption:
                caption = ""
            try:
                with pynstagram.client(username, password) as client:
                    client.upload(filename, caption)
                    self.response.write("Success!")
            except:
                self.response.set_status(500)
                self.response.write("Something went wrong. Is your file ok?")


app = webapp2.WSGIApplication([
    ('/', InstagramPoster),
], debug=True)
