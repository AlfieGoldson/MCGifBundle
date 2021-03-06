import sys
from pathlib import Path
from PIL import Image, ImageSequence
import urllib.request as urllib
import io

def getFramesFromGIF(filename):

    print('Loading \'' + filename + '\'...')

    try:
        print('yikes')
        fd = urllib.urlopen(filename)
        print(fd)
        image_file = io.BytesIO(fd.read())
        print(image_file)
        im = Image.open(image_file)
    except Exception as e:
        print(e)
        print ("Cant load", filename)
        sys.exit(1)

    i = 0
    frames = []
    try:
        while 1:

            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im)
            frames.append(background)

            i += 1
            im.seek(im.tell() + 1)


    except EOFError:
        filesize = Path(filename).stat().st_size
        print(str(len(frames)) + ' frames loaded. [' + str(filesize/1000) + 'kB]')
        return frames