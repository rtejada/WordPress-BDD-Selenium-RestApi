from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_new_users import AddNewUsers
from requests.auth import HTTPBasicAuth
import requests
import os

use_step_matcher("re")


@given("Un usuario con credenciales de administración asignados\.")
def load_arguments(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    #carga opciones de google chrome.
    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)

    #carga conección Api.
    context.user_api = os.getenv('USER_API')
    context.password_api = os.getenv('PASS_API')
    context.url_base = os.getenv('URL_BASE')


@step("Inicia sesion en la web\.")
def login_website(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Un usuario con perfil autorizado\. Accede al Menú Usuarios \(añadir nuevo\)")
def access_to_user_menu(context):

    context.user = AddNewUsers(context.driver)
    context.user.load_user_window()


@when("Dentro de la opcion, añade los datos del nuevo usuario: (?P<role>.+), (?P<name>.+)")
def add_new_users_data(context, role, name):

    user_register = {'role': role, 'name': name}
    context.user_name = context.user.new_users_data(user_register)


@then("Confirmar en la WEB los datos del nuevo usuario añadido\.")
def confirm_details_added_website(context):

    found = context.user.confirm_web_added_data(context.user_name)
    assert found


@step("Confirmar en la BBDD los datos del nuevo usuario añadido\.")
def confirm_details_added_database(context):

    found = context.user.confirm_database_added_data(context.user_name)
    assert found


@step("API-Recuperar Usuario Creado con una petición GET\.")
def recover_user_created_GET_request(context):

    query_results = context.user.get_database()

    context.payload = {}
    url = context.url_base + 'users/' + str(query_results[0])
    response = requests.get(url, auth=HTTPBasicAuth(context.user_api, context.password_api), data=context.payload)
    context.user_data_retrieve = response.json()
    context.code = response.status_code

    assert context.code == 200
    assert context.user_data_retrieve["id"] == query_results[0]

