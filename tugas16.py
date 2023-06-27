from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Menjalankan Web Browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

# Membuka Website Shopee

# Membuka Website Shopee
browser.get('https://shopee.co.id/buyer/login?next=https%3A%2F%2Fshopee.co.id%2F')

# Interaksi Otomatis

