from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_new_page import NewPage
from dotenv import load_dotenv
import os


use_step_matcher("re")


@given("Usuario con permisos asignados\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")
    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia nueva sesion en la web\.")
def step_impl(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Usuario con permisos, accede a las páginas\.")
def step_impl(context):

    context.page = NewPage(context.driver)
    context.page.access_page()


@when("Dentro de la opcion, pulsa y añade nueva página (?P<titulo>.+)\.")
def step_impl(context, titulo):

    context.title = context.page.add_new_page(titulo)


@then("Confirma el título de la página creada\.")
def step_impl(context):

    found = context.page.confirm_data_page(context.title)
    if found:
        assert found
    else:
        print('pagina hija localizada:', context.title)
