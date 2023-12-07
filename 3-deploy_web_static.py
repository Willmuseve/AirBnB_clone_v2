#!/usr/bin/bash
"""
script that creates and
distributes an archive to web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['34.229.137.94', '100.26.246.233']


def do_pack():
    """ a function generate an archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        f = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(f))
        return f
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to web servers"""
    if exists(archive_path) is False:
        return False
    try:
        files = archive_path.split("/")[-1]
        no = files.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no))
        run('tar -xzf /tmp/{} -C {}{}/'.format(files, path, no))
        run('rm /tmp/{}'.format(files))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no))
        run('rm -rf {}{}/web_static'.format(path, no))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no))
        return True
    except:
        return False


def deploy():
    """creates and distributes archives"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
