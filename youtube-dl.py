from subprocess import check_output, STDOUT
from os import system

#Update youtube-dl
rv = check_output('pip install youtube-dl', shell=True)
if "Requirement already satisfied" in str(rv):
    check_output("pip install --upgrade youtube-dl", shell=True)

def video_download(links, video, cookies="cookies.txt"):
    for link in links:
        # Download Subtitles
        rv = check_output('youtube-dl --write-sub --cookies {} --output "%(id)s.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True, stderr=STDOUT)
        if "unable to download video subtitles" in str(rv):
            check_output('youtube-dl --write-auto-sub --cookies {} --output "%(id)s_auto.%(ext)s" --skip-download {}'
                     .format(cookies, link), shell=True)
    
        # Download Video if user asked for it
        if video:
            system('youtube-dl -f {} --cookies {} {}'.format(video, cookies, link))


if __name__=="__main__":
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
    video_download(links, video, cookies)

