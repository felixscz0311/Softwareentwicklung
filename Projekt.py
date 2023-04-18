from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Erstelle eine neue Instanz des Firefox-Webdrivers
driver = webdriver.Firefox()

# Navigiere zur ChatGPT-Webseite
driver.get("https://app.slack.com/client/T02GDPGBL/C01HQB0TRJR")

# Warte, bis die Seite vollständig geladen ist
driver.implicitly_wait(10)

# Finde das Textfeld für die Eingabeaufforderung und gib eine Nachricht ein
input_box = driver.find_element_by_xpath('//div[@aria-label="Message #general input"]')
input_box.send_keys("Hallo ChatGPT! Wie geht es dir?" + Keys.RETURN)

# Schließe den Webbrowser
driver.quit()
