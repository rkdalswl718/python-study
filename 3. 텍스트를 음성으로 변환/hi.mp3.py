from gtts import gTTS

text = "우와 대박이다.";
tts = gTTS(text=text, lang='ko');
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3");