import pycurl as curl

class IG_Processor:
    def send_request(self, url, post, data, userAgent, cookies):
        ch = curl.Curl()
        ch.setopt(ch.URL, 'https://i.instagram.com/api/v1/'+url)
        ch.setopt(ch.USERAGENT, userAgent)
        ch.setopt(ch.RETURNTRANSFER, True)
        ch.setopt(ch.FOLLOWLOCATION, True)

        if post:
            ch.setopt(ch.POST, True)
            ch.setopt(ch.POSTFIELDS, data)

        if cookies:
            ch.setopt(ch.COOKIEFILE, 'cookies.txt')
        else:
            ch.setopt(ch.COOKIEJAR, 'cookies.txt')

        response = ch.perform()
        http = ch.getinfo(ch.HTTP_CODE)
        ch.close()

        return {'code': http, 'response': response}

    def generate_guid(self):
        random_string = '{}{}-{}-{}-{}-{}-{}'.format(
            format(random.randrange(0,65535),'x')
            format(random.randrange(0,65535),'x')
            format(random.randrange(0,65535),'x')
            format(random.randrange(16384,20479),'x')
            format(random.randrange(32768,49151),'x')
            format(random.randrange(0,65535),'x')
            format(random.randrange(0,65535),'x')
            format(random.randrange(0,65535),'x')
            )
        return random_string

