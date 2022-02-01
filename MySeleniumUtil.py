import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


def send_answer(browser, step, answer, login, password):
    
    browser.implicitly_wait(606060606060)
    browser.get("https://stepik.org/catalog?auth=login")
    browser.find_element_by_id("id_login_email").send_keys(login)
    browser.find_element_by_id("id_login_password").send_keys(password)
    browser.find_element_by_css_selector("button.sign-form__btn.button_with-loader").click()
    browser.find_element_by_css_selector("button.navbar__profile-toggler")

    browser.get(step)
    text_ans = browser.find_element_by_css_selector("textarea.ember-text-area")
    browser.execute_script("return arguments[0].scrollIntoView(true);", text_ans)
    text_ans.send_keys(answer)
    browser.find_element_by_css_selector("button.submit-submission").click()

def get_answer(browser):

    browser.implicitly_wait(5)

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("solve").click()

    alert_answer = browser.switch_to.alert
    answer = alert_answer.text
    answer = answer.split(': ')[-1]
    alert_answer.accept()

    return answer
