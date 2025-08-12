from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

print("🟢 Iniciando prueba de login con Selenium...")
driver = webdriver.Chrome()

try:
    print("🌐 Abriendo página de login...")
    driver.get("<<URL DE LA PAGINA>>")

    wait = WebDriverWait(driver, 10)

    # Esperar campo de usuario
    print("⏳ Esperando campo 'username'...")
    usuario_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    usuario_input.send_keys("USUARIO")

    # Esperar campo de contraseña
    print("⏳ Esperando campo 'password'...")
    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys('**********')  # ← aquí pon la real

    # Clic en el botón de login (puede necesitar ajuste si el botón es dinámico)
    print("➡️ Haciendo clic en el botón de login...")
    boton_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    boton_login.click()

    # Esperar respuesta
    print("🔍 Verificando si el login fue exitoso...")
    time.sleep(3)

    # Verificar si aparece algo que indique éxito
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'Bienvenido')]")
        print("✅ Login exitoso.")
    except NoSuchElementException:
        print("❌ Login fallido. No se encontró texto de éxito.")

    # Captura de pantalla
    print("📸 Guardando captura como 'resultado_login.png'...")
    driver.save_screenshot("resultado_login.png")

except TimeoutException:
    print("❌ Timeout: algún campo no apareció a tiempo.")
except Exception as e:
    print("❌ Error general:")
    print(e)
finally:
    print("🚪 Cerrando navegador...")
    driver.quit()
