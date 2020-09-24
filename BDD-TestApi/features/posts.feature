# Created by roxana at 24/09/20
Feature: Gestionar Entradas en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexión con el background de destino
    Given Se establece URL base y sus parametros de autentificación.
    And Se establece el parametro necesario para Crear la Entrada.
    When Se realiza petición POST.
    Then Se Confirma estado 201 (Entrada Creada).


  Scenario: Recuperar Entrada Creada.
    Given Se establece el parametro necesario para recuperar la entrada.
    When Se recupera la Entrada con una petición GET.
    Then Se confirma datos de la entrada creada

  Scenario: Actualizar Entrada Creada.
    Given Se establece el parametro para actualizar la entrada.
    When Se actualiza entrada con una petición PUT.
    Then Se Confirma estado 200 (Entrada actualizada).
    And  Se recupera entrada con petición GET
    And  Se confirma datos de la entrada actualizada

  Scenario: Eliminar Entrada.
    Given Se establece parametros para eliminar la entrada.
    When Se elimina entrada con una petición DELETE.
    Then Se Confirma estado 200 Borrado.
    And  Con petición GET se prueba a recuperar la entrada eliminada
    And  Se Confirma estado 404 No encontrado.
