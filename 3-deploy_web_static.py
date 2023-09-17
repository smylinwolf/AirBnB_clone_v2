#!/usr/bin/python3
# A fabric script that generates a tarball compressed with gzip archive

from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['54.157.129.183', '52.91.125.123']
env.users = "ubuntu"


def do_pack():
    """ A function, using a fabric script to generate a tgz archive
    from the the contents of the web_static """

    try:
        # Create a formatted timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the archive_name
        archive_name = "web_static_{}.tgz".format(timestamp)

        # create the versions folder if it does not exist
        local("mkdir -p versions")

        # create an archive from the contents of web_static
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the archive
        return "versions/{}".format(archive_name)

    except Exception:
        # Return None if an Error Occurs while execution
        return None


def do_deploy(archive_path):
    """ My function to deploy the archive """

    if not os.path.exists(archive_path):
        return false

    try:
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # the archive filename without extension
        archive_filename_uno = archive_path.split("/")[-1]
        archive_filename = archive_filename_uno.split(".")[0]

        run("mkdir -p /data/web_static/releases/{}/".format(archive_filename))

        # uncompress the archive to the webserver directory
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename_uno, archive_filename))

        # delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename_uno))

        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                archive_filename, archive_filename))

        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_filename))

        # delete the symbolic link from the web_server
        run("rm -rf /data/web_static/current")

        # create a new symbolic link on the web server
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_filename))

        return True

    except Exception:
        return False


def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
