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
links = [x.strip() for x in links.split(',')]

for link in links:
    # Download Subtitles
    rv = check_output('youtube-dl --write-sub --cookies {} --skip-download {}'.format(cookies, link),
                                 shell=True, stderr=STDOUT)
    if "unable to download video subtitles" in str(rv):
        check_output('youtube-dl --write-auto-sub --cookies {} --skip-download {}'.format(cookies, link), shell=True)
    # Download Video if user asked for it
    if flag:
        system('youtube-dl -f 135 --cookies {} {}'.format(cookies, link))

