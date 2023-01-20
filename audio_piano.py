import wave
import array
import numpy as np
import pyaudio

def sound(freq,leng,sht=0):
    frequency = freq  # 音の高さ（Hz）
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
    if sht == 0:
        for i in range(leng):
            stream.write(sine_wave.tobytes())
    elif sht == 1:
        stream.write(sine_wave.tobytes())
    stream.stop_stream()
    stream.close()
    p.terminate()

"""
 C-C#-D-D#-E-F-F#-G-G#-A-A#-B
 0-1 -2-3 -4-5-6 -7-8 -9-9 -10
"""
c5base_ary = [523.3,554.4,587.3,622.3,659.3,698.5,740.0,784.0,830.6,880.0,932.3,987.8]

import time

#カエルのうた
sound(c5base_ary[0],1) #か
sound(c5base_ary[2],1) #え
sound(c5base_ary[4],1) #る
sound(c5base_ary[5],1) #の
sound(c5base_ary[4],1) #う
sound(c5base_ary[2],1) #た
sound(c5base_ary[0],1) #が
time.sleep(0.5)
sound(c5base_ary[4],1) #き
sound(c5base_ary[5],1) #こ
sound(c5base_ary[7],1) #え
sound(c5base_ary[9],1) #て
sound(c5base_ary[7],1) #く
sound(c5base_ary[5],1) #る
sound(c5base_ary[4],1) #よ
time.sleep(0.5)
sound(c5base_ary[0],1) #ぐあ
time.sleep(0.5)
sound(c5base_ary[0],1) #ぐあ
time.sleep(0.5)
sound(c5base_ary[0],1) #ぐあ
time.sleep(0.5)
sound(c5base_ary[0],1) #ぐあ
time.sleep(0.5)
sound(c5base_ary[0],1,1) #ぐぇ
sound(c5base_ary[2],1,1) #ぐぇ
sound(c5base_ary[4],1,1) #ぐぇ
sound(c5base_ary[5],1,1) #ぐぇ
sound(c5base_ary[4],1) #ぐあ
sound(c5base_ary[2],1) #ぐあ
sound(c5base_ary[0],1) #ぐあ