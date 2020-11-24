from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_labels import CreateLabel
from lib.pages.add_category import CreateCategories
from lib.pages.add_entry import CreateEntries
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
    context.label.label_access()


@when("Dentro de la opcion, pulsa y añade los datos de una nueva etiqueta\.")
def add_data_label(context):

    context.tag_name = context.label.add_tags()


@then("Confirma en la WEB los datos de la nueva etiqueta añadida\.")
def confirm_data_added_label(context):

    found = context.label.confirm_tags_data(context.tag_name)
    assert found


@given("Usuario autorizado\. Accede al Menú Entradas \(Categorias\)")
def access_menu_post(context):

    context.cat = CreateCategories(context.driver)
    context.cat.category_access()


@when("Dentro de la opcion, pulsa y añade los datos de una nueva categoría\.")
def add_data_category(context):

    context.category_name = context.cat.add_category()


@then("Confirma en la WEB los datos de la nueva categoría añadida\.")
def confirm_data_added_category(context):

    found = context.cat.confirm_data_create_category(context.category_name)
    assert found


@given("Usuario con perfil autorizado\. Accede al Menú Entradas \(Nueva Entrada\)")
def access_menu_post(context):

    context.entry = CreateEntries(context.driver)
    context.entry.entry_access()


@when("Dentro de la opcion, pulsa y añade los datos de una nueva entrada (?P<img>.+), (?P<categoria>.+), (?P<etiqueta>.+)\.")
def step_impl(context, img, categoria, etiqueta):

    values = {"img": img, "categoria": categoria, "etiqueta": etiqueta}
    context.entry.add_new_entry(values)



@then("Confirma en la WEB los datos de la nueva entrada añadida\.")
def confirm_data_added_entry(context):
    """
    :type context: behave.runner.Context
    """
    pass


