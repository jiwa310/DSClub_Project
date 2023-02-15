import whisper
from transformers import pipeline

w_model = whisper.load_model("base")
result = w_model.transcribe("speech-to-text/audio-test-files/insane.wav")
text = result["text"]

print(text)

x = pipeline("sentiment-analysis")

print(x(text))

