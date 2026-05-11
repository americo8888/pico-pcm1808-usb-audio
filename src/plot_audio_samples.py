#!/usr/bin/env python3
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import platform

if __name__ == '__main__':

    # If you got "ValueError: No input device matching", that is because your PC name example device
    # differently from tested list below. Uncomment the next line to see full list and try to pick correct one
    # print(sd.query_devices())

    fs = 48000     # Sample rate
    duration = 1   # Duration of recording
    channels = 2

    if platform.system() == 'Windows':
        device = 'Microphone (MicNode_Stereo), Windows WASAPI'
    elif platform.system() == 'Darwin':
        device = 'MicNode_Stereo'
    else:
        device = 'default'

    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='float32', device=device)
    print('Waiting...')
    sd.wait()  # Wait until recording is finished
    print('Done!')


    time = np.arange(0, duration, 1 / fs)  # time vector
    # strip starting zero

    plt.plot(time, myrecording)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.title('MicNode Stereo')
    plt.legend(['Left', 'Right'])
    plt.show()
