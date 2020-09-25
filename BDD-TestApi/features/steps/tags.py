from behave import *
from dotenv import load_dotenv
from lib.pages.generator_data_params import GeneratorDataParameters
from requests.auth import HTTPBasicAuth
import requests
import os

use_step_matcher("re")


@given("Se establece URL base con su respectivo parametro de autentificación\.")
def authentication(context):
    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Se establece el parametro necesario para Crear la Etiqueta\.")
def parameters_create_label(context):
    params = GeneratorDataParameters()
    description = params.description()
    name = params.name()
    context.payload = {}
    context.url = (context.url_base+'tags?name='+name+'&description='+description)


@when("Creamos Etiqueta mediante petición POST\.")
def create_label(context):
    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.tags_data = response.json()
    context.tags_id = context.tags_data["id"]
    context.tags_code = response.status_code


@then("Se Confirma estado 201 \(Etiqueta Creada\)\.")
def confirm_status_create_label(context):

    assert context.tags_code == 201


@given("Se establece el parametro necesario para recuperar la etiqueta\.")
def parameters_retrieve_label(context):

    context.payload = {}
    context.url = context.url_base+'tags/'+str(context.tags_id)


@when("Se recupera la Etiqueta con una petición GET\.")
def retrieve_label(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.tags_data_retrieve = response.json()
    context.tags_code_retrieve = response.status_code


@then("Se confirma datos de la etiqueta creada")
def confirm_data_create_label(context):

    assert context.tags_code_retrieve == 200
    assert context.tags_data_retrieve["id"] == context.tags_data["id"]
    assert context.tags_data_retrieve["description"] == context.tags_data["description"]
    assert context.tags_data_retrieve["name"] == context.tags_data["name"]
    assert context.tags_data_retrieve["link"] == context.tags_data["link"]
    assert context.tags_data_retrieve["taxonomy"] == context.tags_data["taxonomy"]
    assert context.tags_data_retrieve["slug"] == context.tags_data["slug"]


@given("Se establece el parametro para actualizar la etiqueta\.")
def parameters_updated_label(context):
    params = GeneratorDataParameters()
    description = params.description()
    name = params.name()
    context.payload = {}
    context.url = (context.url_base+'tags/'+str(context.tags_id)+'?name='+name+'&description='+description)


@when("Se actualiza etiqueta con una petición PUT\.")
def updated_label(context):
    response = requests.put(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_tags = response.json()
    context.updated_tags_code = response.status_code


@then("Se Confirma estado 200 \(etiqueta actualizada\)\.")
def confirm_status_update_label(context):

    assert context.updated_tags_code == 200
    assert context.updated_tags["id"] == context.tags_id


@step("Se establecen paramentros para recuperar etiqueta actualizada\.")
def parameters_retrieved_update_label(context):

    context.payload = {}
    context.url = context.url_base+'tags/'+str(context.tags_id)


@step("Se recupera etiqueta con un petición GET\.")
def retrieved_updated_label(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_tags_retrieve = response.json()
    context.updated_tags_code_retrieve = response.status_code


@step("Se confirman datos de la etiqueta actualizada\.")
def confirm_updated_label(context):

    assert context.updated_tags_code_retrieve == 200
    assert context.updated_tags_retrieve["id"] == context.updated_tags["id"]
    assert context.updated_tags_retrieve["description"] == context.updated_tags["description"]
    assert context.updated_tags_retrieve["name"] == context.updated_tags["name"]
    assert context.updated_tags_retrieve["link"] == context.updated_tags["link"]
    assert context.updated_tags_retrieve["taxonomy"] == context.updated_tags["taxonomy"]
    assert context.updated_tags_retrieve["slug"] == context.updated_tags["slug"]


@given("Se establece parametros para eliminar la etiqueta\.")
def parameters_deleted_label(context):

    context.payload = {}
    context.url = context.url_base+'tags/'+str(context.tags_id)+'?force=1'


@when("Se elimina etiqueta con una petición DELETE\.")
def deleted_label(context):
    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.deleted_tags_recovered = response.json()
    context.code_deleted_tags = response.status_code


@then("Se Confirma estado 200 Etiqueta Eliminada\.")
def confirm_label_deleted(context):

    assert context.code_deleted_tags == 200
    assert context.deleted_tags_recovered["deleted"] is True
    assert context.deleted_tags_recovered["previous"]["id"] == context.tags_id


@step("Se establecen paramentros para visualizar etiqueta\.")
def parameters_display_label(context):

    context.payload = {}
    context.url = context.url_base+'tags/'+str(context.tags_id)


@step("Con una petición GET se prueba a recuperar la etiqueta eliminada")
def display_label(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.tags_recovered = response.json()
    context.tags_code = response.status_code


@step("Se Confirma estado 404 Etiqueta No encontrada\.")
def confirm_label_not_found(context):

    assert context.tags_code == 404
    assert context.tags_recovered["data"]["status"] != 200
