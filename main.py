import undetected_chromedriver as uc

from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import ChromeOptions

from flask import Flask, request

app = Flask(__name__)


@app.route('/request')
def get_cookie():
    url = request.args.get('url')
    options = ChromeOptions()
    options.add_argument("--headless")
    driver = uc.Chrome(use_subprocess=True, options=options)
    print('Opening URL:', url)
    driver.get(url)
    WebDriverWait(driver, 5).until(lambda d: d.get_cookie('cf_clearance'))
    cookie = driver.get_cookie("cf_clearance")
    driver.quit()
    return cookie["name"] + "=" + cookie["value"]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
