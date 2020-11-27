from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import winsound
from configparser import RawConfigParser
from colorama import Fore, init, deinit

init()
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
CONFIG = RawConfigParser()
CONFIG.read('config.ini')

driver_path = CONFIG.get('MAIN', 'DRIVER_LOCATION') #"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
email_inp = CONFIG.get('CREDENTIALS', 'USERNAME')
pass_inp = CONFIG.get('CREDENTIALS', 'PASSWORD')
order_link = CONFIG.get('ORDER', 'LINK')
cvv_inp = CONFIG.get('ORDER', 'CVV')
quantity = CONFIG.get('ORDER','QUANTITY') 
addr_input = CONFIG.get('ORDER', 'ADDRESS') #CNTCT1EA51B7A7EFC475992EE32A22
pay_opt_input = CONFIG.get('ORDER', 'PAYMENT') #CRD170926122609387B1E5519C47D302
bankname_input = CONFIG.get('EMIOPTIONS', 'BANK')
tenure_input = CONFIG.get('EMIOPTIONS', 'TENURE')
vou_number = CONFIG.get('ORDER', 'VOUCHER_NUMBER')
vou_pin = CONFIG.get('ORDER', 'VOUCHER_PIN')
addr_1 = int(CONFIG.get('ORDER', 'MULTIPLE_ADDRESSES_SAVED'))
frequency = 2500
duration = 2000
flag = 0
count_click = 0
def prCyan(skk):
        print(Fore.CYAN + skk)
def prRed(skk):
        print(Fore.RED + skk)
def prGreen(skk):
        print(Fore.GREEN + skk)
def prYellow(skk):
        print(Fore.YELLOW + skk)
#print(order_link)

prGreen("  _____    _______   _      _     _______              ")
prGreen(" |  __ \  |__   __| (_)    | |   |__   __|             ")
prGreen(" | |  | |    | |_ __ _  ___| | _____| | ___ _ __ ___   ")
prGreen(" | |  | |    | | '__| |/ __| |/ / __| |/ _ \ '__/ __|  ")
prGreen(" | |__| |    | | |  | | (__|   <\__ \ |  __/ |  \__ \  ")
prGreen(" |_____/     |_|_|  |_|\___|_|\_\___/_|\___|_|  |___/  ")
prGreen("                                                         ")
prGreen("                                                         ")
time.sleep(1.5)
prRed("\n\n")
prRed("  ███████ ▄█▀    ▄▄▄      █    ██▄▄▄█████▓▒█████  ▄▄▄▄   █    █▓██   ██▓")
time.sleep(0.2)
prRed("▓██   ▒██▄█▒    ▒████▄    ██  ▓██▓  ██▒ ▓▒██▒  ██▓█████▄ ██  ▓██▒██  ██▒")
time.sleep(0.2)
prRed("▒████ ▓███▄░    ▒██  ▀█▄ ▓██  ▒██▒ ▓██░ ▒▒██░  ██▒██▒ ▄█▓██  ▒██░▒██ ██░")
time.sleep(0.2)
prRed("░▓█▒  ▓██ █▄    ░██▄▄▄▄██▓▓█  ░██░ ▓██▓ ░▒██   ██▒██░█▀ ▓▓█  ░██░░ ▐██▓░")
time.sleep(0.2)
prRed("░▒█░  ▒██▒ █▄    ▓█   ▓██▒▒█████▓  ▒██▒ ░░ ████▓▒░▓█  ▀█▒▒█████▓ ░ ██▒▓░")
time.sleep(0.2)
prRed(" ▒ ░  ▒ ▒▒ ▓▒    ▒▒   ▓▒█░▒▓▒ ▒ ▒  ▒ ░░  ░ ▒░▒░▒░░▒▓███▀░▒▓▒ ▒ ▒  ██▒▒▒ ")
time.sleep(0.2)
prRed(" ░    ░ ░▒ ▒░     ▒   ▒▒ ░░▒░ ░ ░    ░     ░ ▒ ▒░▒░▒   ░░░▒░ ░ ░▓██ ░▒░ ")
time.sleep(0.2)
prRed(" ░ ░  ░ ░░ ░      ░   ▒   ░░░ ░ ░  ░     ░ ░ ░ ▒  ░    ░ ░░░ ░ ░▒ ▒ ░░  ")
time.sleep(0.2)
prRed("      ░  ░            ░  ░  ░                ░ ░  ░        ░    ░ ░     ")
time.sleep(0.2)
prRed("                                                       ░        ░ ░     ")

url = order_link

prRed("Opening Link in chrome..........")
prCyan("\n")

print('\nLogging in with username:',email_inp)
prYellow("\n")
if pay_opt_input == 'EMI_OPTIONS':
    print('\nEMI Option Selected. \nBANK:',bankname_input,'\nTENURE:',tenure_input,'\n')
elif pay_opt_input == 'PHONEPE':
    print('\nPayment with Phonepe\n')
