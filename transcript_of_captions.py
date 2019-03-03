import webvtt

def generate_transcript(file):
    """Generates the transcript of a given .vtt file."""
    if len(file) < 4 or file[-4:] != ".vtt":
        print("Error: non .vtt file passed in.")
        return 0

    vtt = webvtt.read(file)
    captions = sum([c.text.strip().splitlines() for c in vtt], [])

    captions_of_lecture = list(map(ignore_descriptions, captions))
    captions_of_lecture = list(map(ignore_names(), captions))
    transcript = ""
    prev_cap = ""
    for i in range(len(captions_of_lecture)):
        curr_cap = captions_of_lecture[i]
        if i != 0:
            prev_cap = captions_of_lecture[i - 1]

        if prev_cap != curr_cap:
            transcript += curr_cap + " "

    return transcript

def ignore_descriptions(text):
    """Taking out information in brackets that are auto-generated."""
    start_index = text.find("[")
    end_index = text.find("]")

    if start_index == -1 or end_index == -1:
        return text
    return text[: start_index - 1] + ignore_descriptions(text[end_index + 1:])

def ignore_names(text):
    """Ignore captions that give the name of the speaker."""
    colon_index = text.find(":")
    print("COL_INDEX", colon_index)
    if colon_index == -1 or len(text) <= 1:
        return text

    reverse_name = ""
    for i in range(colon_index):
        reverse_index = colon_index - i - 1
        curr_letter = text[reverse_index]
        print("index", reverse_index)
        print("curr_letter", curr_letter)

        if curr_letter.isupper() or curr_letter == " ":
            reverse_name += curr_letter
        else:
            break
        print("reverse_name", reverse_name)

    name = reverse_name[::-1]

    return text[:text.find(name)] + ignore_names(text[colon_index + 1:])

ci = "DAN GARCIA: yes Sahil haha. SAHIL RAO: oh no. jamES CARL: ye"
print(ignore_names(ci))