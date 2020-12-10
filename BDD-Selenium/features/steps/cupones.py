from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from lib.pages.login_website import LoginWebsite
from lib.pages.add_cupons import Coupons
import os

use_step_matcher("re")


@given("Usuario con permisos de acceso\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion en la Website\.")
def step_impl(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Usuario autorizado\. Accede al menu marketing \(cupones\)")
def step_impl(context):

    context.coupon = Coupons(context.driver)
    context.coupon.access_marketing()


@when("En la opción, pulsa y añade un nuevo cupón\.")
def step_impl(context):

    context.title_coupon = context.coupon.add_new_coupon()


@then("Confirma los datos del nuevo cupón añadido\.")
def step_impl(context):

    found = context.coupon.confirm_data_coupons(context.title_coupon)
    assert found
