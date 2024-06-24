import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, buttord

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)
# fig, (ax1, ax2) = plt.subplots(2)

# input the recorded wav file
sampFreq, sound = wavfile.read("C:/Users/User/Downloads/Tone_Analyzer-main/Tone_Analyzer-main/test.wav")
sound = sound[:,0]
print(len(sound))
samp_range = int(len(sound)/49.0)
fs = int(sound.size/4.9)
# filtering proceess (butterworth filter - lowpass)
single = []
# single = np.log(np.abs(np.fft.rfft(sound[:samp_range])))
# freq = np.fft.rfftfreq(sound[:samp_range].size, d=1./samp_range)
# ax1.plot(freq, single)
# print(len(single))
# print(freq)
# n, wn = buttord(0.5, 0.6, 3, 40)

normal_cutoff = 3000 / (0.5 * len(sound)/4.9)
b, a = butter(9, normal_cutoff, btype='low', analog=False)
sound = filtfilt(b, a, sound, axis = 0)

# single = np.log(np.abs(np.fft.rfft(sound[:samp_range])))
# freq = np.fft.rfftfreq(sound[:samp_range].size, d=1./samp_range)
# ax2.plot(freq, single)
# plt.show()
# single = np.log(np.abs(np.fft.rfft(sound[:samp_range])))
# freq = np.fft.rfftfreq(len(sound[:samp_range]), d=1./fs)
# freq = freq[1:]
# print(sound[:samp_range])
# print(len(sound[:samp_range]))
# print(len(freq))
# print(len(single))
# ax1.plot(freq, single)
# sampling rate for MinecraftAudio.wav = 48000 (samples per second)

# making a nice range for our own use
length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

dom_freq = []

count = 0
fft_ret = np.zeros((49, 2890))
t_constant = 0
check = True
db = []

while count < len(sound):
    
    if (count+samp_range > len(sound)):
        break
    sample = sound[count: int(count+samp_range) ]
    fft_spectrum = np.fft.rfft(sample)
    freq = np.fft.rfftfreq(sample.size, d=1./fs)
    fft_spectrum_abs = np.abs(fft_spectrum)

    spec = True
    
    if spec:
        fft_spectrum_abs = np.log(fft_spectrum_abs)
        fft_ret[t_constant] = fft_spectrum_abs
        t_constant += 1
        db.append(10 * np.log(np.mean(np.power(fft_spectrum_abs, 2))))
        


    else:
        fft_data = np.fft.fft(sample)
        freqs = np.fft.fftfreq(len(sample))

        peak_coefficient = np.argmax(np.abs(fft_data))
        peak_freq = freqs[peak_coefficient]

        dom_freq.append(abs(peak_freq * sampFreq))
    # g = 0
    # g_freq = 0
    # index = 0
    # for i,f in enumerate(fft_spectrum_abs[count:int(count + samp_range)]):
    #     if (np.round(f) > g):
    #         g = f
    #         g_freq = freq[i]
    #         print(freq[i])

    # dom_freq.append(g_freq)
    
    count += samp_range

print(db)

new_time = []
t = 0
for i in range(len(dom_freq)):
    new_time.append(t)
    t += 0.1

plt.plot(range(len(db)), db)

# plt.imshow(np.transpose(fft_ret), extent=[0,4.9,0,2890], cmap='jet',
#            vmin=0, vmax=20, origin = "lower", aspect='auto')
# plt.colorbar()
plt.xlabel("time (samples)") 
plt.ylabel("magnitude (dB)")
plt.show() 
