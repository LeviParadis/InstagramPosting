import logging

import requests
import hmac
import random
import uuid
import urllib
import json
import hashlib
import time

urllib_quote_plus = urllib.quote


class InstaUploader(object):

    def generate_signature(self, data):
        return hmac.new('b4a23f5e39b5929e0666ac5de94c89d1618a2916', data, hashlib.sha256).hexdigest()

    def generate_user_agent(self):
        possible_resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
        possible_versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
        possible_dpis = ['120', '160', '320', '240']

        ua_resolution = random.choice(possible_resolutions)
        ua_version = random.choice(possible_versions)
        ua_dpi = random.choice(possible_dpis)

        return 'Instagram 4.2.0 Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'.format(
            random.randrange(10, 11),
            random.randrange(1, 3),
            random.randrange(3, 5),
            random.randrange(0, 5),
            ua_dpi, ua_resolution, ua_version, ua_version
        )

    def __init__(self):
        self.guid = str(uuid.uuid1())
        self.device_id = 'android-{}'.format(self.guid)
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': self.generate_user_agent()})

    def login(self, username, password):
        data = json.dumps({
            "device_id": self.device_id,
            "guid": self.guid,
            "username": username,
            "password": password,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        })
        signature = self.generate_signature(data)
        payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            signature,
            urllib_quote_plus(data)
        )
        request = self.session.post("https://instagram.com/api/v1/accounts/login/", payload)
        if request.json().get('status') == "ok":
            print "Successfully logged in as {}.".format(username)
            return True
        else:
            print "Error logging in as {}. Check your username and password.".format(username)
            print "If the problem persists, you've probably been banned."
            logging.critical("Error logging in - received status {}!".format(request.json().get('status')))
            return False

    def upload_photo(self, filename):
        data = {
            "device_timestamp": time.time(),
        }
        files = {
            "photo": open(filename, 'rb'),
        }
        request = self.session.post("https://instagram.com/api/v1/media/upload/", data, files=files)
        return request.json().get('media_id')

    def configure_photo(self, media_id, caption):
        data = json.dumps({
            "device_id": self.device_id,
            "guid": self.guid,
            "media_id": media_id,
            "caption": caption,
            "device_timestamp": time.time(),
            "source_type": "5",
            "filter_type": "0",
            "extra": "{}",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        })
        signature = self.generate_signature(data)
        payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            signature,
            urllib_quote_plus(data)
        )
        request = self.session.post("https://instagram.com/api/v1/media/configure/", payload)
        if request.json().get('status') == "ok":
            print "Successfully posted photo!"
            return True
        else:
            print "Error posting photo - check that the file exists and is a square. Status - {}".format(request.json().get('status'))
            logging.critical("Error configuring photo - received response {}!".format(request.json().get('status')))
            return False

if __name__ == "__main__":
    ip = InstaUploader()
    if ip.login('rameezy456', 'leviiscool'):
        media_id = ip.upload_photo("levi.jpg")
        if media_id is not None:
            ip.configure_photo(media_id, "Test Caption")
