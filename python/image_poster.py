import json
import os

from ig_processor import IG_Processor
from urllib import urlencode, quote_plus


class Image_Poster:
    def __init__(self):
        self.processor = IG_Processor()
        self.agent = self.processor.generate_user_agent()
        self.guid = self.processor.generate_guid()
        self.device_id = "android-" + self.guid
        self.data = ""
        self.sig = ""

    def process_post(self, username, password, filename, caption):

        self.data = '{"device_id":"' + self.device_id
        self.data += '","guid":"' + self.guid + '","username":"' + username + '","password":"' + password
        self.data += '","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}'

        self.sig = self.processor.generate_signature(str(self.data))
        tempdata = quote_plus(self.data)
        self.data = 'signed_body={}.{}&ig_sig_key_version=4'.format(self.sig, tempdata)
        login = self.processor.send_request('accounts/login/', True, self.data, self.agent, False)

        if "Sorry, an error occurred while processing this request" in str(login["response"]):
            raise StandardError("Request failed, there's a chance that this proxy/ip is blocked")
        else:
            if login["code"] != 200:
                raise StandardError("Error logging in - received code {}".format(login["code"]))
            else:
                # Decode the response
                decoded_login_response = str(login["response"])
                if not decoded_login_response:
                    raise StandardError("Could not decode response for login")
                else:
                    # Post the pic!
                    self.data = self.processor.get_post_data(filename)
                    post = self.processor.send_request('media/upload/', True, self.data, self.agent, True)
                    if post["code"] != 200:
                        raise StandardError("Error posting image - code {}".format(post["code"]))
                    else:
                        pass


if __name__ == "__main__":
    ip = Image_Poster()
    ip.process_post('leviparadis123', 'leviiscool1', 'square.jpg', 'TestCaption')
    """print "Agent = " + ip.agent
    print "GuID = " + ip.guid
    print "Device ID = " + ip.device_id
    print "Sig = " + ip.sig"""



