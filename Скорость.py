from pydub import AudioSegment

def speed_change(sound, speed):
    global filename
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
        })
    filename = filename[-3:] + '_changed_speed' + '.wav'

    sound_with_altered_frame_rate.export(filename, format = "wav")

filename = input('Введите имя файла или укажите путь к нему:  ')
mode = input('''Что сделать со звуковым файлом?
1 - замедлить его
2 - ускорить его
Выбор: ''')
sound = AudioSegment.from_file(filename)

if mode == '1':
    speed_mode = float(input('Во сколько раз замедлить файл (0.5, 0.1, 0.99 и т.п.): '))
    slow_sound = speed_change(sound, speed_mode)
elif mode == '2':
    speed_mode = float(input('Во сколько раз ускорить файл (1.5, 2.0, 3.11 и т.п.): '))
    fast_sound = speed_change(sound, speed_mode)
else:
    print('Перезапускай теперь, ввёл что-то не то!')
