import os
import sys
import pytube
from tqdm import tqdm


# Confirms if URL is Youtube
def confirmURL(ytUrl):
    if 'youtube' not in ytUrl.lower():
        print("Please use a youtube URL")
        exit()


def progressBar(stream):
    for i in tqdm(range(stream.filesize)):
        pass


# This will download URL provided to command
def downloadVideoUrl(stream, path):
    try:  # Always download video in highest resolution
        stream = yt.streams.filter(file_extension='mp4').first()
    except Exception as exc:
        print(exc)

    print("downloading", yt.title)
    try:
        stream.download(path, yt.title)
        progressBar(stream)
        print("files downloaded to {}".format(os.path.abspath(path)))
    except Exception as exc:
        print(exc)


if __name__ == '__main__':
    default_output_dir = './videos/'
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('USAGE: python YoutubeVideoDloader.py "YoutubeURL"')
        exit()
    else:
        ytUrl = sys.argv[1]
        yt = pytube.YouTube(ytUrl)
        confirmURL(ytUrl)

    if not ytUrl.startswith("http"):
        ytUrl = 'https://' + ytUrl

    try:
        # make directory if dir specified doesn't exist
        os.makedirs(default_output_dir, exist_ok=True)
        downloadVideoUrl(yt, default_output_dir)

    except OSError as e:
        print(e)
        exit()
