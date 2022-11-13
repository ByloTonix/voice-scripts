from pydub import AudioSegment
from pydub import effects

filename = input('Введите имя файла или укажите путь к нему:  ')

sound_before = AudioSegment.from_file(filename, filename[-3:])  
print('Текущая частота дискретизации:', round(sound_before.dBFS, 1))

sound_after = effects.normalize(sound_before)
print('Новая частота дискретизации:', round(sound_after.dBFS, 1), '\n')

filename = filename[:-3] + 'wav'
sound_after.export(filename, format="wav")

print('Готово! Новый файл -', filename)
