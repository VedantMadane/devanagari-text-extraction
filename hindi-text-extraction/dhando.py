from gtts import gTTS
# path ='C:\Users\\vedantm\Ultimate\DhandhoInvestor.txt'

with open('C:/Users/vedantm/Ultimate/DhandhoInvestor.txt', "r", encoding="utf-8") as f:
    file = f.read()

tts = gTTS(text=file, lang="en")
tts.save("C:/Users/vedantm/Ultimate/dhando.mp3")
print("saved")