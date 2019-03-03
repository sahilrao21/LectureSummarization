from flask import Flask, render_template, request, redirect, url_for
import dl_youtube, os
from puncuator import punctuate_transcript
import sumy_lex_rank, video_indices, edit_video

app = Flask(__name__)

class Summarization():
    the_link = None
    the_props = None

summ = Summarization()

@app.route("/")
def search_home():
    return render_template("index.html")

@app.route("/props", methods=['POST'])
def props():
    # session['the_link'] =
    the_link = request.form['link']
    summ.the_link = the_link

    # percentage_size = float(request.form['proportion'])

    # the_cookies = request.form['cookies']
    # video_yn = request.form['download_video']
    # audio_yn = request.form['download_audio']
    assert the_link is not '', "Please Input a Link"
    # assert percentage_size>=0.33 and percentage_size <= 1, "Please Input a Valid Proportion"
    # tuple = dl_youtube.video_download(the_link, 135)
    # vtt = tuple[1]
    # the_transcript = punctuate_transcript(vtt)
    return render_template("props.html")

@app.route("/transcript", methods=['POST'])
def transcript():
    link_again = summ.the_link
    the_props = request.form['proportion']
    print("Downloading Video")
    tuple = dl_youtube.video_download(link_again, 22)
    vtt = tuple[1]
    video = tuple[0]
    print("Loading Transcript")
    file = punctuate_transcript(vtt)
    print("Summarizing Lecture")
    with open(file[:-4] + "_sum.txt", "w+") as lex_rank_summary_file:
        lex_rank_summary_file.write(sumy_lex_rank.lex_rank_summarizer(file, the_props))
    print("Finding TimeStamps")
    times = video_indices.video_indices(vtt, file[:-4] + "_sum.txt")
    print('Rendering Video')
    final = edit_video.edit_summarized_video(video, times)
    return render_template("transcript.html")

if __name__ == "__main__":
    app.run(debug=True)
