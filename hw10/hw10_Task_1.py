import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class presence_of_N_elements_located:
    def __init__(self, count, locator):
        self.count = count
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.count:
            return elements


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('http://10.0.88.116/ow/')
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 5)
    return wait


@pytest.fixture
def user_cooke(driver):
    return driver.add_cookie({
        'domain': '10.0.88.116',
        'httpOnly': True,
        'name': '46fc3f05bb147800e59d399caeaede40',
        'path': '/',
        'secure': False,
        'value': 'k06mc7e4fd0m5esog06p3icmd1'
    })


def get_post_txt(post):
    # два варианта отображения даты в сообщении
    post = post.text.split()
    if 'within' in post:
        return ' '.join(post[1:-5])
    else:
        return ' '.join(post[1:-4])


def get_post_user(post):
    return str(post.text.split()[0])


def find_first_visible(elements):
    for el in elements:
        if el.is_displayed():
            return el


def param_file(filename):
    with open(filename, "r", encoding="utf-8") as user_file:
        user_list = [tuple(li.split(';')) for li in user_file.readlines()]
        return user_list


test_params = param_file("C:\\test_file\\Users_reg.txt")

@pytest.mark.parametrize('username, email, password, realname, date', test_params,
                         ids=['Reg ' + i[3] for i in test_params])
def test_user_reg(driver, wait, username, email, password, realname, date):

    driver.find_element_by_xpath("//a[@class='ow_console_item_link']").click()
    assert wait.until(es.element_to_be_clickable((By.NAME, 'joinSubmit')))
    find_first_visible(driver.find_elements(By.XPATH, '//input[contains(@class, "username")]')).send_keys(username)
    find_first_visible(driver.find_elements(By.XPATH, '//input[contains(@class, "email")]')).send_keys(email)
    find_first_visible(driver.find_elements(By.XPATH, '//input[@name = "password"]')).send_keys(password)
    pass_rep = find_first_visible(driver.find_elements(By.XPATH, '//input[@name = "repeatPassword"]'))
    pass_rep.send_keys(password)
    pass_rep.send_keys(Keys.TAB)
    driver.switch_to_active_element().send_keys(realname)
    find_first_visible(driver.find_elements(By.XPATH, '//input[@type="radio" and @value="1"]')).click()
    b_day = Select(find_first_visible(driver.find_elements(By.XPATH, '//select[contains(@name, "day_")]')))
    b_month = Select(find_first_visible(driver.find_elements(By.XPATH, '//select[contains(@name, "month_")]')))
    b_year = Select(find_first_visible(driver.find_elements(By.XPATH, '//select[contains(@name, "year_")]')))
    date_list = date.split('.')
    b_day.select_by_visible_text(date_list[0])
    b_month.select_by_value(date_list[1])
    b_year.select_by_visible_text(date_list[2])
    driver.find_element(By.NAME, 'joinSubmit').click()
    wait.until(es.element_to_be_clickable((By.XPATH, "//textarea")))
    owl_user = driver.find_element_by_css_selector(".ow_console_dropdown_hover a.ow_console_item_link")
    assert owl_user.text == realname, 'login error'


test_params = param_file("C:\\test_file\\Users_login.txt")


@pytest.mark.parametrize('user, password', test_params, ids=['Login ' + i[0] for i in test_params])
def test_login(driver, wait, user, password):
    driver.find_element_by_class_name('ow_signin_label').click()
    driver.find_element(By.NAME, "identity").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()
    assert wait.until(es.element_to_be_clickable((By.XPATH, "//textarea"))), 'user page load error'
    owl_user = driver.find_element_by_css_selector(".ow_console_dropdown_hover a.ow_console_item_link")
    assert owl_user.text == user, 'login error'

    # Использовать после добавления чтения куков из файла
    # with open('C:\\test_file\\brow\\cookies3.info', "w") as cookies:
    #    cookies.write(str(driver.get_cookies()))


@pytest.mark.parametrize('comment', [('eng comment 1'), ('Русский коммент 1')],
                         ids=['Post ENG comment', 'Post RUS Comment'])
def test_post_create(driver, wait, user_cooke, comment):
    # авторизация по кукам
    driver.refresh()
    wait.until(es.element_to_be_clickable((By.XPATH, "//textarea")))
    posts = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
    assert len(posts) == 10
    driver.find_element(By.XPATH, "//textarea").send_keys(comment)
    driver.find_element(By.NAME, "save").click()
    assert wait.until(presence_of_N_elements_located(11, (By.CLASS_NAME, "ow_newsfeed_body"))), \
        "Not 11 elements located"
    last_message = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")[0]
    last_message_text = get_post_txt(last_message)
    assert comment == last_message_text, 'last message not found on page'


def test_last_post_delete(driver, wait, user_cooke):
    # авторизация по кукам
    driver.refresh()
    wait.until(es.element_to_be_clickable((By.XPATH, "//textarea")))
    posts = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
    assert len(posts) == 10

    first_post = posts[0]
    current_user = driver.find_element_by_css_selector(".ow_console_dropdown_hover a.ow_console_item_link").text
    assert get_post_user(first_post) == current_user, "Last post from unknown user, you can't delete it!"

    del_post_text = get_post_txt(first_post)

    act = ActionChains(driver)
    act.move_to_element(first_post)
    first_post_menu = first_post.find_element(By.XPATH, "//span[contains(@class,'ow_context_more')]")
    act.move_to_element(first_post_menu).perform()
    del_button = first_post_menu.find_element(By.XPATH, "//a[contains(@class,'newsfeed_remove_btn owm_red_btn')]")
    driver.execute_script("arguments[0].click();", del_button)
    driver.switch_to.alert.accept()

    driver.refresh()
    wait.until(es.element_to_be_clickable((By.XPATH, "//textarea")))
    posts = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_body")
    assert del_post_text != get_post_txt(posts[0])

