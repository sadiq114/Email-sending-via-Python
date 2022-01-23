# 1st intall three libraries namely:
# 1-pip install SpeechRecognition
# 2a-pyaudio. Its a supporive library for speehcregonition library.You caanot
# install this library through pip install command. For its installtion, 1st you
# have to another python manager "pipwin". Its just like pip manager.So 1st install
# it using the same pip install command i.e., >>pip install pipwin
# 2b-Now you can install pyaudio using the same command install but not with pip
# but instead pipwin i.e., >>pipwin install pyaudio
# 3-yagmail is th 3rd library you have to install, i.e., >>pip install yagmail

# Now write your code but 1st part is always importing of libraries, so

import speech_recognition as sr
import yagmail

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing the background Noise....")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message....")
    recorderaudio = recognizer.listen(source)
    print("Done recording!")
try:
    print("Printing the message....")
    text = recognizer.recognize_google(recorderaudio,language='en-US')

    print('Your message:{}'.format(text))
except Exception as ex:
    print(ex)

# Automatic mails:
receiver='sadiqakbar@uop.edu.pk'
message=text
sender=yagmail.SMTP('sadiq114@gmail.com')
sender.send(to=receiver,subject='This is an automatic mail',contents=message)
print("Your email was sent successfully")
    
