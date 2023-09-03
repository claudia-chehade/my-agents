import whisper
model = whisper.load_model("base")

# result = model.transcribe("2023-05-05_22h27_37.mp4")
result = model.transcribe("../data/Huberman_Gotfried.mp3")
# result = model.transcribe("https://www.voiptroubleshooter.com/open_speech/american/OSR_us_000_0061_8k.wav", 
#                           verbose = True)
text_result = result["text"]
print(text_result)

with open("../data/Huberman_Gotfried.txt", "w") as file:
        file.write(text_result)