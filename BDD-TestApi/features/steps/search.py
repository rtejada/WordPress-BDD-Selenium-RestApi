from behave import *
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import os
import requests
use_step_matcher("re")


@given("Establecer URL base con sus respectivos parametros de autentificación\.")
def set_authentication_parameters(context):

    context.page_data = {"search": "Pruebas", "type": "post", "subtype": "page"}

    load_dotenv(os.getcwd() + "/BDD-TestApi/features/lib/data/.env.wordpress")
    context.user = os.getenv('USER_API')
    context.password = os.getenv('PASS_API')
    context.page_id = os.getenv('PAGE_ID')
    url_base = os.getenv('URL_BASE')
    context.url_base = url_base


@step("Establecer parametro de busqueda\.")
def set_search_parameters(context):

    context.payload = {}
    context.url = (
            context.url_base+'search?type=post&search='+context.page_data["search"])


@when("Realizar petición GET\.")
def step_impl(context):

    response = requests.get(context.url, auth=HTTPBasicAuth(context.user, context.password), data=context.payload)
    context.page_retrieved = response.json()
    context.code = response.status_code


@then("Confirmar Resultados\.")
def step_impl(context):

    assert context.code == 200

    for i in range(len(context.page_retrieved)):
        assert str(context.page_retrieved[i]["id"]) == context.page_id
        assert context.page_data["search"] in context.page_retrieved[i]["title"]
        assert context.page_retrieved[i]["type"] == context.page_data["type"]
        assert context.page_retrieved[i]["subtype"] == context.page_data["subtype"]



