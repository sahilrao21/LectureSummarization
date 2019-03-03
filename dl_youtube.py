from subprocess import check_output, STDOUT
from os import system

#Update youtube-dl
rv = check_output('pip install youtube-dl', shell=True)
if "Requirement already satisfied" in str(rv):
    check_output("pip install --upgrade youtube-dl", shell=True)

"""
Downloads the video and associated subtitle, and returns the file name as a tuple

Input:
link(str): Youtube video link, e.g: https://www.youtube.com/watch?v=zbf3ILq9IJs
video(False/int): False if don't want video, 22 if want audio, 135 if not
cookies(str): filename of cookies file. Default is cookies.txt

Output:
Tuple in the format (video file, subtitle file). Will return (None, subtitle file) if video is not selected, and 
subtitle_auto if the subtitles are auto generated.
"""
def video_download(link, video, cookies="cookies.txt"):
    # Download Subtitles
    linkid = link[link.find("watch?v=") + 8:]

    subtitle = linkid+".en.vtt"
    rv = check_output('youtube-dl --write-sub --cookies {} --output "%(id)s.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True, stderr=STDOUT)
    if "unable to download video subtitles" in str(rv):
        subtitle = linkid+"_auto.en.vtt"
        check_output('youtube-dl --write-auto-sub --cookies {} --output "%(id)s_auto.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True)
    
    # Download Video if user asked for it
    if video:
        system('youtube-dl -f {} --cookies {} --output "%(id)s.%(ext)s" {}'.format(video, cookies, link))

    return (linkid+".mp4", subtitle) if video else (None, subtitle)

if __name__ == "__main__":
    # get input
    links = input("Video Links (comma separated):\n\t")
    links = [x.strip() for x in links.split(',')]
    cookies = input("Cookies Text File Name:\n\t")
    cookies = "cookies.txt" if cookies.lower() == '' else cookies
    video = input("Download Videos? y/n\n\t")
    video = True if video.lower() == 'y' else False
    if video:
        audio = input("Audio? This will take longer to download y/n:\n\t")
        video = '22' if audio.lower() == 'y' else '135'
    for link in links:
        print(video_download(link, video, cookies))

