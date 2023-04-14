import pyttsx3
p = pyttsx3.init()
messaggio = "Ciao, sono il tuo Assistente Virtuale"
p.say(messaggio)
p.runAndWait()