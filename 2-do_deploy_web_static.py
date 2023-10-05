#!/usr/bin/python3
"""
Fabfile to deploy an archive to servers
"""

from fabric.api import local, env, run, put
import os

env.hosts = ["18.209.152.248", "54.157.179.19"]


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
