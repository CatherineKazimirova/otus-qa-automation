from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

catalog_page = 'laptop-notebook'
product_card = 'laptop-notebook/hp-lp3065'


def test_main(open_browser):
    open_browser.get(url=open_browser.base_url)

    wait = WebDriverWait(open_browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#slideshow0 div.swiper-slide.text-center.swiper'
                                                                  '-slide-active')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#slideshow0 div.swiper-slide.text-center.swiper'
                                                                  '-slide-prev.swiper-slide-duplicate-next')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content > h3'), 'Featured'))

    product_preview = len(wait.until(EC.visibility_of_all_elements_located((
        By.CSS_SELECTOR, '#content div.row [class ^= "product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12"]'))))
    assert product_preview == 4

    footer_carousel_bullets = len(wait.until(EC.visibility_of_all_elements_located((
        By.CSS_SELECTOR, '[class ^= "swiper-pagination carousel0"] span:nth-child(n)'))))
    assert footer_carousel_bullets == 11


def test_catalog(open_browser):
    open_browser.get(url=open_browser.base_url + catalog_page)

    wait = WebDriverWait(open_browser, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#list-view')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#grid-view')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#compare-total')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.col-md-4.col-xs-6 '
                                                                  'div.form-group.input-group.input-group-sm')))

    sort_by_elements = ['[value$="sort=p.sort_order&order=ASC"]', '[value$="sort=pd.name&order=ASC"]',
                        '[value$="sort=pd.name&order=DESC"]', '[value$="sort=p.price&order=ASC"]',
                        '[value$="sort=p.price&order=DESC"]', '[value$="sort=rating&order=DESC"]',
                        '[value$="sort=rating&order=ASC"]', '[value$="sort=p.model&order=ASC"]',
                        '[value$="sort=p.model&order=DESC"]']
    for el in sort_by_elements:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, el)))

    show_elements = ['[value$="limit=15"]', '[value$="limit=25"]', '[value$="limit=50"]', '[value$="limit=75"]',
                     '[value$="limit=100"]']
    for el in show_elements:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, el)))


def test_product_card(open_browser):
    open_browser.get(url=open_browser.base_url + product_card)

    wait = WebDriverWait(open_browser, 5)

    tabs = ['[href = "#tab-description"]', '[href = "#tab-specification"]', '[href = "#tab-review"]']
    for el in tabs:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, el)))

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-original-title="Add to Wish List"]')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#button-cart')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.form-group.required > label.control-label'), 'Delivery Date'))


def test_register(open_browser):
    open_browser.get(url=open_browser.base_url + 'index.php?route=account/register')

    wait = WebDriverWait(open_browser, 5)

    continue_btn = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.pull-right input.btn.btn-primary')))
    continue_btn.click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#account div:nth-child(3) div.text-danger'),
                                                'First Name must be between 1 and 32 characters!'))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#account div:nth-child(4) div.text-danger'),
                                                'Last Name must be between 1 and 32 characters!'))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#account div:nth-child(5) div.text-danger'),
                                                'E-Mail Address does not appear to be valid!'))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#account div:nth-child(6) div.text-danger'),
                                                'Telephone must be between 3 and 32 characters!'))


def test_login(open_browser):
    open_browser.get(url=open_browser.base_url + 'index.php?route=account/login')

    wait = WebDriverWait(open_browser, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content div.row div:nth-child(2) h2'), 'Returning '
                                                                                                           'Customer'))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#content div.row div:nth-child(2) p strong'),
                                                'I am a returning customer'))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[for=input-email]'), 'E-Mail Address'))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-email')))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[for=input-password]'), 'Password'))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#input-password')))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[action$="account/login"] [type=submit]')))

