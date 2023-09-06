from moviepy.editor import concatenate_audioclips, AudioFileClip
import os

def combineAudio(directory,book,first,last):
    audioFiles = [AudioFileClip(os.path.join(directory,filename)) for filename in os.listdir("combine")]
    combined = concatenate_audioclips(audioFiles)
    combined.write_audiofile(f"{book}{first}-{last}.mp3")
