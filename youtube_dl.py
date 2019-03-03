from subprocess import check_output, STDOUT
from os import system

#Update youtube-dl
rv = check_output('pip install youtube-dl', shell=True)
if "Requirement already satisfied" in str(rv):
    check_output("pip install --upgrade youtube-dl", shell=True)


"""
Downloads the video and associated subtitle, and returns the file name as a tuple
link(str): Youtube video link, e.g: https://www.youtube.com/watch?v=zbf3ILq9IJs
video(False/int): False if don't want video, 22 if want audio, 135 if not
cookies(str): filename of cookies file. Default is cookies.txt
"""
def video_download(link, video, cookies="cookies.txt"):
    # Download Subtitles
    id = link[link.find("watch?v=") + 8:]

    subtitle = id+".en.vtt"
    rv = check_output('youtube-dl --write-sub --cookies {} --output "%(id)s.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True, stderr=STDOUT)
    if "unable to download video subtitles" in str(rv):
        subtitle = id+"_auto.en.vtt"
        check_output('youtube-dl --write-auto-sub --cookies {} --output "%(id)s_auto.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True)
    
    # Download Video if user asked for it
    if video:
        system('youtube-dl -f {} --cookies {} --output "%(id)s.%(ext)s" {}'.format(video, cookies, link))

    return (id+".mp4", subtitle) if video else (None, subtitle)



