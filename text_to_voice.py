from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
file_path = 'subdata/mytext.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file, lang= 'ko')

tts.save("my_text.mp3")
playsound("subdata/my_text.mp3") #pip3 install PyObjC 설치 후 오류 해결


