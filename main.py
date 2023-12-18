import pyttsx3
while True:
    text = input('Введите текст: ')
    # Создание объекта для озвучивания
    engine = pyttsx3.init()

    # Установка скорости речи
    engine.setProperty('rate', 150)

    # Озвучивание текста
    engine.say(text)

    # Воспроизведение озвученного текста
    engine.runAndWait()
