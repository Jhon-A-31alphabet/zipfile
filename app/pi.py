#pytube api for download videos and audio.....

from pytube import YouTube



def download_video():
    get_l = f"{enter_link}"
    video = YouTube(get_l)
    stream = video.streams.get_highest_resolution()
    stream.download()


