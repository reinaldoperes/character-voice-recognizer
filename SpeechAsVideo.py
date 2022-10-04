import speech_recognition as sr 
import moviepy.editor as mp

clip = mp.VideoFileClip(r".\\videos\\mp4\\dio.mp4") 
clip.audio.write_audiofile("dio.wav")

clip2 = mp.VideoFileClip(r".\\videos\\mp4\\auto_da_compadecida.mp4") 
clip2.audio.write_audiofile("compadecida.wav")

r = sr.Recognizer()

# DIO
audio = sr.AudioFile("dio.wav")
with audio as source:
  audio_file = r.record(source)
  
result = r.recognize_google(audio_file, language="ja-JP")
print(result)

# Compadecida
audio = sr.AudioFile("compadecida.wav")
with audio as source:
  audio_file = r.record(source)
  
result = r.recognize_google(audio_file, language="pt-BR")
print(result)