elif pay_opt_input == 'NET_OPTIONS':
    print('\nNet Banking Payment Selected\n')
elif pay_opt_input == 'COD':
    prGreen("COD selected\n")
elif pay_opt_input == 'GC':
    prGreen("GiftCard Payment Selected")
else:
    print('\nFull Payment Selected\n')
    

driver = webdriver.Chrome(driver_path, options=options)
driver.maximize_window()
driver.get(url)

prCyan("\n")

input('Confirm Payment Details above, Product Details on Browser & Press Enter to proceed.')

def login():
    try:
        prYellow("Logging In..\n")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._34niwY"))
            )
            prYellow('Login Button Clickable\n')
        except:
            prYellow('Login Button Not Clickable\n')
        login.click()
        prYellow('Login Button Clicked Successfully\n')
    except:
        prRed('login Failed. Retrying.')
        time.sleep(0.5)    
        login()
        
def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector(".Km0IJL ._2zrpKA")
            passd = driver.find_element_by_css_selector(".Km0IJL ._3v41xv")
            email.clear()
            passd.clear()
            email.send_keys(email_inp)
            passd.send_keys(pass_inp)
            try:
                form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".Km0IJL ._7UHT_c"))
                )
                prCyan('Submit Button Clickable')
            except:
                prRed('Submit Button Not Clickable')
            form.click()
            prYellow("\nPress any key when login is done and your name appeares in menu bar.")
            input()
            prGreen("\nLogged in successully.")
            prRed('\n')
            #input("Click Login on page and then enter here")
#        else:
#            print('Trying Alternate method of Login.')
#            email = driver.find_element_by_css_selector("._2zrpKA")
#            email.clear()
#            email.send_keys(email_inp)
#            loginnext = WebDriverWait(driver, 5).until(
#                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
#                        )
#            loginnext.click()
#            loginpassword = WebDriverWait(driver, 5).until(
#                            EC.element_to_be_clickable((By.CSS_SELECTOR, ".jUwFiZ"))
#                        )
#            loginpassword.click()
#            time.sleep(0.5)
#            passd = driver.find_elements_by_css_selector("._2zrpKA")[1]
#            passd.clear()
#            passd.send_keys(pass_inp)
#            form = WebDriverWait(driver, 20).until(
#                            EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
#                        )
#            form.click()
#        print("Logged In Successfully")
    except:
        if ('Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source):
           print('Logged in Manually.')
        else:
           prRed('login_submit Failed. Please login manually.')
           time.sleep(1)
           login_submit()

def buy_check():
    global count_click
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector("._1k1QCg ._7UHT_c")
                if buyprod.is_enabled():
                    prYellow('Buy Button Clickable')
                    buyprod.click()
                    nobuyoption = False
                else:
                    nobuyoption = True
                    count_click += 1
                    print('Buy button is disabled. Retrying ' + str(count_click), end='\r')
            except:
                nobuyoption = True
                count_click += 1
                print('Buy Button Not Active. Retrying ' + str(count_click), end='\r')
        prYellow('Buy Button Clicked Successfully')
        buy_recheck()
    except:
        prRed('buy_check Failed. Retrying.')
        time.sleep(0.5)    
        buy_check()
        
def buy_recheck():        
    try:
        WebDriverWait(driver, 10).until(
            EC.title_contains("Secure Payment")
        )        
        prYellow('Redirected to Payment')
    except:
        prRed('Error in Redirecting to Payment')
        time.sleep(0.5)    
        buy_check()
        
def deliver_option():
    try:
        addr_input_final = "//label[@for='"+addr_input+"']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH,addr_input_final))
            )
            prYellow('Address Selection Button Clickable')
        except:
            prRed('Address Selection Button Not Clickable')    
        sel_addr.click()
        prYellow('Address Selection Button Clicked Successfully')
    except:
        prRed('deliver_option Failed. Retrying.')
        #time.sleep(0.5)    
        deliver_option()
    
def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
                )
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                winsound.Beep(frequency, duration)
                print('Address Delivery Button Not Clickable')
        flag = 0
        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')
        #time.sleep(0.5)    
        deliver_continue()
        
def order_summary_continue():
    global flag
    try:
        #if( flag == 0):
         #   try:
         #       flag = 1
         #       txt_quantity = driver.find_element_by_css_selector("._2csFM9")
         #       txt_quantity.clear()
         #       txt_quantity.send_keys(quantity)
                #print("Quantity updated")
                #prGreen("Quantity updated\n")
         #   except:
         #       prRed("Sorry... Quantity is limited by flipkart. Setting value to one again\n")
        press_continue =  driver.find_element_by_css_selector("._2Q4i61")
        #press_continue = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._2Q4i61 ._7UHT_c")))
        press_continue.click()
        #input("Press key")
        prYellow('Continue Button Clicked Successfully')
    except:
        #input("press key")
        prRed('order_summary_continue Failed. Retrying.')
        #time.sleep(0.2)    
        order_summary_continue()
        
