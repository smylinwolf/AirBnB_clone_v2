#!/usr/bin/python3
# A fabric script that generates a tarball compressed with gzip archive

from fabric.api import local
from datetime import datetime

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
