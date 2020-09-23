from behave import *
from dotenv import load_dotenv
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os
use_step_matcher("re")


@given("Se establece la URL base y parametros de autentificación\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    auth = os.getenv('AUTH')
    url_base = os.getenv('URL_BASE')
    headers = {
        'Authorization': auth
    }
    context.url_base = url_base
    context.headers = headers


@step("Se establecen los parametros necesarios para Crear la Página\.")
def step_impl(context):

    params = GeneratorDataParameters()
    content = params.content()
    title = params.title()
    excerpt = params.excerpt()
    status = params.status()
    slug = params.slug()
    author = params.author()
    comment_status = params.comment_status()
    ping_status = params.ping_status()

    context.url = (context.url_base+'/wp-json/wp/v2/pages?content='+content+'&title='+title+'&excerpt='+excerpt+'&status='+
                   status+'&author='+author+'&comment_status='+comment_status+'&slug='+slug+'&ping_status='+ping_status)


@when("Se realiza la petición POST\.")
def step_impl(context):

    payload = {}
    response = requests.post(context.url, headers=context.headers, data=payload)
    context.page_data = response.json()
    context.id_page = context.page_data["id"]
    context.code = response.status_code


@then("Se Confirma estado 201 Creado\.")
def step_impl(context):

    assert context.code == 201


@given("Se establecen los parametros necesarios para recuperar la pagina\.")
def step_impl(context):
    context.payload = {}
    context.url = context.url_base+'/wp-json/wp/v2/pages/'+str(context.id_page)

@when("Se recupera la página con una petición GET\.")
def step_impl(context):

    response = requests.get(context.url, headers=context.headers, data=context.payload)
    context.page_retrieve = response.json()
    context.code = response.status_code


@step("Se confirman los datos de la página creada")
def step_impl(context):

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
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se actualiza la página con una petición PUT\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma el estado 200 Actualizado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se recupera página con petición GET")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se confirman datos de la página actualizada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass