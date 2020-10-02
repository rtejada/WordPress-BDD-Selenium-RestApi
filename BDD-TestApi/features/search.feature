# Created by roxana at 2/10/20
Feature: Listar Resultados de búsqueda en Wordpress.

  Scenario: Establecer conexión en el background de destino
    Given Establecer URL base con sus respectivos parametros de autentificación.
    And Establecer parametro de busqueda.
    When Realizar petición GET.
    Then Confirmar Resultados.