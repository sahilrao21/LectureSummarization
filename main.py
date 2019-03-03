from flask import Flask, render_template, request, redirect
import dl_youtube, os
from puncuator import punctuate_transcript

app = Flask(__name__)

@app.route("/")
def search_home():
    return render_template("index.html")

@app.route("/transcript", methods=['POST'])
def transcript():
    the_link = request.form['link']

    percentage_size = float(request.form['proportion'])
    # the_cookies = request.form['cookies']
    # video_yn = request.form['download_video']
    # audio_yn = request.form['download_audio']
    assert the_link is not '', "Please Input a Link"
    assert percentage_size>=0.33 and percentage_size <= 1, "Please Input a Valid Proportion"
    vtt = dl_youtube.video_download(the_link, False)[1]
    print("file:///"+os.getcwd()+'/' + vtt)
    the_transcript = punctuate_transcript(vtt)
    # return render_template("transcript.html", transc=the_transcript)
    return redirect("file:\\\\\\"+os.getcwd()+'\\' + vtt)

if __name__ == "__main__":
    app.run(debug=True)
