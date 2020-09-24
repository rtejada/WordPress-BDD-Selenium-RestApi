from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os
use_step_matcher("re")


@given("Se establece la URL base y parametros de autentificación\.")
def authentication(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER')
    context.password = os.getenv('PASSWORD')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Se establecen los parametros necesarios para Crear la Página\.")
def parameters_create_page(context):

    params = GeneratorDataParameters()
    content = params.content()
    title = params.title()
    excerpt = params.excerpt()
    status = params.status()
    author = params.author()
    comment_status = params.comment_status()
    ping_status = params.ping_status()
    context.payload = {}
    context.url = (context.url_base+'/wp-json/wp/v2/pages?content='+content+'&title='+title+'&excerpt='+excerpt+'&status='+
                   status+'&author='+author+'&comment_status='+comment_status+'&ping_status='+ping_status)


@when("Se realiza la petición POST\.")
def make_request(context):

    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_data = response.json()
    context.id_page = context.page_data["id"]
    context.code = response.status_code


@then("Se Confirma estado 201 Creado\.")
def confirm_status(context):

    assert context.code == 201


@given("Se establecen los parametros necesarios para recuperar la pagina\.")
def parameters_page_retrieve(context):
    context.payload = {}
    context.url = context.url_base+'/wp-json/wp/v2/pages/'+str(context.id_page)


@when("Se recupera la página con una petición GET\.")
def retrieve_page(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_retrieve = response.json()
    context.code = response.status_code


@step("Se confirman los datos de la página creada")
def confirm_data(context):

    assert context.code == 200
    assert context.page_retrieve["id"] == context.page_data["id"]
    assert context.page_retrieve["date"] == context.page_data["date"]
    assert context.page_retrieve["status"] == context.page_data["status"]
    assert context.page_retrieve["title"]["rendered"] == context.page_data["title"]["rendered"]
    assert context.page_retrieve["content"]["rendered"] == context.page_data["content"]["rendered"]
    assert context.page_retrieve["author"] == context.page_data["author"]
    assert context.page_retrieve["comment_status"] == context.page_data["comment_status"]
    assert context.page_retrieve["ping_status"] == context.page_data["ping_status"]


@given("Se establecen parametros para actualizar la pagina\.")
def parameters_update_page(context):

    context.payload = {}
    params = GeneratorDataParameters()
    content = params.content()
    title = params.title()
    excerpt = params.excerpt()
    status = params.status()
    author = params.author()
    comment_status = params.comment_status()
    ping_status = params.ping_status()
    context.url_put = (context.url_base + '/wp-json/wp/v2/pages/'+str(context.id_page)+'?content=' + content + '&title=' + title + '&excerpt=' + excerpt + '&status=' +
                   status + '&author=' + author + '&comment_status=' + comment_status + '&ping_status=' + ping_status)


@when("Se actualiza la página con una petición PUT\.")
def update_page(context):

    response = requests.put(context.url_put, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_put = response.json()
    context.id_page_put = context.page_put["id"]
    context.code_put = response.status_code


@then("Se Confirma el estado 200 Actualizado\.")
def confirm_status(context):

    assert context.code_put == 200


@step("Se recupera página con petición GET")
def parameters_retrieve_page(context):
    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/pages/' + str(context.id_page_put)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_put_retrieve = response.json()
    context.code_put = response.status_code


@step("Se confirman datos de la página actualizada")
def confirm_data_update(context):

    assert context.code_put == 200
    assert context.page_put_retrieve["id"] == context.page_put["id"]
    assert context.page_put_retrieve["date"] == context.page_put["date"]
    assert context.page_put_retrieve["status"] == context.page_put["status"]
    assert context.page_put_retrieve["title"]["rendered"] == context.page_put["title"]["rendered"]
    assert context.page_put_retrieve["content"]["rendered"] == context.page_put["content"]["rendered"]
    assert context.page_put_retrieve["author"] == context.page_put["author"]
    assert context.page_put_retrieve["comment_status"] == context.page_put["comment_status"]
    assert context.page_put_retrieve["ping_status"] == context.page_put["ping_status"]


@given("Se establecen parametros para eliminar la pagina\.")
def parameters_delete_page(context):

    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/pages/' + str(context.id_page) + '?force=1'


@when("Se elimina la página con una petición DELETE\.")
def delete_page(context):

    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_delete = response.json()
    context.code_delete = response.status_code


@then("Se Confirma el estado 200 Borrado\.")
def confirm_deleted_page_status(context):

    assert context.code_delete == 200
    assert context.page_delete["deleted"] is True


@step("Con petición GET se prueba a recuperar página eliminida")
def retrieve_deleted_page(context):

    context.payload = {}
    context.url = context.url_base + '/wp-json/wp/v2/pages/' + str(context.id_page)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_delete = response.json()
    context.code_page_delete = response.status_code


@step("Se Confirma el estado 404 No encontrado\.")
def confirm_not_found_after_delete(context):

    assert context.code_page_delete == 404
