#!/usr/bin/python3
""" Fabric script to compress contents of web_static """

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of `web_static`
    """
    # Create timestamp to append to archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Archive name
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # Create the archive using local command
    archive_path = "versions/{}".format(archive_name)
    command = "tar -czvf {} web_static".format(archive_path)

    result = local(command)

    # Clean up
    if result.failed:
        return None
    return archive_path
