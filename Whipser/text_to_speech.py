import whisper
model = whisper.load_model("tiny")
result = model.transcribe("audio-test-files//insane.wav")
print(result["text"])



