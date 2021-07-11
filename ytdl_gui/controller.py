import subprocess as sp
import bottle as bt
from ytdl_gui import root, download_video

if sp.run("type ffmpeg", shell=True).returncode != 0 or sp.run("type youtube-dl", shell=True).returncode != 0:
    exit(1)


@bt.route("/", method="GET")
def main_page():
    return bt.template("index.html")


@bt.route("/finished", method="GET")
def finished():
    return bt.template("finished.html")


@bt.route("/dl", method="POST")
def download_req():
    forms = bt.request.forms
    link = forms.get("link")
    video_format = forms.get("format")

    try:
        download_video.download(link, video_format)
    except Exception as exc:
        raise bt.HTTPError(400, str(exc))

    bt.redirect("/finished")


@bt.route("/assets/<filepath:path>", method="GET")
def assets(filepath):
    return bt.static_file(filepath, root=root.joinpath('assets'))
