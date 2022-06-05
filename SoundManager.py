import pyaudio
import numpy as np
import pylab
import time
import sys
import matplotlib.pyplot as plt
import sounddevice as sd

RATE = 44100
CHUNK = int(RATE / 20)  # RATE / number of updates per second


def soundplot(stream):
    t1 = time.time()
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    print(data)


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    print(sd.query_devices())
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    outStream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, output=True, output_device_index=6,
                       frames_per_buffer=CHUNK)
    for i in range(sys.maxsize ** 10):
        # soundplot(stream)
        outStream.write(stream.read(1))
    stream.stop_stream()
    stream.close()

    outStream.stop_stream()
    outStream.close()
    p.terminate()
