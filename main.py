from flask import Flask, render_template, request, send_from_directory
import dl_youtube, os
from puncuator import punctuate_transcript
import sumy_lex_rank, video_indices, edit_video

# static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
app = Flask(__name__)


# @app.route('/dir', methods=['GET'])
# def serve_dir_directory_index():
#     return send_from_directory(static_file_dir, 'index.html')
#
#
# @app.route('/dir/<path:path>', methods=['GET'])
# def serve_file_in_dir(path):
#     if not os.path.isfile(os.path.join(static_file_dir, path)):
#         path = os.path.join(path, 'index.html')
#
#     return send_from_directory(static_file_dir, path)
#
#


class Summarization():
    the_link = None
    the_props = None

summ = Summarization()

@app.route("/")
def search_home():
    return render_template("index.html")

@app.route("/props", methods=['POST'])
def props():
    the_link = request.form['link']
    summ.the_link = the_link
    assert the_link is not '', "Please Input a Link"

    return render_template("props.html")

@app.route("/transcript", methods=['POST'])
def transcript():
    link_again = summ.the_link
    the_props = float(request.form['proportion'])
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
    return render_template("transcript.html", final_video=final)

if __name__ == "__main__":
    app.run(debug=True)
