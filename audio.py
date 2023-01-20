import wave
import array
import numpy as np
import pyaudio

frequency = 523.3  # 音の高さ（Hz）
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
for i in range(60):
    stream.write(sine_wave.tobytes())
stream.stop_stream()
stream.close()
p.terminate()
