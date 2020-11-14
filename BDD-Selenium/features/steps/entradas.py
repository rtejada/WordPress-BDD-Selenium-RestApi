from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_labels import CreateLabel
from requests.auth import HTTPBasicAuth
import requests
import os

use_step_matcher("re")


@given("Usuario con credenciales de administración asignados\.")
def load_arguments(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)

    context.user_api = os.getenv('USER_API')
    context.password_api = os.getenv('PASS_API')
    context.url_base = os.getenv('URL_BASE')


@step("Inicia una sesion en la web\.")
def login_website(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Usuario con un perfil autorizado\. Accede al Menú Entradas \(Etiquetas\)")
def access_menu_post(context):

    context.label = CreateLabel(context.driver)
    context.label.access_tags()


@when("Dentro de la opcion, pulsa y añade los datos de una nueva etiqueta\.")
def step_impl(context):

    context.tag_name = context.label.add_tags()


@then("Confirma en la WEB los datos de la nueva etiqueta añadida\.")
def step_impl(context):

    found = context.label.confirm_tags_data(context.tag_name)
    assert found

