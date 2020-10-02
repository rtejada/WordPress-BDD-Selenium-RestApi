from behave import *
from dotenv import load_dotenv
from lib.pages.generator_data_params import GeneratorDataParameters
from requests.auth import HTTPBasicAuth
import requests
import os

use_step_matcher("re")


@given("Establecer URL base y parametros de autentificación\.")
def set_authentication_parameters(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    context.page_id = os.getenv('PAGE_ID')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Establecer parametros para Crear el Usuario\.")
def set_parameters_create_user(context):

    params = GeneratorDataParameters()
    username = params.username()
    name = params.name()
    first_name = params.first_name()
    last_name = params.last_name()
    email = params.email()
    url = 'https://prueba.es'
    description = params.description()
    locale = 'es_ES'
    nickname = params.username()
    password = params.password()
    roles = params.name()

    context.payload = {}
    context.url = (
                context.url_base+'users?username='+username+'&name='+name+'&first_name='+first_name+'&last_name='+last_name+
                '&email='+email+'&description='+description+'&locale='+locale+'&url='+url+'&password='+password+
                '&nickname='+nickname)


@when("Realizar una petición POST\.")
def make_a_request(context):

    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.user_data = response.json()
    context.user_id = context.user_data["id"]
    context.code = response.status_code


@then("Confirmar estado 201 Usuario Creado\.")
def confirm_status(context):

    assert context.code == 201


@given("Establecer parametros para recuperar el usuario\.")
def set_parameters_retrieve_user(context):

    context.payload = {}
    context.url = context.url_base + 'users/' + str(context.user_id)


@when("Recuperar Usuario con una petición GET\.")
def retrieve_user(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.user_data_retrieve = response.json()
    context.code = response.status_code


@then("Confirmar los datos del usuario creado\.")
def confirm_data_user(context):

    assert context.code == 200
    assert context.user_data_retrieve["id"] == context.user_data["id"]
    assert context.user_data_retrieve["name"] == context.user_data["name"]
    assert context.user_data_retrieve["url"] == context.user_data["url"]
    assert context.user_data_retrieve["description"] == context.user_data["description"]


@given("Establecer parametros para actualizar los datos del usuario\.")
def set_parameters_update_data_user(context):
    params = GeneratorDataParameters()
    name = params.name()
    first_name = params.first_name()
    last_name = params.last_name()
    email = params.email()
    url = 'https://wordpress.es'
    description = params.description()
    nickname = params.username()

    context.payload = {}
    context.url = (
            context.url_base+'users/'+str(context.user_id)+'?name='+name+'&first_name='+first_name+'&last_name='
            +last_name+'&email='+email+'&description='+description+'&url='+url+'&nickname='+nickname)


@when("Actualizar los datos con una petición PUT\.")
def update_data_user(context):

    response = requests.put(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.update_data_user = response.json()
    context.id_update_user = context.update_data_user["id"]
    context.code_update_user = response.status_code


@then("Confirmar estado 200 Datos actualizados\.")
def confirm_status(context):

    assert context.code_update_user == 200


@step("Recuperar Datos actualizados con petición GET")
def step_impl(context):

    context.payload = {}
    context.url = context.url_base + 'users/' + str(context.id_update_user)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.retrieve_updated_user_data = response.json()
    context.retrieve_updated_id_user = context.retrieve_updated_user_data["id"]
    context.code = response.status_code


@step("Confirmar datos actualizados")
def step_impl(context):

    assert context.code == 200
    assert context.retrieve_updated_user_data["id"] == context.update_data_user["id"]
    assert context.retrieve_updated_user_data["name"] == context.update_data_user["name"]
    assert context.retrieve_updated_user_data["url"] == context.update_data_user["url"]
    assert context.retrieve_updated_user_data["description"] == context.update_data_user["description"]


@given("Establecer parametros para eliminar usuario\.")
def step_impl(context):

    context.payload = {}
    context.url = context.url_base + 'users/' + str(context.user_id)+'?force=1&reassign=8'


@when("Eliminar usuario con una petición DELETE\.")
def step_impl(context):

    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.delete_user_data = response.json()
    context.code = response.status_code


@then("Confirmar 200 Datos del usurio elimando\.")
def confirm_status(context):

    assert context.code == 200
    assert context.delete_user_data["deleted"] is True


@step("Con una petición GET probar a recuperar datos del usuario eliminido\.")
def retrieve_data_user_delete(context):

    context.payload = {}
    context.url = context.url_base + 'users/' + str(context.user_id)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.retrieve_deleted_user_data = response.json()
    context.code = response.status_code


@step("Confirmar estado 404 No encontrado\.")
def confirm_status_not_found(context):

    assert context.code == 404
    assert context.retrieve_deleted_user_data["data"]["status"] >= 400
