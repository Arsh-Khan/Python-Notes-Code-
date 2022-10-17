import speech_recognition as sr 
# pip install pipwin
# pipwin install pyaudio

# it takes microphone input from user and returns a string output

def takeInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ... ")
        r.pause_threshold = 1
        
        audio = r.listen(source)
    
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User Said : {query}")

    except Exception as e :
        # print(e)
        print("Say That again Please ")
        return "None"
    return query


takeInput()