def choose_payment():
    try:
        if pay_opt_input == 'GC':
            pay_opt_input_final = "//label[@for='EGV']"
        else:
            pay_opt_input_final = "//label[@for='"+pay_opt_input+"']"
        pay_method_sel = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, pay_opt_input_final)) )
        pay_method_sel.click()
        if pay_opt_input == 'COD':
                winsound.Beep(frequency, duration)
                cod_captcha()
        elif pay_opt_input == 'PHONEPE':
                phonepe()
        elif pay_opt_input == 'GC':
                gc()
        else:
                prGreen("\nCard selected...")
                payment_cvv()
                payment_continue()
                otp_submit()
        #print(driver.find_element_by_xpath("//label[@for='COD']//input[1]").get_attribute("id"))
        #capImg = driver.find_element_by_css_selector(".AVMILy")
        #print(capImg.get_attribute("src"))
        #driver.find_element_by_xpath("//label[@for='COD']//input[1]").click()
        #if pay_opt_input == 'COD':
        #        emi_button = WebDriverWait(driver, 5).until(
        #        EC.presence_of_element_located((By.XPATH, "//label[@for='COD']//input[1]"))
        #        )
        #        print(emi_button.get_attribute("type"))
        #        input("key")
        #        emi_button.click()
                #time.sleep(0.5)
            #card_name = WebDriverWait(driver, 5).until(
             #       EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "'+bankname_input+'")]')) )
            #card_name.click()
            #time.sleep(0.5)
            #emi_tenure = WebDriverWait(driver, 5).until(
             #   EC.element_to_be_clickable((By.XPATH, "//label[@for='"+tenure_input+"']")) )
            #emi_tenure.click()
            #time.sleep(0.5)
         #       continue_emi = WebDriverWait(driver, 5).until(
         #       EC.presence_of_element_located((By.CSS_SELECTOR, "._7UHT_c"))
         #       )
         #       continue_emi.click()
        prGreen('Payment Method Selected Successfully')
        winsound.Beep(frequency, duration)
    except:
        prRed('choose_payment Failed. Retrying.')
        time.sleep(0.5)    
        choose_payment()

def gc():
    try:
        gc_btn = driver.find_element_by_css_selector("._26gfbJ")
        vouNum = driver.find_element_by_name("voucherNumber")
        vouNum.clear()
        vouNum.send_keys(vou_number)
        vouPin = driver.find_element_by_name("voucherPin")
        vouPin.clear()
        vouPin.send_keys(vou_pin)
        gc_btn.click()
    except:
        print("Giftcard option not selected. Retrying")
        time.sleep(0.5)
        gc()

def cod_captcha():
        try:
                payment_sel = None
                payment_sel = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._16qL6K")))
                payment_sel.clear()
                prYellow("Type the captcha here:")
                capText = input()
                payment_sel.send_keys(capText)
                prGreen("\nCaptcha entered successfully.")
                prYellow("\nClicking Confirm Button order:")
                confirm_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._7UHT_c")))
                confirm_btn.click()
                prGreen("\nOrder confirmed successfully")
        except:
                prRed("\nCaptcha could not be selected. Retrying")
                #time.sleep(0.2)
                cod_captcha()
                


def phonepe():
        try:
                
                prYellow("Continuing with phonepe...")
                phonepe_con = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "._7UHT_c")))
                phonepe_con.click()
                prYellow("Choose QR code mode for quicker payment")
                #phn_txt.click()
        except:
                prRed("Could not enter number")

def payment_cvv():
    try:
        payment_sel =  None
        payment_sel = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._16qL6K"))
        )
        payment_sel.clear()
        payment_sel.send_keys(cvv_inp)
        print('CVV Entered:'+cvv_inp)
    except:
        print('payment_cvv Failed. Retrying.')
        #time.sleep(0.5)    
        #payment_cvv()
        
def payment_continue():
    try:
        pay =  None
        try:
            pay = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
            )
            print('Pay Button Clickable')   
        except:
            print('Pay Button Not Clickable')        
        pay.click()
        print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')
        #time.sleep(0.5)    
        #payment_continue()
        
def otp_submit():
    try:
        otp = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ .l5dwor"))
            )
        otp.clear()
        print('Please enter OTP here:')
        otp_input = input()    
        otp.send_keys(otp_input)
                    
        submit_otp = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
            )
        submit_otp.click()
        print('OTP Submitted Successfully')
    except:
        print('otp_submit Failed. Retrying.')
        time.sleep(0.5)    
        otp_submit()

def try_till_otp():       
    login()
    login_submit()
    buy_check()
    if addr_1 == 1:
        deliver_option()
        deliver_continue()
    order_summary_continue()
    choose_payment()
    #payment_cvv()
    #payment_continue()
    #otp_submit()

if __name__ == "__main__":
    try_till_otp()





