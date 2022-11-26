import time
import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

baseurl = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
urls = []
for offer in range(0, 10):
    urls.append(baseurl + str(offer))


@pytest.mark.skip
@pytest.mark.parametrize('link', urls)
def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_item_to_cart()
    time.sleep(2)
    page.should_be_added_proper_item()
    page.should_be_added_item_with_proper_price()


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_item_to_cart()
    time.sleep(2)
    page.should_be_added_proper_item()
    page.should_be_added_item_with_proper_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_disappear_success_message()


@pytest.mark.one
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_cart()
    basket_page.should_visible_message_of_empty_cart()
