import getopt
import os
from getpass import getpass

from ig_uploader import InstaUploader
from PIL import Image
import sys

def do_post_to_instagram(username, password, filename, caption):
    fn, ext = os.path.splitext(filename)
    if not ext in [".jpg", ".jpeg", ".png", "bmp"]:
        print "Error: wrong file extension!"
        return False
    with Image.open(filename) as image:
        width, height = image.size

    if width == height:
        processed_image_filename = filename
    else:
        if width > height:
            delta = width - height
            left = int(delta / 2)
            upper = 0
            right = height + left
            lower = height
        else:
            delta = height - width
            left = 0
            upper = int(delta / 2)
            right = width
            lower = width + upper
        image = image.crop(left, upper, right, lower)
        processed_image_filename = "{}-cropped{}".format(fn, ext)
        image.save(processed_image_filename)

    uploader = InstaUploader()
    if uploader.login(username, password):
        media_id = uploader.upload_photo(processed_image_filename)
        if media_id is not None:
            uploader.configure_photo(media_id, caption)

if __name__ == "__main__":
    username = None
    password = None
    image = None
    caption = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:p:i:c:", ["help", "username=", "password=", "image=", "caption="])
    except getopt.GetoptError:
        print "Invalid usage. Use -h for usage."
        sys.exit()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print 'upload_to_instagram.py -u <username> -p <password> -i <image> -c <caption>'
            print '<username> and <image> are mandatory.'
            print 'If <password> is not given, user will be prompted in private.'
            print 'If <caption> is not given, an empty caption will be used.'
            sys.exit()
        elif opt in ('-u', '--username'):
            username = arg
        elif opt in ('-p', '--password'):
            password = arg
        elif opt in ('-i', '--image'):
            image = arg
        elif opt in ('-c', '--caption'):
            caption = arg
    if not username or not image:
        print "Invalid usage, must provide username and image. Use -h for usage."
        sys.exit()
    if not password:
        print "Please enter your password:"
        password = getpass()
    if not caption:
        caption = ""
    do_post_to_instagram(username, password, image, caption)
