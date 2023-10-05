#!/usr/bin/python3
"""
Fabfile to deploy an archive to servers
"""

from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ["18.209.152.248", "54.157.179.19"]


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


def do_deploy(archive_path):
    """
    Distributes the archive file to the web servers
    """
    if os.path.exists(archive_path):
       # Upload archive to /tmp/ directory
        put(archive_path, "/tmp/")

        # Extract filename without extension
        basefile = os.path.basename(archive_path)
        filename = basefile.split(".")[0]

        data_path = "/data/web_static/releases"
        # Create directory if it doesn't exist
        run("mkdir -p {}/{}".format(data_path, filename))

        # uncompress the archive to the folder on the web servers
        run("tar -xzf /tmp/{} -C {}/{}".
            format(basefile, data_path, filename))

        # delete the archive from the web servers
        run("rm /tmp/{}".format(basefile))

        # delete the symbolic link
        run("rm -rf /data/web_static/current")

        # create a new symbolic link
        run("ln -s {}/{} /data/web_static/current".
            format(data_path, filename))

        print("New version deployed!")
        return True

    return False
