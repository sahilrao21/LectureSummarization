from flask import Flask, render_template, request
import youtube_dl
import transcript_of_captions

app = Flask(__name__)
@app.route("/")
def search_home():
   return render_template("index.html")

@app.route("/transcript", methods=['POST'])
def transcript():
    the_link = request.form['link']
    # the_cookies = request.form['cookies']
    # video_yn = request.form['download_video']
    # audio_yn = request.form['download_audio']
    vtt = youtube_dl.video_download(the_link, 22)
    the_transcript = transcript_of_captions.generate_transcript(vtt)

    return render_template("transcript.html")



if __name__ == "__main__":
    app.run(debug=True)
