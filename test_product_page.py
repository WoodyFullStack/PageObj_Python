import time
import pytest

from .pages.product_page import ProductPage

baseurl = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
urls = []
for offer in range(1, 10):
    urls.append(baseurl + str(offer))

@pytest.mark.xfail
@pytest.mark.parametrize('link', urls)
def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    time.sleep(2)
    page.should_be_added_proper_item()
    page.should_be_added_item_with_proper_price()
