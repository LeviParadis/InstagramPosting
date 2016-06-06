from ig_processor import IG_Processor
from urllib import urlencode


class Image_Poster:
    def __init__(self):
        self.processor = IG_Processor()
        self.agent = self.processor.generate_user_agent()
        self.guid = self.processor.generate_guid()
        self.device_id = "android-" + self.guid
        self.data = ""
        self.sig = ""

    def process_post(self, username, password, filename, caption):
        self.data = {
            "device_id": self.device_id,
            "guid": self.guid,
            "username": username,
            "password": password,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        self.sig = self.processor.generate_signature(str(self.data))
        self.data = 'signed_body={}.{}&ig_sig_key_version=4'.format(self.sig, urlencode(self.data))

        login = self.processor.send_request('accounts/login/', True, self.data, self.agent, False)
        print login


if __name__ == "__main__":
    ip = Image_Poster()
    ip.process_post('jimmyjohnson3674', 'leviiscool1', 'square.jpg', 'TestCaption')
    """print "Agent = " + ip.agent
    print "GuID = " + ip.guid
    print "Device ID = " + ip.device_id
    print "Sig = " + ip.sig"""



