from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os
import datetime
use_step_matcher("re")


@given("Se establece URL base y sus parametros de autentificación\.")
def authentication(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base



@step("Se establece el parametro necesario para Crear la Entrada\.")
def parameters_create_entry(context):

    params = GeneratorDataParameters()
    content = params.content()
    title = params.title()
    excerpt = params.excerpt()
    status = params.status()
    author = params.author()
    comment_status = params.comment_status()
    ping_status = params.ping_status()
    categories = '36'
    tags = "74"
    context.payload = {}
    context.url = (context.url_base+'posts?content='+content+'&title='+title+'&excerpt='+excerpt+'&status='+
                   status+'&author='+author+'&comment_status='+comment_status+'&ping_status='+ping_status+
                   '&categories='+categories+'&tags='+tags)


@when("Se realiza petición POST\.")
def request_entry(context):
    response = requests.post(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.entry_data = response.json()
    context.entry_id = context.entry_data["id"]
    context.entry_code = response.status_code


@then("Se Confirma estado 201 \(Entrada Creada\)\.")
def confirm_entry_status(context):

    x = datetime.datetime.now()
    date = ("%s-%s-%s" % (x.year, x.month, x.day))
    assert context.entry_code == 201
    #assert date in context.entry_data["date"]


@given("Se establece el parametro necesario para recuperar la entrada\.")
def parameters_retrieve_entry(context):

    context.payload = {}
    context.url = context.url_base+'posts/'+str(context.entry_id)


@when("Se recupera la Entrada con una petición GET\.")
def retrieve_entry(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.entry_retrieve = response.json()
    context.code = response.status_code


@then("Se confirma datos de la entrada creada")
def confirm_create_entry(context):

    assert context.code == 200
    assert context.entry_retrieve["id"] == context.entry_data["id"]
    assert context.entry_retrieve["date"] == context.entry_data["date"]
    assert context.entry_retrieve["status"] == context.entry_data["status"]
    assert context.entry_retrieve["type"] == context.entry_data["type"]
    assert context.entry_retrieve["author"] == context.entry_data["author"]
    assert context.entry_retrieve["slug"] == context.entry_data["slug"]
    assert context.entry_retrieve["title"]["rendered"] == context.entry_data["title"]["rendered"]
    assert context.entry_retrieve["content"]["rendered"] == context.entry_data["content"]["rendered"]
    assert context.entry_retrieve["excerpt"]["rendered"] == context.entry_data["excerpt"]["rendered"]
    assert context.entry_retrieve["link"] == context.entry_data["link"]
    assert context.entry_retrieve["comment_status"] == context.entry_data["comment_status"]
    assert context.entry_retrieve["ping_status"] == context.entry_data["ping_status"]


@given("Se establece el parametro para actualizar la entrada\.")
def parameters_update_entry(context):
    params = GeneratorDataParameters()
    content = params.content()
    title = params.title()
    excerpt = params.excerpt()
    status = params.status()
    author = params.author()
    comment_status = params.comment_status()
    ping_status = params.ping_status()
    context.payload = {}
    context.url = (context.url_base+'posts/'+str(context.entry_id)+'?content='+content+'&title='+title+'&excerpt='+
                   excerpt+'&status='+status+'&author='+author+'&comment_status='+comment_status+'&ping_status='+ping_status)


@when("Se actualiza entrada con una petición PUT\.")
def updated_entry(context):
    response = requests.put(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.updated_entry = response.json()
    context.id_updated_entry = context.updated_entry["id"]
    context.code_updated_entry = response.status_code


@then("Se Confirma estado 200 \(Entrada actualizada\)\.")
def confirm_status_update_entry(context):

    assert context.code_updated_entry == 200


@step("Se recupera entrada con petición GET")
def retrieve_entry(context):
    context.payload = {}
    context.url = context.url_base+'posts/'+str(context.entry_id)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.entry_updated_retrieve = response.json()
    context.code_entry_retrieve = response.status_code


@step("Se confirma datos de la entrada actualizada")
def confirm_data_updated_entry(context):

    assert context.code_entry_retrieve == 200
    assert context.entry_updated_retrieve["id"] == context.updated_entry["id"]
    assert context.entry_updated_retrieve["date"] == context.updated_entry["date"]
    assert context.entry_updated_retrieve["status"] == context.updated_entry["status"]
    assert context.entry_updated_retrieve["type"] == context.updated_entry["type"]
    assert context.entry_updated_retrieve["author"] == context.updated_entry["author"]
    assert context.entry_updated_retrieve["slug"] == context.updated_entry["slug"]
    assert context.entry_updated_retrieve["title"]["rendered"] == context.updated_entry["title"]["rendered"]
    assert context.entry_updated_retrieve["content"]["rendered"] == context.updated_entry["content"]["rendered"]
    assert context.entry_updated_retrieve["excerpt"]["rendered"] == context.updated_entry["excerpt"]["rendered"]
    assert context.entry_updated_retrieve["link"] == context.updated_entry["link"]
    assert context.entry_updated_retrieve["comment_status"] == context.updated_entry["comment_status"]
    assert context.entry_updated_retrieve["ping_status"] == context.updated_entry["ping_status"]


@given("Se establece parametros para eliminar la entrada\.")
def parameters_deleted_entry(context):
    context.payload = {}
    context.url = context.url_base+'posts/'+str(context.entry_id)+'?force=1'


@when("Se elimina entrada con una petición DELETE\.")
def deleted_entry(context):

    response = requests.delete(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.deleted_entry = response.json()
    context.code_entry_deleted = response.status_code


@then("Se Confirma estado 200 Borrado\.")
def confirm_status_deleted(context):

    x = datetime.datetime.now()
    date = ("%s-%s-%s" % (x.year, x.month, x.day))
    assert context.code_entry_deleted == 200
    #assert date in context.deleted_entry["previous"]["date"]
    assert context.deleted_entry["deleted"] is not False


@step("Con petición GET se prueba a recuperar la entrada eliminada")
def parameters_retrieve_entry(context):

    context.payload = {}
    context.url = context.url_base + 'posts/' + str(context.entry_id)

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.deleted_entry_retrieved = response.json()
    context.code_deleted_entry_retrieved = response.status_code


@step("Se Confirma estado 404 No encontrado\.")
def confirm_entry_not_found(context):

    assert context.code_deleted_entry_retrieved == 404
    assert context.deleted_entry_retrieved["data"]["status"] == 404
