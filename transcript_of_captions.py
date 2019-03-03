import webvtt

#
def generate_transcript(file):
    """Generates the transcript of a given .vtt file."""
    if len(file) < 4 or file[-4:] != ".vtt":
        print("Error: non .vtt file passed in.")
        return 0

    vtt = webvtt.read(file)
    captions = sum([c.text.strip().splitlines() for c in vtt], [])
    print(captions)
    captions_without_descrip = list(map(ignore_descriptions, captions))
    print(captions_without_descrip)
    transcript = ""
    prev_cap = ""
    for i in range(len(captions_without_descrip)):
        curr_cap = captions_without_descrip[i]
        if i != 0:
            prev_cap = captions_without_descrip[i - 1]

        if prev_cap != curr_cap:
            transcript += curr_cap + " "

    return transcript


#def ignore_descriptions(text):
#    """Avoids speaker names or other descriptions provided by captions."""
#    print("HERE")
#    if text == "":
#        return text

#    symbols_to_avoid = ["[", "]", "{", "}"]
#    text_without_descrip = ""
#    for chars in text:
#        print(chars)
#        if (not chars[0].isalpha() and chars[0] not in symbols_to_avoid) or \
#                (chars[0].isalpha() and chars[0].islower()):
#            text_without_descrip += chars

#    return text_without_descrip

def ignore_descriptions(text):
    start_index = text.find("[")
    end_index = text.find("]")
    curr_text = ""
    #count = 0

    if start_index == -1 or end_index == -1: #and count == 0:
        return text

    #while start_index != -1:
    #+= text[0: start_index] + text[end_index + 1:]

    #start_index = curr_text.find("[")
    #end_index = curr_text.find("]")
    #count += 1

    #return curr_text
    return text[: start_index - 1] + ignore_descriptions(text[end_index + 1:])

def ignore_names(text):
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






#print(ignore_descriptions("hello there [my friend, ok], yes sir."))
#print(ignore_names("DAN GARCIA: yes "))
#print(ignore_names("DAN GARCIA: yes Sahil haha. SAHIL RAO: oh no. jamES CARL: ye"))
#ci = "DAN GARCIA: yes Sahil haha. SAHIL RAO: oh no. jamES CARL: ye"["DAN GARCIA: yes Sahil haha. SAHIL RAO: oh no. jamES CARL: ye".find(":") + 2:]
ci = "yes Sahil haha. SAHIL RAO: oh no. jamES CARL: ye"
#print(ci)
#ci2 = ci.find(":")
#print(ignore_names(ci))

print(ignore_names(ci))
#print(generate_transcript("COMPSCI 170 - 2019-02-19-f7fri6FsvvQ.en.vtt"))
#print([1,2,3][0:-1])
#print(list(map(lambda x: 1, ['s','a','h','u','k'])))