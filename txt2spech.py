from gtts import gTTS
text="Hiii my name is Ayan"
language='en'
obj=gTTS(text=text,lang=language,slow=False)
obj.save("speech.mp3")
