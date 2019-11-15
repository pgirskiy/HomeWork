import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# Попробуйте запустить браузер через Selenium Server (слайд 25-28)

rm_driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                             desired_capabilities=DesiredCapabilities.CHROME)

rm_driver.get('http://google.com')
assert rm_driver.title == "Google"
rm_driver.quit()

# Поиграйтесь со всеми видами нахождения элементов и со всеми действиями.
# Повторите действие клика на выпадающее подменю с сайтом https://novaposhta.ua/

driver = webdriver.Chrome()
driver.get('https://novaposhta.ua/')
assert driver.title.startswith('Термінова і експрес доставка'), 'page title error'
wait = WebDriverWait(driver, 10)

#Найдем элементы меню
menu = driver.find_element(By.ID, "top_menu")
submenu = driver.find_element_by_partial_link_text("Відділення")
offices = driver.find_element_by_partial_link_text("Графік роботи відділень")

#переход в подменю используя ActionChains
open_office_page = ActionChains(driver)
wait.until(es.presence_of_element_located((By.ID, "top_menu")))
open_office_page.move_to_element(menu)
open_office_page.move_to_element(submenu)
wait.until(es.element_to_be_clickable((By.LINK_TEXT, "Графік роботи відділень")))
open_office_page.move_to_element(offices).click()
open_office_page.perform()

#Заполняем фильтры на странице и переходим на филиал в результатах
city_filter = driver.find_element(By.ID, "NovaPoshtaFiltersForm_city")
city_filter.send_keys('Київ')
city_filter.send_keys(Keys.DOWN)
city_filter.send_keys(Keys.RETURN)

department = driver.find_element(By.CSS_SELECTOR, "#department div.option_select").click()
set_department = driver.find_element(By.CSS_SELECTOR, "#department div.dropdown li:nth-child(3)").click()

work_time = driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div").click()
set_work_time = driver.find_element_by_xpath("//li[text()='Будні']").click()

get_f_department_inf = driver.find_element_by_xpath('//a/span[contains(text(),"просп. Перемоги")]/..')
driver.execute_script("window.scrollTo(0, 850);")
get_f_department_inf.click()

# Не разобрался касательно скрола к элементу, в списке отделений, для клика
# выбираю фильтры и хочу проскролить к элементу в средине списка
# атрибут элемента .location возвращает значения типа x:200 y:300
# скрол заканчивается неудачей, и ошибкой что элемент на самом деле на 860 позиции, а не на 300
# вариант типа такого driver.execute_script("arguments[0].scrollIntoView(true);", get_f_department_inf)
# тоже не помог, осталось только что-то вроди нажатий PAGEDOWN пока не появится видимый элемент или решений
# которые нашел но не пробовал в виду какой-то не универсальности, и не ясно так ли это, например:
# a = browser.execute_script("return outerWidth")
# c = browser.execute_script("return outerHeight - innerHeight")
# b = browser.execute_script("return outerHeight")
# loc.moveTo(location['x']*1920/a, (location['y'] + c)*1080/b, 0.1)
# вообщем пока оставил рабочий вариант с координатами прописаными руками
# ясно что не универсально, но все методы какие-то странные


#Научитесь работать с check box, radio button, select (drop-down list) прикреплять файлы
#Для select (drop-down list) воспользуйтесь классом Select со слайда 71.

driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/HTML/')

name = driver.find_element_by_css_selector('#firstname')
name.send_keys('Name1')

send_file = driver.find_element_by_xpath('//input[@type="file"]')
send_file.send_keys('C:\\test_file\\1.txt')

dropdown_1 = driver.find_element_by_css_selector('#options[name="Select list"]')
dropdown_1.find_element_by_css_selector('option:nth-child(4)').click()

dropdown_2 = Select(driver.find_element(By.ID, 'os'))
dropdown_2.select_by_visible_text('Windows XP')

#чекбокс с проверкой
checkbox_1 = driver.find_element(By.ID, "ch1")
if not checkbox_1.is_selected():
    checkbox_1.click()

driver.quit()
