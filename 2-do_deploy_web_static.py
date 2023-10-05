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
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory
        put(archive_path, "/tmp/")

        # Extract filename without extension
        basefile = os.path.basename(archive_path)
        filename = basefile.split(".")[0]

        # Create directory if it doesn't exist
        run("mkdir -p /data/web_static/releases/{}".
            format(filename))

        # uncompress the archive to the folder on the web servers
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
            format(basefile, filename))

        # delete the archive from the web servers
        run("rm /tmp/{}".format(basefile))

        # delete the symbolic link
        run("rm -rf /data/web_static/current")

        # create a new symbolic link
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(filename))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        print("Deployment failed...")
        return False
