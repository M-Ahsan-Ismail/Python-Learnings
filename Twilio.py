#By Speech!
import speech_recognition as sr
import pyttsx3
from twilio.rest import Client

account_sid = 'ACfc8c79190eaf9179eb6f6ec8435355b0'
auth_token = '5fab5e3501d85bc2fa1498e552142a23'
client = Client(account_sid, auth_token)


def send_whatsapp_message(message):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message,
            to='whatsapp:+923180690159'
        )
        return message.sid
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")


def listen_for_command():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for your voice command...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            print("Audio captured, recognizing...")

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            if "send message" in command.lower():
                return True
            else:
                return False
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
    except sr.WaitTimeoutError:
        print("Listening timed out")
    except Exception as e:
        print(f"Microphone error: {e}")

    return False


def get_message():
    print("Enter your message (type and press Enter): ")
    message = input()
    return message


def voice_interaction():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    engine.say("Tell me the key.")
    engine.runAndWait()

    if listen_for_command():
        engine.say("Key recognized. Please input your message.")
        engine.runAndWait()

        message = get_message()
        if message:
            engine.say("Sending message.")
            engine.runAndWait()
            send_whatsapp_message(message)
            engine.say("Message sent successfully.")
            engine.runAndWait()
        else:
            engine.say("Failed to receive message. Please try again.")
            engine.runAndWait()
    else:
        engine.say("Wrong key. Please say 'Send message' to send a message.")
        engine.runAndWait()


voice_interaction()








