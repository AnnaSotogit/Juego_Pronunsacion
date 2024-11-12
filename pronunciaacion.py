import speech_recognition as speech_recog
import random
import time

# Niveles de dificultad y palabras
niveles = {
    "facil": ["agenda", "casa", "hola"],
    "medio": ["bye", "algorithm", "bed"],
    "dificil": ["réseau neuronal", "apprentissage automatique", "inteligencia artificial"]
}

# Función para reconocer la voz del usuario
def speech(language="es-ES"):
    recog = speech_recog.Recognizer()
    mic = speech_recog.Microphone()
    
    try:
        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file)
            print("Por favor, di la palabra...")
            audio = recog.listen(audio_file, timeout=5)  # Tiempo máximo para hablar
            return recog.recognize_google(audio, language=language)
    except speech_recog.UnknownValueError:
        print("No se entendió nada, intenta de nuevo.")
        return None
    except speech_recog.RequestError:
        print("Error con el servicio de reconocimiento de voz.")
        return None
    except speech_recog.WaitTimeoutError:
        print("No has dicho nada a tiempo.")
        return None

# Función del juego
def play_game():
    print("Selecciona el nivel de dificultad: fácil, medio, difícil")
    nivel = input("Escribe el nivel: ").lower()
    
    if nivel not in niveles:
        print("Nivel no válido. Inténtalo de nuevo.")
        return
    
    palabras = niveles[nivel]
    language = {"facil": "es-ES", "medio": "en-EN", "dificil": "fr-FR"}[nivel]
    score = 0
    intentos_totales = 3

    for palabra in palabras:
        intentos = intentos_totales
        while intentos > 0:
            print(f"Tienes {intentos} intentos para decir: '{palabra}'")
            inicio = time.time()
            respuesta = speech(language)
            tiempo_transcurrido = time.time() - inicio
            
            if tiempo_transcurrido > 5:
                print("¡Se acabó el tiempo!")
                break
            
            if respuesta is None:
                intentos -= 1
            elif respuesta.lower() == palabra.lower():
                print("¡Correcto!")
                score += 1
                break
            else:
                print("Incorrecto. Inténtalo de nuevo.")
                intentos -= 1

        if intentos == 0:
            print(f"No lograste decir '{palabra}' correctamente.")
    
    if score == len(palabras):
        if nivel == "dificil":
            print("Ohhh has ganado el juego ¡FELICIDADES!")
        else:
            print("Has pasado al siguiente nivel!!!")
    else:
        print("Inténtalo de nuevo para mejorar tu puntuación:(.")
    
    print(f"Puntuación total: {score}/{len(palabras)}")

# Ejecutar el juego
if __name__ == "__main__":
    play_game()
