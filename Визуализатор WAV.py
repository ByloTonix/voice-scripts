from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

filename = input('Введите имя файла или укажите путь к нему (только .wav):  ')

samplerate, data = read(filename)
print('Частота звука:', samplerate/1000, 'кГц')

duration = len(data)/samplerate
print("Продолжительность аудио в секундах/минутах: ", duration,'/',duration/60)
time = np.arange(0,duration,1/samplerate)

plt.figure(figsize=(10,5))
plt.plot(time,data)
plt.xlabel('Время, с')
plt.ylabel('Амплитуда, Гц')
plt.title('Аудиофайл ' + filename)
plt.show()
