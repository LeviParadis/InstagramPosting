from ig_processor import IG_Processor
from urllib import urlencode


class Image_Poster:
    def process_post(self,username,password,filename,caption):
        processor = IG_Processor()
        agent = processor.generate_user_agent()
        guid = processor.generate_guid()
        device_id = "android-" + guid

        #Login
        data = {"device_id": device_id,
                "guid": guid,
                "username": username,
                "password": password,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        print str(data) + '\n'
        sig = processor.generate_signature(str(data))
        print sig + '\n'
        data = 'signed_body=' + sig + '.' + urlencode(data) + '&ig_sig_key_version=4'
        print str(data)


if __name__ == "__main__":
    ip = Image_Poster()
    ip.process_post('testUsername','testPassword','testFilename','TestCaption')



