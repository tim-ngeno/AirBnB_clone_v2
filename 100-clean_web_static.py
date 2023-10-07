#!/usr/bin/python3
"""
Fabfile scripts:
do_pack:
    compresses the contents of web_static into an archive

do_deploy:
    distributes the archive file to the servers

deploy:
    Creates and distributes an archive to the web servers

do_clean:
    Performs clean-up of old/outdated archive files

"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ["18.209.152.248", "54.157.179.19"]


@runs_once
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


def deploy():
    """
    Create and distributes an archive to web servers
    """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)


def do_clean(number=0):
    """
    Deletes out-of-date arrchives from the servers
    """
    number = int(number)
    if number <= 1:
        number = 1

    with lcd("versions"):
        local_archives = local("ls -t", capture=True).split("\n")
        for archive in local_archives[number:]:
            local("rm -f {}".format(archive))

    # Remote cleanup
    data_path = "/data/web_static/releases"
    with cd(data_path):
        archives = run("ls -t -d */ | sed 's|/$||'").split("\n")
        for archive in archives[number:]:
            run("rm -rf {}/{}".format(data_path, archive))
