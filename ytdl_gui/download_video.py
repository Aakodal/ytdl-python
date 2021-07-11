import subprocess

format_to_arg = [
    ("mp3", "-x --audio-format mp3"),
    ("m4a", "-f 'bestaudio[ext=m4a]'"),
    ("mp4-o", "-f 'bestvideo[ext=mp4]'"),
    ("webm-o", "-f 'bestvideo[ext=webm]'"),
    ("mp4", "-f 'best'"),
    ("webm", "-f 'bestvideo+bestaudio' --merge-output-format webm")
]
format_to_command = {video_format: arg for video_format, arg in format_to_arg}


def download(link, video_format):
    print(format_to_command.get(video_format))
    subprocess.run(
        f"youtube-dl {format_to_command.get(video_format)} -o '$HOME/YouTube-Downloader/%(title)s.%(ext)s' {link}",
        shell=True
    )

