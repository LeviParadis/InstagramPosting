import requests
import random
import hmac
import hashlib
import time


class IG_Processor:
    def send_request(self, url, post, data, userAgent, cookies):
        headers = {
            "User-Agent": userAgent,
            "Follow-Location": True,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        req = {'code': -1, 'response': 'null'}

        if cookies:
            headers["cookie-file"] = "cookies.txt"
        else:
            headers["cookie-jar"] = "cookies.txt"

        if post:
            req = requests.post(
                "https://i.instagram.com/api/v1/{}".format(url),
                data=data,
                headers=headers
            )

        return {'code': req.status_code, 'response': req.content}

    def generate_guid(self):
        return '{}{}-{}-{}-{}-{}-{}'.format(
            format(random.randrange(0,65535),'x'),
            format(random.randrange(0,65535),'x'),
            format(random.randrange(0,65535),'x'),
            format(random.randrange(16384,20479),'x'),
            format(random.randrange(32768,49151),'x'),
            format(random.randrange(0,65535),'x'),
            format(random.randrange(0,65535),'x'),
            format(random.randrange(0,65535),'x')
            )

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

    def generate_signature(self, data):
        return hmac.new('b4a23f5e39b5929e0666ac5de94c89d1618a2916', data, hashlib.sha256).hexdigest()

    def get_post_data(self, filename):
        if not filename:
            raise ValueError("Image may or may not exist")
        now_time = str(time.time())
        now_time = now_time[0:now_time.index(".")]
        data = "{'device_timestamp': '" + now_time + "', 'photo': '@" + filename + "'}"
        return data


if __name__ == "__main__":
    igp = IG_Processor()
    """print "GuID = " + IG_Processor.generate_guid(igp)
    print "User Agent = " + IG_Processor.generate_user_agent(igp)
    print "Signature = " + IG_Processor.generate_signature(igp, "test data")"""
