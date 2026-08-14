import pyttsx3
import speech_recognition as sr
import eel
import time

# Function to make Vistra speak the given text
def speak(text):
    text = str(text)
    # Set up the text-to-speech engine using Windows' built-in voices
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # Choose a specific voice for Vistra
    engine.setProperty('voice', voices[1].id)
    # Set the speaking speed
    engine.setProperty('rate', 174)
    # Show the text on the interface 
    eel.DisplayMessage(text)
    # Vistra say the text out loud
    engine.say(text)
    # Send the text to the interface for display
    eel.receiverText(text)
    # Wait until Vistra finishes speaking
    engine.runAndWait()

# Function to listen for voice commands from the user
def takecommand():

    # Set up the speech recognizer
    r = sr.Recognizer()

    # Use the microphone to capture audio
    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage("listening ...")
        # Set a pause threshold to detect when the user stops speaking
        r.pause_threshold = 1
        # Adjust for background noise to improve recognition
        r.adjust_for_ambient_noise(source)
        # Listen for up to 10 seconds, with a 6-second phrase timeout
        audio=r.listen(source, 10, 6)
    try:
        print('recognizing') 
        eel.DisplayMessage('recognizing... ')
        # Convert the audio to text using Google's speech recognition
        query= r.recognize_google(audio,language= 'en-in')
        print(f"user said:{query}") 
        eel.senderText(query)
        eel.DisplayMessage(query) 
        # Display the recognized text on the interface
        # eel.DisplayMessage(query)
        # Pause briefly to keep the interface readable
        time.sleep(2)
        
    except Exception as e:
        return ""

    return query.lower()
 
@eel.expose
def allCommands(message=1):
    # If no message is provided, listen for a voice command
    if message==1:
        query = takecommand()
        # Send the recognized command to the interface
        # eel.senderText(query)
        eel.senderText(query)
        eel.DisplayMessage(query)
    else: 
        # Use the provided message as the command
        query=message
        # Send the command to the interface
        eel.senderText(query)
    try:
        
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
           
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)
        elif "search" in query or "google" in query:
            from engine.features import searchGoogle
            searchGoogle(query)
            
        else:
           # If no specific command matches, use the chatbot feature
           from engine.features import chatBot
           chatBot(query)
    except:
        print("error")    
        
    # Show the interface's main display
    eel.ShowHood()