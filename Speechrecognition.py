import speech_recognition as sr

audio_file=("C:/Users/User/Downloads/audiofile.wav")
#this takes the audio file name. Note : the audio file has to be in .wav format

r=sr.Recognizer()
#initialising the recogniser

with sr.AudioFile(audio_file) as source:
    audio = r.record(source)    #First record/read the audio sample
    
try:
    print("The audio file contains"+ r.recognize_google(audio)) 
    #r.recognise basically prints the text from the audio file
except sr.UnknownValueError :
    print("The google recognizer couldnt decipher the audio file")
except sr.RequestError :
    print("Couldnt get results from the google recognizer")
    
#Note : except is a type of error which we need to raise
    
