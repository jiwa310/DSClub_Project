from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="michellejieli/emotion_text_classifier")
print(classifier("Good morning China. Right now I am holding ice cream. I love ice cream!"))