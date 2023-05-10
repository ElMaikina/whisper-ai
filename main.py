import whisper

model = whisper.load_model("base")

audio = "audio.mp3"
translate = model.transcribe(audio, task="translate")

print(translate["text"])