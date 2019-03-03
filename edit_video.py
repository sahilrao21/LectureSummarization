from moviepy.editor import VideoFileClip, concatenate_videoclips
import video_indices

def edit_summarized_video(video, tuples):
    clips = []
    for tuple in tuples:
        clip = VideoFileClip(video).subclip(tuple[0], tuple[1])
        clips += [clip]
    final_clip = concatenate_videoclips(clips)
    final_video = video.replace(".mp4", "_sum.mp4")
    final_clip.write_videofile(final_video)


# edit_summarized_video("1qy9xVEOI40.mp4", video_indices.video_indices("1qy9xVEOI40_auto.en.vtt","1qy9xVEOI40_sum.txt"))
