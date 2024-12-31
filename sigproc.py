import wave
import struct
import matplotlib.pyplot as plt

sound = wave.open('test2.wav', 'rb')
left = [sound.getnframes()/2]
right = [sound.getnframes()/2]
xscale = [sound.getnframes()/2]
print(sound.getparams())
for i in range(0, sound.getnframes()-1, 1):
    bytearray_obj_left = bytearray(sound.readframes(1)[:2])
    bytearray_obj_right = bytearray(sound.readframes(1)[:-2])  # example bytearray
    sound.setpos(i+1)
    float_val_left = struct.unpack('h', bytearray_obj_left)[0]  # convert bytearray to float
    float_val_right = struct.unpack('h', bytearray_obj_right)[0]  # convert bytearray to float
    left.append(float_val_left)
    right.append(float_val_right)
    xscale.append(i+1)

print(left)
print(right)

plt.plot(xscale, left, label='left')
plt.legend()
plt.show()