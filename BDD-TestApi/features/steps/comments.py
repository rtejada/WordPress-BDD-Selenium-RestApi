from behave import *
from dotenv import load_dotenv
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
from requests.auth import HTTPBasicAuth
import os

use_step_matcher("re")


@given("Establecer URL base y sus parametros de autentificación\.")
def authentication(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    context.page_id = os.getenv('PAGE_ID')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Establecer el parametro necesario para Crear el Comentario\.")
def parameters_create_comment(context):
    params = GeneratorDataParameters()
    content = params.content()
    status = params.status()
    author_email = params.email()
    author_name = params.name()

    context.payload = {}
    context.url = (
                context.url_base+'comments?post='+context.page_id+'&content='+content+'&author_name='+author_name+'&author_email='
                +author_email+'&status='+status)


@when("Realizar petición POST\.")
def make_a_request(context):

    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.comment_data = response.json()
    context.comment_id = context.comment_data["id"]
    context.code = response.status_code


@then("Confirmar estado 201 \(Comentario Creada\)\.")
def confirm_status(context):

    assert context.code == 201


@given("Establecer el parametro necesario para recuperar el comentario\.")
def establish_parameters_retrieve_comment(context):

    context.payload = {}
    context.url = context.url_base + 'comments/' + str(context.comment_id)


@when("Recuperar Comentario con una petición GET\.")
def retrieve_a_comment(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.comment_retrieve = response.json()
    context.code = response.status_code


@then("Confirmar datos del comentario creado\.")
def step_impl(context):

    assert context.code == 200
    assert context.comment_retrieve["id"] == context.comment_data["id"]
    assert context.comment_retrieve["post"] == context.comment_data["post"]
    assert context.comment_retrieve["author_name"] == context.comment_data["author_name"]
    assert context.comment_retrieve["date"] == context.comment_data["date"]
    assert context.comment_retrieve["status"] == context.comment_data["status"]
    assert context.comment_retrieve["type"] == context.comment_data["type"]
    assert context.comment_retrieve["content"]["rendered"] == context.comment_data["content"]["rendered"]


@given("Establecer parametro para actualizar comentario\.")
def set_parameters_to_comment_update(context):
    params = GeneratorDataParameters()
    content = params.content()
    status = params.status()
    author_email = params.email()
    author_name = params.name()

    context.payload = {}
    context.url = (
            context.url_base+'comments/'+str(context.comment_id)+'?content='+content+'&author_name='+author_name+'&author_email='
            +author_email+'&status='+status)


@when("Actualizar comentario con una petición PUT\.")
def update_comment(context):

    response = requests.put(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_comment = response.json()
    context.id_updated_comment = context.updated_comment["id"]
    context.code_updated_comment = response.status_code


@then("Confirmar estado 200 \(Comentario actualizado\)\.")
def confirm_status(context):

    assert context.code_updated_comment == 200


@step("Recupera comentario actualizado con una petición GET")
def retrieve_updated_commentary(context):

    context.payload = {}
    context.url = context.url_base + 'comments/' + str(context.id_updated_comment)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.update_comment_retrieve = response.json()
    context.code = response.status_code


@step("Confirmar datos del nuevo comentario \(actualizado\)")
def confirm_new_comment_data(context):

    assert context.code == 200
    assert context.update_comment_retrieve["id"] == context.updated_comment["id"]
    assert context.update_comment_retrieve["post"] == context.updated_comment["post"]
    assert context.update_comment_retrieve["author_name"] == context.updated_comment["author_name"]
    assert context.update_comment_retrieve["date"] == context.updated_comment["date"]
    assert context.update_comment_retrieve["status"] == context.updated_comment["status"]
    assert context.update_comment_retrieve["type"] == context.updated_comment["type"]
    assert context.update_comment_retrieve["content"]["rendered"] == context.updated_comment["content"]["rendered"]


@given("Establecer parametros para eliminar comentario\.")
def set_parameters_delete_commentary(context):

    context.payload = {}
    context.url = context.url_base+'comments/'+str(context.comment_id)+'?force=1'


@when("Eliminar comentario con una petición DELETE\.")
def delete_commentary(context):

    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.comment_delete = response.json()
    context.code_comment_delete = response.status_code


@then("Confirmar estado 200 Comentario eliminado\.")
def confirm_status(context):

    assert context.code_comment_delete == 200
    assert context.comment_delete["deleted"] is True


@step("Con petición GET probar a recuperar la entrada eliminada")
def retrieve_deleted_comment(context):

    context.payload = {}
    context.url = context.url_base + 'comments/' + str(context.comment_id)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.comment_delete = response.json()
    context.code = response.status_code


@step("Confirmar estado 404 Comentario No encontrado\.")
def confirm_status(context):

    assert context.code == 404
    assert context.comment_delete["data"]["status"] == 404


@given("Establecer parametros para listar comentarios\.")
def set_parameters_list_comment(context):

    context.payload = {}
    context.url = context.url_base + 'comments'


@when("Listar comentarios con petición GET")
def list_commentary(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.comment_list = response.json()
    context.code = response.status_code


@then("Confirmar estado 200\.")
def confirm_status(context):

    assert context.code == 200
