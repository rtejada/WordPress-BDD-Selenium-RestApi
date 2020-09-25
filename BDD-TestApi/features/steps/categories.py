from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os

use_step_matcher("re")


@given("Se establece URL base con sus parametros de autentificación\.")
def authentication(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Se establece el parametro necesario para Crear la Categoría\.")
def parameters_create_page(context):

    params = GeneratorDataParameters()
    description = params.description()
    name = params.name()
    context.payload = {}
    context.url = (context.url_base+'/wp-json/wp/v2/categories?name='+name+'&description='+description)


@when("Se realiza una petición POST\.")
def request_is_made(context):

    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.category_data = response.json()
    context.category_id = context.category_data["id"]
    context.code = response.status_code


@then("Se Confirma estado 201 \(Categoría Creada\)\.")
def confirm_status(context):

    assert context.code == 201


@given("Se establece el parametro necesario para recuperar la categoria\.")
def parameters_recover_category(context):
    context.payload = {}
    context.url = context.url_base+'/wp-json/wp/v2/categories/'+str(context.category_id)


@when("Se recupera la Categoría con una petición GET\.")
def retrieve_category(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.category_retrieve = response.json()
    context.category_code = response.status_code


@then("Se confirma datos de la categoría creada")
def status_create_category(context):
    assert context.category_code == 200
    assert context.category_retrieve["id"] == context.category_data["id"]
    assert context.category_retrieve["description"] == context.category_data["description"]
    assert context.category_retrieve["name"] == context.category_data["name"]
    assert context.category_retrieve["link"] == context.category_data["link"]
    assert context.category_retrieve["taxonomy"] == context.category_data["taxonomy"]
    assert context.category_retrieve["slug"] == context.category_data["slug"]


@given("Se establece el parametro para actualizar la Categoría\.")
def parameters_update_category(context):

    params = GeneratorDataParameters()
    description = params.description()
    name = params.name()
    context.payload = {}
    context.url_update = (context.url_base+'/wp-json/wp/v2/categories/'+str(context.category_id)+'?name='+name+'&description='+description)


@when("Se actualiza Categoría con una petición PUT\.")
def update_category(context):
    response = requests.put(context.url_update, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_category = response.json()
    context.updated_category_code = response.status_code


@then("Se Confirma estado 200 \(Categoría actualizada\)\.")
def confirm_updated_category(context):

    assert context.updated_category_code == 200
    assert context.updated_category["id"] == context.category_id


@step("Se establece paramentros para recuperar Categoría actualizada\.")
def parameters_retrieve_updated_category(context):
    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/categories/' + str(context.category_id)


@step("Se realiza petición GET\.")
def request_category_made(context):
    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_category_recovered = response.json()
    context.code_updated_category = response.status_code


@step("Se confirma datos de la categoría actualizada\.")
def confirm_updated_category(context):

    assert context.code_updated_category == 200
    assert context.updated_category_recovered["id"] == context.updated_category["id"]
    assert context.updated_category_recovered["description"] == context.updated_category["description"]
    assert context.updated_category_recovered["name"] == context.updated_category["name"]
    assert context.updated_category_recovered["link"] == context.updated_category["link"]
    assert context.updated_category_recovered["taxonomy"] == context.updated_category["taxonomy"]
    assert context.updated_category_recovered["slug"] == context.updated_category["slug"]


@given("Se establece parametros para eliminar la Categoría\.")
def parameter_deleted_category(context):
    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/categories/' + str(context.category_id) + '?force=1'


@when("Se elimina Categoría con una petición DELETE\.")
def deleted_category(context):
    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.deleted_category_recovered = response.json()
    context.code_deleted_category = response.status_code


@then("Se Confirma estado 200 Categoría Eliminada\.")
def confirm_data_deleted_category(context):

    assert context.code_deleted_category == 200
    assert context.deleted_category_recovered["deleted"] is True
    assert context.deleted_category_recovered["previous"]["id"] == context.category_id


@step("Con petición GET se prueba a recuperar la categoría eliminada")
def retrieve_deleted_category(context):

    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/categories/' + str(context.category_id)
    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.category_recovered = response.json()
    context.code_category = response.status_code


@step("Se Confirma estado 404 Categoría No encontrada\.")
def confirm_category_not_found(context):

    assert context.code_category == 404
    assert context.category_recovered["data"]["status"] != 200
