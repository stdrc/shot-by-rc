import os
import re
import sys
from PIL import Image

begin_date = sys.argv[1]

for dir, subdirs, files in os.walk("static/photos"):
    if m := re.search(r"\d{4}-\d{2}-\d{2}", dir):
        if m.group() < begin_date:
            continue
    else:
        continue

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
