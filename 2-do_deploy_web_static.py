#!/usr/bin/python3
"""defines func do_deploy
"""
from fabric.api import run, put, env
from os import path

env.hosts = ["ubuntu@34.229.137.94", "ubuntu@100.26.246.233"]


def do_deploy(archive_path):
    """deploys archived web-static to servers"""

    if not path.exists(archive_path):
        return False
    else:
        try:
            last_in = archive_path.rfind("/") + 1
            arch = archive_path[last_ind:]
            w = arch[: arch.find(".")]
            put(archive_path, "/tmp/")
            run("mkdir -p /data/web_static/releases/{}/".
                format(w))
            run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                    arch, w))
            run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
                w, w))
            run("rm -rf /data/web_static/releases/{}/web_static".format(
                    w, w))
            run("rm -f /tmp/{}".format(arch))
            run("rm -f /data/web_static/current")
            run("ln -s /data/web_static/releases/{} /data/web_static/current".
                format(w))
            return True
        except Exception:
            return False
