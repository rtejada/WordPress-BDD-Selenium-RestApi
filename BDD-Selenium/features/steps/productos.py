from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.login_website import LoginWebsite
from lib.pages.add_product_category import NewProductCategory
from lib.pages.add_product_tag import NewProductTag
from lib.pages.add_product_atrib import NewProductAttribute
from lib.pages.add_new_product import NewProduct
from dotenv import load_dotenv
import os


use_step_matcher("re")


@given("Usuario con permisos de administración de productos asignados\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-Selenium/features/lib/data/.env.wordpress")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion en la página web\.")
def step_impl(context):

    login = LoginWebsite(context.driver)
    login.load_page()
    login.enter_page()


@given("Usuario autorizado\. Accede al menu de productos \(categorías\)")
def step_impl(context):

    context.cat = NewProductCategory(context.driver)
    context.cat.access_page()


@when("En la opcion, pulsa y añade los datos de una nueva categoría\.")
def step_impl(context):

    context.name_category = context.cat.add_category()


@then("Confirma los datos de la nueva categoría añadida\.")
def step_impl(context):

    found = context.cat.confirm_data_category(context.name_category)
    assert found


@given("Usuario autorizado\. Accede al menú de productos \(etiquetas\)")
def step_impl(context):

    context.label = NewProductTag(context.driver)
    context.label.access_page()


@when("En la opcion, pulsa y añade los datos de una nueva etiqueta\.")
def step_impl(context):

    context.tag_name = context.label.add_tags()


@then("Confirma los datos de la nueva etiqueta añadida\.")
def step_impl(context):

    found = context.label.confirm_data_tags(context.tag_name)
    assert found


@given("Usuario autorizado\. Accede al menú de productos \(atributos\)")
def step_impl(context):

    context.attrib = NewProductAttribute(context.driver)
    context.attrib.access_attrib()


@when("En la opcion, pulsa y añade los datos de un nuevo atributo\.")
def step_impl(context):

    context.attrib_name = context.attrib.add_attrib()


@then("Confirma los datos del nuevo atributo añadida\.")
def step_impl(context):

    found = context.attrib.confirm_data_attrib(context.attrib_name)
    assert found


@given("Usuario autorizado\. Accede al menú de productos\.")
def step_impl(context):

    context.prod = NewProduct(context.driver)
    context.prod.access_product()


@when("En la opcion, pulsa y añade los datos de un nuevo producto\.")
def step_impl(context):
    tag_name = 'Eti-ezaTY85FoZ'
    context.prod_name = context.prod.add_new_product(tag_name)


@then("Confirma los datos del nuevo producto añadida\.")
def step_impl(context):

    found = context.prod.confirm_data_product(context.prod_name)
    assert found
