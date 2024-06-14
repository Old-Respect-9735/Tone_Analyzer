import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)

# input the recorded wav file
sampFreq, sound = wavfile.read("C:/Users/User/Downloads/Tone_Analyzer-main/Tone_Analyzer-main/test_audio.wav")

# sampling rate for MinecraftAudio.wav = 48000 (samples per second)
# print(sound.dtype, sampFreq)

# making a nice range for our own use
length_in_s = sound.shape[0] / sampFreq
time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s

dom_freq = []

samp_range = int(sampFreq/9.4)
count = 0
fft_ret = np.zeros((94, 2554))
t_constant = 0

while count < len(sound):
    
    if (count+samp_range > len(sound)):
        break
    sample = sound[count: int(count+samp_range) ]
    fft_spectrum = np.fft.rfft(sample)
    freq = np.fft.rfftfreq(sample.size, d=1./samp_range)
    

    fft_spectrum_abs = np.abs(fft_spectrum)
    # plt.plot(freq[count:int(count + samp_range)], fft_spectrum_abs[count:int(count + samp_range)])
    # plt.xlabel("frequency, Hz")
    # plt.ylabel("Amplitude, units")
    # plt.show()

    spec = True

    if spec:
        # fft_spectrum_avg = []
        # sum = 0
        # for i in range(1, 2554):
        #     sum += fft_spectrum_abs[i]
        #     if (i % 16 == 0):
        #         fft_spectrum_avg.append(sum/16.0)
        #         sum = 0
        # fft_spectrum_avg.append((fft_spectrum_abs[-1]+fft_spectrum_avg[-2])/2.0)

        fft_ret[t_constant] = fft_spectrum_abs
        t_constant += 1

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
new_time = []
t = 0
for i in range(len(dom_freq)):
    new_time.append(t)
    t += 0.1

dom_freq = np.divide(dom_freq, 10)
spec_matrix = np.column_stack((new_time, dom_freq))
print(fft_ret.size)
# plt.plot(new_time, dom_freq)
plt.imshow(np.transpose(fft_ret), extent=[0,9.4,0,1000], cmap='jet',
           vmin=0, vmax=10000, origin = "lower", aspect='auto')
plt.colorbar()
plt.xlabel("time (s)")
plt.ylabel("frequency ")
plt.show()
