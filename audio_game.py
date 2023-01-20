import wave
import array
import numpy as np
import pyaudio
import random as rd


def sound(self,self2=60):
    frequency = self  # 音の高さ（Hz）
    sampling_rate = 44100  # サンプリング周波数（Hz）
    num_samples = sampling_rate  # 音の長さ（サンプル数）

    # 音データを生成
    sine_wave = array.array("h", [0] * num_samples)
    for i in range(num_samples):
        sine_wave[i] = int(32767 * np.sin(2 * np.pi * frequency * i / sampling_rate))

    # 音データをワイブ形式で保存
    with wave.open("440hz.wav", "w") as wave_file:
        wave_file.setparams((1, 2, sampling_rate, num_samples, "NONE", "not compressed"))
        wave_file.writeframes(sine_wave.tobytes())

    # 音を再生
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=sampling_rate, output=True)
    def ply():
        stream.write(sine_wave.tobytes())
    for i in range(self2):
        ply()
    stream.stop_stream()
    stream.close()
    p.terminate()

def main(ans):
    inp = ""
    i = 0
    while True:  
        inp = input("音を聞く：1　答える：2　やめる：3>>")
        if inp == "1":
            sound(ans)
            i += 1
            inp = input("乱数は... >>")
            if int(inp) == ans:
                print("\n正解！！！！！！")
                print("乱数は："+str(ans)+"でした！")
                print("当てるまで聞いた回数："+str(i))
                return 1
            else:
                print("ちがいます...")
                continue
        elif inp == "2":
            inp = input("乱数は... >>")
            if int(inp) == ans:
                print("\n正解！！！！！！")
                print("乱数は："+str(ans)+"でした！")
                print("当てるまで聞いた回数："+str(i))
                return 1
            else:
                print("ちがいます...")
                continue
        elif inp == "3":
            break
    return 0

print("音から乱数あてゲーム")
print("・60秒間でうなりを聞いて乱数をあてよう。")
print("・耳壊れてもしらん")
print("・乱数は整数で、440~2000Hzの間です。\n")
rdm = 0
x = 0
while True:
    rdm = rd.randint(440,2000)
    x = main(rdm)
    inp = input("もう一度続ける？(y) >>")
    if inp == "y" or inp == "Y":
        continue
    else:
        break
