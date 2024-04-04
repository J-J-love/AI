from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    os.system(f"start {output_file}")  # 在Windows上用默认音乐播放器播放
    # 如果你使用的是其他操作系统，请根据需要修改上述行，以在相应系统上播放音频。

if __name__ == "__main__":
    input_text = "你好，这是一个文本转语音的示例。"
    text_to_speech(input_text, language='zh-cn', output_file='output.mp3')
