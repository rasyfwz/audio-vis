from scipy.io.wavfile import read
import matplotlib.pyplot as plt

input = read("test2.wav")
print(input)
audio = input[1]
plt.plot(audio)
plt.show()

left = audio[1][1]
print(left)