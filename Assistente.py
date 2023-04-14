import serial
import time
import speech_recognition as sr
def ascolta():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pronuncia 'on' per accendere il LED o 'off' per spegnerlo.")
        print("Pronuncia 'esci' per uscire.")
        try:
            audio = r.listen(source)
            texto = r.recognize_google(audio, language='it-IT')
            print("Tu: " + texto)
            return texto.lower()
        except sr.UnknownValueError:
            print("Assistente: non ti capisco. Puoi ripeterlo?")
        except sr.RequestError:
            print("Assistente: si è verificato un errore nella connessione con il riconoscimento vocale")

def inviare_comando_arduino(comando):
    try:
        puerto_seriale = serial.Serial('COM3', 9600)  # il com3 dipende dalla nostra porta seriale di arduino
        time.sleep(2)  # tempo di 2 secondi per stabilire la conessione 
        puerto_seriale.write(comando.encode())  # invia il comando a arduino
        puerto_seriale.close()  # Chiude la porta seriale 
    except Exception as e:
        print("Error al enviar el comando a Arduino:", e)

def main():
    print("Ciao! Sono un assistente virtuale per controllare un LED con comandi vocali.")
    print("Pronunciare 'on' per accendere il LED o 'off' per spegnerlo.")
    print("Pronuncia 'esci' per uscire.")

    while True:
        comando = ascolta()
        if comando == 'esci':
            print("Arrivederci!")
            break
        elif comando == 'on':
            inviare_comando_arduino('1')
            print("Assistente: LED acceso.")
        elif comando == 'off':
            inviare_comando_arduino('0')
            print("Assistente: LED spento.")
        else:
            print("Assitente: comando non riconosciuto. Riprova.")

if __name__ == "__main__":
    main()
