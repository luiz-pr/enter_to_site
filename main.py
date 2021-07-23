# This is my library with Python
# Esta é a minha Biblioteca em Python
# これは私のPythonライブラリです

from selenium import webdriver
import time
import pyttsx3


# entrar no site Em portuges brazileiro

class entrarPt():
    def __init__(self) :

        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        msg_pt = 'Qual site você quer acessar?: '
        engine.setProperty("voice", voice[0].id) 

        engine.say(msg_pt)
        engine.runAndWait()

        time.sleep(0)

        esc_url = input("qual o site que você quer acessar?: ")
        urlPt = esc_url
        httpsPt = f'https://www.{urlPt}.com'
        httpsPtLinkY = 'https://www.youtube.com/?persist_gl=1&gl=BR'

        
        driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        if urlPt == 'youtube' :
            driver.get(httpsPtLinkY)
        else:
            driver.get(httpsPt)
        print(httpsPt)
        time.sleep(20)
        driver.quit()



# Enter the site in English United States

class entrarEn():
    def __init__(self) :

        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        msg_en = 'which site do you want to access?: '
        engine.setProperty("voice", voice[1].id) 

        engine.say(msg_en)
        engine.runAndWait()

        time.sleep(0)
       
        urlEn = str(input('which site do you want to access?: '))
        httpsEn = f'https://www.{urlEn}.com'
        httpsEnLinkY = 'https://www.youtube.com/?persist_gl=1&gl=US'

        driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        if urlEn == 'youtube' :
            driver.get(httpsEnLinkY)
        else:
            driver.get(httpsEn)
        print(httpsEn)
        time.sleep(20)
        driver.quit()

# 日本語でサイトに入る

class entrarJp():
    def __init__(self) :

        engine = pyttsx3.init()
        voice = engine.getProperty('voices')
        msg_jp = 'どのサイトにアクセスしますか？：'
        engine.setProperty("voice", voice[2].id) 
        engine.setProperty("rate", 178)

        engine.say(msg_jp)
        engine.runAndWait()

        time.sleep(0)

        urlJp = str(input('どのサイトにアクセスしますか？：'))
        httpsJp = f'https://{urlJp}.com/jp'
        httpsJpLinkY = 'https://www.youtube.com/?persist_gl=1&gl=JP'

        driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        if urlJp == 'youtube' :
            driver.get(httpsJpLinkY)
        else :
            driver.get(httpsJp)
        print(httpsJp)
        time.sleep(20)
        driver.quit()


class setLang() :
    def __init__(self) :
        self.setCountry = str(input('Set Your country: '))

        if self.setCountry == 'Brazil' or self.setCountry == 'Brazil' or  self.setCountry == 'bRazil' or  self.setCountry == 'brAzil' or  self.setCountry == 'braZil' or  self.setCountry == 'brazIl' or  self.setCountry == 'braziL' or  self.setCountry == 'BRAZIL' or  self.setCountry == 'BR' or  self.setCountry == 'bR' or  self.setCountry == 'Br':
            
            engine = pyttsx3.init()
            voice = engine.getProperty('voices')
            print(f"===================================")
            msg_voice_one = "Ok Vou traduzir para você!"
            msg_voice_two = "Traduzido Para Português Brasileiro!"

            engine.setProperty("voice", voice[0].id) # 2 is the 3rd item index
            engine.say(msg_voice_one)
            print(msg_voice_one)

            engine.runAndWait()

            time.sleep(3)
            engine.say(msg_voice_two)
            print(msg_voice_two)

            engine.runAndWait()

            entrarPt()

        elif self.setCountry == 'United states' or self.setCountry == 'United States' or self.setCountry == 'united states' or self.setCountry == 'US' or self.setCountry == 'U.S' or self.setCountry == 'us' or self.setCountry == 'u.s' or self.setCountry == 'English' or self.setCountry == 'english' :
            
            engine = pyttsx3.init()
            voice = engine.getProperty('voices')
            print(f"===================================")
            msg_voice_one = "Ok I'll translate for you!"
            msg_voice_two = "Translated to English United States"

            engine.setProperty("voice", voice[1].id) # 2 is the 3rd item index
            engine.say(msg_voice_one)
            print(msg_voice_one)

            engine.runAndWait()

            time.sleep(3)
            engine.say(msg_voice_two)
            print(msg_voice_two)

            engine.runAndWait()

            entrarEn()
        
        elif (self.setCountry == '日本語'
         or self.setCountry == 'にほんご'
          or  self.setCountry == 'ニホンゴ'
            or self.setCountry == 'nihongo'
             or self.setCountry == 'Japanese'
              or self.setCountry == 'japanese'
               or self.setCountry == 'Japones'
                or self.setCountry == 'japones'
                 or self.setCountry == 'JP'
                  or self.setCountry == 'jp'
                   or self.setCountry == 'Jp'
                    or self.setCountry == 'jP') :
            
            engine = pyttsx3.init()
            voice = engine.getProperty('voices')
            print(f"===================================")
            msg_voice_one = "わかりました,  わたし  わ あなた  の  ため  に  ほん'やく  します！"
            msg_voice_two = "にほんご  に  ほん'やく"
            
            engine.setProperty("voice", voice[2].id) # 2 is the 3rd item index
            engine.say(msg_voice_one)
            print(msg_voice_one)

            engine.runAndWait()

            time.sleep(3)
            engine.setProperty("voice", voice[2].id)
            engine.say(msg_voice_two)
            print(msg_voice_two)

            engine.runAndWait()
            entrarJp()


setLang()

