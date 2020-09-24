from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from lib.pages.generator_data_params import GeneratorDataParameters
import requests
import os
use_step_matcher("re")


@given("Se establece URL base y sus parametros de autentificación\.")
def authentication(context):

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base



@step("Se establece el parametro necesario para Crear la Entrada\.")
def step_impl(context):

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


@when("Se realiza petición POST\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 201 \(Entrada Creada\)\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Se establece el parametro necesario para recuperar la entrada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se recupera la Entrada con una petición GET\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se confirma datos de la entrada creada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Se establece el parametro para actualizar la entrada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se actualiza entrada con una petición PUT\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 200 \(Entrada actualizada\)\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se recupera entrada con petición GET")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se confirma datos de la entrada actualizada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("Se establece parametros para eliminar la entrada\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Se elimina entrada con una petición DELETE\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 200 Borrado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Con petición GET se prueba a recuperar la entrada eliminada")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Se Confirma estado 404 No encontrado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass