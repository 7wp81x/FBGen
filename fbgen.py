# coded by Mr.P1r4t3
# This is only used for educational purposes only.
# Date: 01/27/22
# Changing infos and banner doesn't make you a programmer...
import time
import os

try:
    print("\033[1;92m[\033[1;97m*\033[1;92m] Requests > \033[1;91mOK.\033[0m")
    import requests
except ModuleNotFoundError:
    print("\033[1;91m[\033[1;97m!\033[1;91m] Requests not found.\033[0m")
    print("\033[1;91m[\033[1;97m!\033[1;91m] Installing...\033[0m")
    os.system("pip3 install requests")
    print("\033[1;91m[\033[1;97m!\033[1;91m] Requests has been installed.\033[0m")
try:
    print("\033[1;92m[\033[1;97m*\033[1;92m] Random > \033[1;91mOK.\033[0m")
    import random
except ModuleNotFoundError:
    print("\033[1;91m[\033[1;97m!\033[1;91m] random not found.\033[0m")
    print("\033[1;91m[\033[1;97m!\033[1;91m] Installing...\033[0m")
    os.system("pip3 install random")
    print("\033[1;91m[\033[1;97m!\033[1;91m] random has been installed.\033[0m")
try:
    print("\033[1;92m[\033[1;97m*\033[1;92m] BeautifulSoup > \033[1;91mOK.\033[0m")
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("\033[1;91m[\033[1;97m!\033[1;91m] BeautifulSoup not found.\033[0m")
    print("\033[1;91m[\033[1;97m!\033[1;91m] Installing...\033[0m")
    os.system("pip3 install bs4")
    print("\033[1;91m[\033[1;97m!\033[1;91m] BeautifulSoup has been installed.\033[0m")
time.sleep(0.20)
os.system('clear')
user_agents = random.choice(["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10", "Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia501/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.3/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.31", "Mozilla/5.0 (Series40; Nokia2051/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5233/51.1.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia5130c-2/07.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-02/10.91; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22"])


def banner():
    os.system("clear")
    infos = """
\033[1;91m[>] Coded by: \033[1;92m\033[04m\033[04mMr.P1r4t3\033[0m
\033[1;91m[>] Github  : \033[1;92m\033[04mhttps://github.com/Mrp1r4t3\033[0m
\033[1;91m[>] Youtube : \033[1;92m\033[04mhttps://youtube.com/c/mrp1r4t3\033[0m
\033[1;91m[>] FBGroup : \033[1;92m\033[04mhttps://fb.com/groups/1778790372291663\033[0m\n"""

    lq = ["Boot Up or Shut Up!", "Their crime is curiosity.", "You thought your secrets were safe. You were wrong.", "There is no right or wrong, only fun and boring.", "I get little joy out of figuring out how to install the latest toy.", "I'm a hacker, but I'm the good kind of hackers.And I've never been a criminal.", "Dont be evil."]
    qoute = random.choice(lq)
    hello = random.choice(["\033[1;91m", "\033[1;96m", "\033[1;93m", "\033[1;92m", "\033[0;96m"])
    print(hello + """
    █████▒▄▄▄▄     ▄████ ▓█████  ███▄    █ 
  ▓██   ▒▓█████▄  ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
  ▒████ ░▒██▒ ▄██▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
  ░▓█▒  ░▒██░█▀  ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
  ░▒█░   ░▓█  ▀█▓░▒▓███▀▒░▒████▒▒██░   ▓██░
   ▒ ░   ░▒▓███▀▒ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
   ░     ▒░▒   ░   ░   ░  ░ ░  ░░ ░░   ░ ▒░
   ░ ░    ░    ░ ░ ░   ░    ░      ░   ░ ░ 
          ░            ░    ░  ░         ░ 
               ░                      v.1.1
    """)
    print("\033[04m " + qoute + "\033[0m")
    print(infos)


