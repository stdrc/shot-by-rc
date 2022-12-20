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

        im = Image.open(fullpath)
        im.thumbnail((2048, 2048))
        im.save(fullpath)
