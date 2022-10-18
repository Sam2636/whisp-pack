# import whisper

# model = whisper.load_model("base")
# result = model.transcribe("greetings.mp3",fp16=False)
# print(result["text"])

from sympy import jacobi_poly
import whisper
model = whisper.load_model("base")


# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("greetings.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions(language='en',fp16=False)
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = result.text

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("greeting_en.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
