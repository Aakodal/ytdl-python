import subprocess
import bottle as bt

format_to_arg = [
    ("mp3", "-x --audio-format mp3"),
    ("m4a", "-f 'bestaudio[ext=m4a]'"),
    ("webm-ao", "-f 'bestaudio[ext=webm]'"),
    ("mp4-vo", "-f 'bestvideo[ext=mp4]'"),
    ("webm-vo", "-f 'bestvideo[ext=webm]'"),
    ("mp4", "-f 'best'"),
    ("webm", "-f 'bestvideo[ext=webm]+bestaudio[ext=webm]' --merge-output-format webm")
]
format_to_command = {video_format: arg for video_format, arg in format_to_arg}


def download(link, video_format, default_metadata, **metadata):
    args = ["youtube-dl"]
    args += format_to_command.get(video_format).split(" ")

    if default_metadata is not None:
        args.append("--add-metadata")

    if len(metadata) != 0:
        args.append("--postprocessor-args")
        ffmpeg_args = " ".join(list(map(
            lambda tup: f"-metadata {tup[0]}=" + '"' + tup[1].replace("'", "").replace('"', "") + '"',
            metadata.items()
        )))
        args.append(f"'{ffmpeg_args}'")

    args += ["-o", "'$HOME/YouTube-Downloader/%(title)s.%(ext)s'", f'"{link}"']

    subprocess.run(" ".join(args), shell=True)

    # TODO: implement path
    return bt.template("finished.html", path="path")
