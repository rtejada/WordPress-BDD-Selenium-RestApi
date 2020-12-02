from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
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


@given("Usuario con permisos, accede a todas las páginas\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("En la opcion, pulsa y añade una nueva página\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se confirman los datos de la página creada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass