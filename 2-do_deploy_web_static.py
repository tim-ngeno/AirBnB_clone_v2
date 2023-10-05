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
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(a_path, f_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))

        print("New version deployed!")
        return True

    return False
