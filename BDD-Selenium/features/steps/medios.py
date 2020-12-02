from behave import *
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_new_media import NewMedia
import os

use_step_matcher("re")


@given("Usuario con permisos de administración asignados\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    # carga argumentos de google chrome.
    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Iniciar sesion en la web\.")
def step_impl(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Usuario con permisos\. Accede a los Medios\.")
def step_impl(context):

    context.media = NewMedia(context.driver)
    context.media.access_media()
    context.media.add_new_media()



@when("En la opcion, pulsa y añade un nuevo medio\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Confirma en la WEB los medios añadidos\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass