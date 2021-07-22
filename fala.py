# import pyttsx3

robot = pyttsx3.init()

msg_robot = input('Ecreva algo: ')

robot.say(msg_robot)

robot.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# voice = voices
# msg_voice = input("diga: ")
    

# print(f"Voice: {voice}")
# engine.setProperty("voice", voices[2].id) # 2 is the 3rd item index
# engine.say(msg_voice)
#     # Hello world' in Hindi: नमस्ते दुनिया
# engine.runAndWait()


# import pyttsx3

# engine = pyttsx3.init()
# engine.say('Welcome to Medium')
# engine.runAndWait()

# engine.setProperty('rate', 150)
# engine.getProperty('volume')
# voices = engine.getProperty('voices')

# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

# engine.setProperty("voice", voices[2].id)
# engine.save_to_file("How do you do?", "output.mp3")