from moviepy.editor import VideoFileClip, concatenate_videoclips

def edit_summarized_video(video, tuples):
    clips = []
    for tuple in tuples:
        clip = VideoFileClip(video).subclip(tuple[0], tuple[1])
        clips += [clip]
    final_clip = concatenate_videoclips(clips)
    final_video = video.replace(".mp4", "_sum.mp4")
    final_clip.write_videofile(final_video)
