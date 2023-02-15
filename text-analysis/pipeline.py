import whisper
from transformers import pipeline

w_model = whisper.load_model("base")
result = w_model.transcribe("/Users/hongtan/Desktop/DSClub_Project/speech-to-text/audio-test-files/my_recording.wav")
text = result["text"]

print(text)

x = pipeline("sentiment-analysis")

print(x(text))

