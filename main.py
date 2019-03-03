from flask import Flask, render_template, request
import dl_youtube
import puncuator

app = Flask(__name__)
@app.route("/")
def search_home():
   return render_template("index.html")

@app.route("/transcript", methods=['POST'])
def transcript():
    the_link = request.form['link']
    vtt = dl_youtube.video_download(the_link, 22)
    txt = vtt[1]
    punctuated = puncuator.punctuate_transcript(txt)

    # the_transcript = transcript_of_captions.generate_transcript(vtt)
    # txt_file = transcript_of_captions.populate_file(the_transcript)
    return render_template("transcript.html")

if __name__ == "__main__":
    app.run(debug=True)
