import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from encry import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pywhatkit import sendwhatmsg
import datetime

target_datetime = datetime.datetime(2024, 5, 6, 21, 27)  # Yıl, Ay, Gün, Saat, Dakika
phone_number = "telefon numaranız"

driver = webdriver.Chrome()#webdrive başlatma
driver.get("https://lms.gazi.edu.tr/Account/LoginBefore")#istenen siteye yönlenme
driver.maximize_window()

username=driver.find_element(By.ID,"UserName") #username yazdırma
username.send_keys(str_decrypted_usernmae) #kullanıcı adını girme
username.send_keys(Keys.ENTER)#entera basama
time.sleep(5)

pasword = driver.find_element(By.NAME,"Password")#aynı işlemler şifre için
time.sleep(1)
pasword.send_keys(str_decrypted_password)
pasword.send_keys(Keys.ENTER)
time.sleep(20)

activities = driver.find_element(By.XPATH,"//a[contains(text(), 'Tümünü Göster')]") #tüm aktivitleri bulma
activities.click()
time.sleep(1)
times= driver.find_elements(By.ID,"activity-card") #zamanları bulma ve yazdırma
#print(times)
for x in times:
    print(x.text,end="\n\n")

# dersler = driver.find_element(By.XPATH,"//a[contains(text(), 'Derslerime Git')]")
# dersler.click()
time.sleep(2)

driver.back() #önceki sayfay dönüldü
time.sleep(1)#iletşim butonlarını bulma ave tıklama
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "communicationToolsButtons"))
)
element.click()
time.sleep(1)#aynısını duyurlar için yapma
duyurular = driver.find_element(By.XPATH, "//a[contains(@class, 'r_menu_announcements') and contains(text(), 'Duyurular')]")
duyurular.click()
time.sleep(5)#elementin konumu kadar beklemek için webdriver wait kullanımı
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h6/span[contains(text(), 'ENGİN ALKAN')]")))

# Tüm ilgili duyuruları bulun
announcements = driver.find_elements(By.XPATH,"//div[contains(@class,'media') and .//span[contains(text(), 'ENGİN ALKAN')]]")

# Bulunan duyurular üzerinde işlem yapın
for announcement in announcements:
    # Duyurunun başlığını yazdırın
    print("Duyuru Başlığı: ", announcement.find_element(By.XPATH, ".//h5").text)
    # Duyurunun detaylı metnini yazdırın
    detail_text = announcement.find_element(By.XPATH, ".//h6").text
    print("Duyuru Detayı: ", detail_text)
    print("-----")

#bu kısım gelişme aşamasında şuan tam değil
for a in announcements:
    sendwhatmsg(phone_number, a.text, target_datetime.hour, target_datetime.minute)

time.sleep(20)


time.sleep(120)
driver.close()


