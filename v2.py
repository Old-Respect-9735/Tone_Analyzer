# direct spectrograph from scipy

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# input the recorded wav file

cmap = plt.get_cmap('viridis') # this may fail on older versions of matplotlib
vmin = -40  # hide anything below -40 dB
cmap.set_under(color='k', alpha=None)

rate, frames = wavfile.read("C:/Users/User/Downloads/Tone_Analyzer-main/Tone_Analyzer-main/test_audio.wav")
fig, ax = plt.subplots()
pxx, freq, t, cax = ax.specgram(frames[:], # first channel
                                Fs=rate,      # to get frequency axis in Hz
                                cmap=cmap, vmin=vmin)
cbar = fig.colorbar(cax)
cbar.set_label('Intensity dB')
ax.axis("tight")

# Prettify
import matplotlib
import datetime

ax.set_xlabel('time h:mm:ss')
ax.set_ylabel('frequency kHz')

scale = 1e3                     # KHz
ticks = matplotlib.ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale))
ax.yaxis.set_major_formatter(ticks)

def timeTicks(x, pos):
    d = datetime.timedelta(seconds=x)
    return str(d)
formatter = matplotlib.ticker.FuncFormatter(timeTicks)
ax.xaxis.set_major_formatter(formatter)
plt.show()
