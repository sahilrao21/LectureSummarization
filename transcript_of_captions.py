import webvtt

#
def generate_transcript(file):
    """Generates the transcript of a given .vtt file."""
    if len(file) < 4 or file[-4:] != ".vtt":
        print("Error: non .vtt file passed in.")
        return 0

    vtt = webvtt.read(file)
    captions = sum([c.text.strip().splitlines() for c in vtt], [])

    transcript = ""
    prev_cap = ""
    for i in range(len(captions)):
        curr_cap = captions[i]
        if i != 0:
            prev_cap = captions[i - 1]

        if prev_cap != curr_cap:
            transcript += curr_cap + " "

    return transcript
