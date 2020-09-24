from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os

use_step_matcher("re")


@given("Se establece URL base con sus parametros de autentificación\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Se establece el parametro necesario para Crear la Categoría\.")
def step_impl(context):

    params = GeneratorDataParameters()
    description = params.description()
    name = params.name()
    context.payload = {}
    context.url = (context.url_base+'/wp-json/wp/v2/categories?name='+name+'&description='+description)


@when("Se realiza una petición POST\.")
def step_impl(context):

    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.category_data = response.json()
    context.category_id = context.category_data["id"]
    context.code = response.status_code


@then("Se Confirma estado 201 \(Categoría Creada\)\.")
def step_impl(context):

    assert context.code == 201


@given("Se establece el parametro necesario para recuperar la categoria\.")
def step_impl(context):
    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/pages/' + str(context.category_id)


@when("Se recupera la Categoría con una petición GET\.")
def step_impl(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.category_retrieve = response.json()
    context.category_code = response.status_code


@then("Se confirma datos de la categoría creada")
def step_impl(context):
    assert context.category_code == 200
    assert context.category_retrieve["id"] == context.category_data["id"]
    assert context.category_retrieve["description"] == context.category_data["description"]
    assert context.category_retrieve["name"] == context.category_data["name"]
    assert context.category_retrieve["curies"]["templated"] == context.category_data["curies"]["templated"]
    assert context.category_retrieve["curies"]["name"] == context.category_data["curies"]["name"]
    assert context.category_retrieve["taxonomy"] == context.category_data["taxonomy"]
    assert context.category_retrieve["slug"] == context.category_data["slug"]
    assert context.category_retrieve["ping_status"] == context.category_data["ping_status"]


@given("Se establece el parametro para actualizar la Categoría\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se actualiza Categoría con una petición PUT\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 200 \(Categoría actualizada\)\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se recupera Categoría con petición GET")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se confirma datos de la categoría actualizada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Se establece parametros para eliminar la Categoría\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se elimina Categoría con una petición DELETE\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 200 Categoría Eliminada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Con petición GET se prueba a recuperar la categoría eliminada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se Confirma estado 404 Categoría No encontrada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass