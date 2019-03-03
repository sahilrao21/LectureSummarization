from subprocess import check_output, STDOUT, Popen, PIPE
from os import system

#Update youtube-dl
rv = check_output('pip install youtube-dl', shell=True)
if "Requirement already satisfied" in str(rv):
    check_output("pip install --upgrade youtube-dl", shell=True)

#get input
links = input("Video Links (comma separated):\n\t")
cookies = input("Cookies Text File Name:\n\t")
cookies = "cookies.txt" if cookies.lower()=='' else cookies
flag = input("Download Videos? y/n\n\t")
flag = True if flag.lower()=='y' else False
if flag:
    audio = input("Audio? This will take longer to download y/n:\n\t")
    audio = '22' if audio.lower() == 'y' else '135'
links = [x.strip() for x in links.split(',')]

for link in links:
    # Download Subtitles
    system('youtube-dl --write-auto-sub --cookies {} --skip-download {}'.format(cookies, link))
    
    # Download Video if user asked for it
    if flag:
        system('youtube-dl -f {} --cookies {} {}'.format(audio, cookies, link))
