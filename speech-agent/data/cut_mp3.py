# Source: https://www.geeksforgeeks.org/cut-a-mp3-file-in-python/

from pydub import AudioSegment

print("Get audio from mp3 ...")
audio_content = AudioSegment.from_mp3("Huberman_Gotfried.mp3")

# pydub does things in milliseconds
a_minute = 60 * 1000

  
first_minute = audio_content[:a_minute]
  
last_minute = audio_content[-a_minute:]

print("Export extracted first minute ...")
first_minute.export("first_minute_huberman.mp3", format="mp3")