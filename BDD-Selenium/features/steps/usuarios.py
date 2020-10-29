from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_new_users import AddNewUsers
import os

use_step_matcher("re")


@given("Un usuario con credenciales de administración asignados\.")
def load_arguments(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


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