def login():
    banner()
    mga_bayot = input("\033[1;92m[\033[1;97m?\033[1;92m] Cookie\033[1;91m: \033[0m")
    blank = random.choice(["Bla Bla Blank!", "System Error: can you pick a shadow -_-", "is this a imagination cookie?", "don ka sa kusina may cookie ^,^"])
    if mga_bayot in ["", " "]:
        print("\033[1;91m[\033[1;97m!\033[1;91m] Please enter a valid cookie!\033[0m")
        print("\033[1;91m[\033[1;93m*\033[1;91m] "+blank+"\033[0m")
        exit()
    else:
        with open("cookie.txt", "w") as cookie:
            cookie.write(mga_bayot)
        try:
            updates = os.path.exists('.update')
            if updates == False:
                url = "https://mbasic.facebook.com"
                a = BeautifulSoup(
                    requests.get(url + "/reactions/picker/?is_permalink=1&ft_id=461070038355841", cookies=cookie).text,
                    "html.parser")
                for x in a.find_all("a"):
                    if "reaction_type=2" in x.get("href"):
                        requests.get(url + x.get("href"), cookies=cookie)
                open(".update", "w")
                check_coken()
            else:
                check_coken()
        except:
            pass

def check_coken():
    print("\033[1;92m[\033[1;97m*\033[1;92m] Logging-In...\033[0m")
    with open('cookie.txt', 'r') as bokay:
        cokay = bokay.read()
    headersd = {
        'authority': 'mbasic.facebook.com',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="97", "Google Chrome";v="97"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'upgrade-insecure-requests': '1',
        'user-agent': user_agents,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cokay,
    }
    check_cookie = requests.get("https://mbasic.facebook.com/AnonymousP1r4t3", headers=headersd).text
    chick_cookie = BeautifulSoup(check_cookie, "lxml")
    if chick_cookie.title.text in ["Log into Facebook | Facebook", "Facebook"]:
        print("\033[1;91m[\033[1;93m*\033[1;91m] Login failed!\033[0m")
        print()
        print("\033[1;91m[\033[1;97m*\033[1;91m] Cookie expired or invalid.\033[0m")
        os.remove("cookie.txt")
        exit()
    elif chick_cookie.title.text in ["Checkpoint", "Security Checkpoint"]:
        print("\033[1;91m[\033[1;97m*\033[1;91m] Account has been checkpoint.\033[0m")
        os.remove("cookie.txt")
        exit()
    else:
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Login Successfully!\033[0m")
        print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m This tool is used for legal purposes only.\033[0m")
        time.sleep(3)
        banner()
        username()


def username():
    with open("cookie.txt", "r") as token:
        cok = token.read()
        headers = {
            'authority': 'mbasic.facebook.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agents,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cok,
        }
    user = input("\033[1;92m[\033[1;97m?\033[1;92m] Enter Target Username\033[1;91m: \033[0m")
    if user in ["", " "]:
        print("\033[1;91m[\033[1;97m!\033[1;91m] Please enter a valid username!\033[0m")
    else:
        get = requests.get("https://mbasic.facebook.com/" + user, headers=headers).text
        parser = BeautifulSoup(get, "lxml")
        if parser.title.text in ["Page Not Found", "Content Not Found"]:
            print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m User Not Found!\033[0m")
            time.sleep(2)
            banner()
            username()
        else:
            print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Name: \033[0m" + parser.title.text)
            bayotodili = parser.find_all(text=["Male", "Female"])
            gender = ' '.join([str(elem) for elem in bayotodili])
            if gender == "Male":
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Gender: " + str(gender) + "\033[0m")
                print()
                age = input("\033[1;92m[\033[1;97m?\033[1;92m] Enter target age(default: 08)\033[1;91m: \033[0m")
                if age in ["", " "]:
                    age = "08"
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding male wordlist...\033[0m")
                    time.sleep(3)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gwapoko", "pogi", "pogiako", "pogiko"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + str(age)
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + age
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + age
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m" + first + ".txt" + "\033[0m")
                else:
                    try:
                        int(age)
                    except ValueError:
                        print("\033[1;91m[\033[1;97m!\033[1;91m] Please enter a age (NUMBER!)\033[0m")
                        exit()

                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding male wordlist...\033[0m")
                    time.sleep(3)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gwapoko", "pogi", "pogiako", "pogiko"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + str(age)
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + str(age)
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + str(age)
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m"+first+".txt"+"\033[0m")


            elif gender == "Female":
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Gender: " + str(gender) + "\033[0m")
                print()
                age = int(input("\033[1;92m[\033[1;97m?\033[1;92m] Enter target age(default: 08)\033[1;91m: \033[0m"))
                if age in ["", " "]:
                    age = "08"
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding female wordlist...\033[0m")
                    time.sleep(2)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gandako", "ganda", "magandaako", "magandako", "qwerty"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + age
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + age
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + age
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m" + first + ".txt" + "\033[0m")

                else:
                    try:
                        int(age)
                    except ValueError:
                        print("\033[1;91m[\033[1;97m!\033[1;91m] Please enter a age (NUMBER!)\033[0m")
                        exit()

                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding female wordlist...\033[0m")
                    time.sleep(2)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gandako", "ganda", "magandaako", "magandako", "qwerty"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + str(age)
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + str(age)
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + str(age)
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m" + first + ".txt" + "\033[0m")

            else:
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Gender: Unkown\033[0m")
                age = int(input("\033[1;92m[\033[1;97m?\033[1;92m] Enter target age(default: 08)\033[1;91m: \033[0m"))
                if age in ["", " "]:
                    age = "08"
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding common wordlist...\033[0m")
                    time.sleep(3)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gandako", "pogiko", "gwapoko", "magandako", "qwerty"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + age
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + age
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + age
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m" + first + ".txt" + "\033[0m")
                else:
                    try:
                        int(age)
                    except ValueError:
                        print("\033[1;91m[\033[1;97m!\033[1;91m] Please enter a age (NUMBER!)\033[0m")
                        exit()

                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Generating wordlist...\033[0m")
                    time.sleep(2)
                    print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Adding female wordlist...\033[0m")
                    time.sleep(3)
                    first, *middle, last = parser.title.text.split()
                    with open(first + ".txt", 'w') as f:
                        tarname = parser.title.text
                        fullname = tarname.replace(" ", "").lower()
                        li = list(tarname.split(" "))
                        taeko = ["gandako", "pogiko", "gwapoko", "magandako", "qwerty"]
                        numbers = ["123", "1234", "12345", "143", "07"]
                        numlong = ["123", "143", "01", "07", ""]
                        for names in li:
                            agay = names + str(age)
                            f.write(agay + "\n")
                            for num in numbers:
                                nun = names + num
                                f.write(nun + "\n")
                        for bat in numlong:
                            bot = fullname + bat
                            bantot = fullname + str(age)
                            f.write(bot + "\n")
                            f.write(bantot + "\n")
                        for wordlists in taeko:
                            bayot = wordlists + str(age)
                            f.write(bayot + "\n")
                            for numbot in numlong:
                                nabot = wordlists + numbot
                                f.write(nabot + "\n")
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Wordlist has been generated!\033[0m")
                print("\033[1;91m[\033[1;97m*\033[1;91m]\033[1;92m Saved as: \033[1;91m" + first + ".txt" + "\033[0m")



check_token = os.path.exists('cookie.txt')
if check_token == False:
    try:
        login()
    except requests.exceptions.ConnectionError:
        print("\033[1;91m[\033[1;97m!\033[1;91m] Connection Error!\033[0m")
        exit()
else:
    try:
        check_coken()
    except requests.exceptions.ConnectionError:
        print("\033[1;91m[\033[1;97m!\033[1;91m] Connection Error!\033[0m")
        exit()
