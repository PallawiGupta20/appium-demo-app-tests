from appium.webdriver.common.appiumby import AppiumBy

PRODUCT_NAME = "Sauce Labs Backpack"


def test_app_launches(driver):
    assert driver.current_package == "com.saucelabs.mydemoapp.rn"


def test_product_list_visible(driver):
    products = driver.find_elements(
        AppiumBy.XPATH, f'//android.widget.TextView[@text="{PRODUCT_NAME}"]'
    )
    assert len(products) > 0, f"Expected to see '{PRODUCT_NAME}' product on home screen"


def test_open_product_details(driver):
    product = driver.find_element(
        AppiumBy.XPATH, f'//android.widget.TextView[@text="{PRODUCT_NAME}"]'
    )
    product.click()

    add_to_cart = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
    assert add_to_cart.is_displayed()


def test_add_product_to_cart(driver):
    product = driver.find_element(
        AppiumBy.XPATH, f'//android.widget.TextView[@text="{PRODUCT_NAME}"]'
    )
    product.click()

    add_to_cart = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Add To Cart button")
    add_to_cart.click()

    driver.back()
    # Cart icon shows a badge with item count once something is added
    cart_badge = driver.find_element(
        AppiumBy.XPATH, '//android.view.ViewGroup[contains(@content-desc, "cart")]//android.widget.TextView'
    )
    assert cart_badge.text == "1"
