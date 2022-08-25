import pyttsx3 
while True:
    #инициализируем механизм преобразования текста в речь
    engine = pyttsx3.init()
    #спрашиваем у пользователя текст
    text = input("Введите текст, который требуется озвучить ")
    #устанавливаем скорость чтения текста
    engine.setProperty("rate", 150)
    #преобразуем текст в речь
    engine.say(text)
    #проигрываем речь
    engine.runAndWait() 
