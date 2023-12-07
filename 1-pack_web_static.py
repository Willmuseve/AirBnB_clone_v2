#!/usr/bin/python3
# A fabric script that generates a .tgz archive from the items
# of the web_static folder of your AirBnB Clone repositorry

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive."""
    y = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(y.year,\
y.month,y.day,y.hour,y.minute,y.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
