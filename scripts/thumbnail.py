import os
import re
from PIL import Image

for dir, subdirs, files in os.walk("static/photos"):
    for file in files:
        if not re.search(r"\.(jpe?g|png)$", file.lower()) or re.search(
            r"thumb", file.lower()
        ):
            continue

        fullpath = os.path.join(dir, file)
        print(fullpath)

        a, b = os.path.splitext(fullpath)
        thumbpath = a + ".thumb" + b

        im = Image.open(fullpath)
        im.thumbnail((640, 640))
        im.save(thumbpath)
