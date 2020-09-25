# Created by roxana at 24/09/20
Feature: Gestionar Categorías en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexión con el background de destino
    Given Se establece URL base con sus parametros de autentificación.
    And Se establece el parametro necesario para Crear la Categoría.
    When Se realiza una petición POST.
    Then Se Confirma estado 201 (Categoría Creada).


  Scenario: Recuperar Categoría Creada.
    Given Se establece el parametro necesario para recuperar la categoria.
    When Se recupera la Categoría con una petición GET.
    Then Se confirma datos de la categoría creada

  Scenario: Actualizar Categoría Creada.
    Given Se establece el parametro para actualizar la Categoría.
    When Se actualiza Categoría con una petición PUT.
    Then Se Confirma estado 200 (Categoría actualizada).
    And  Se establece paramentros para recuperar Categoría actualizada.
    And  Se realiza petición GET.
    And  Se confirma datos de la categoría actualizada.

  Scenario: Eliminar Categoría.
    Given Se establece parametros para eliminar la Categoría.
    When Se elimina Categoría con una petición DELETE.
    Then Se Confirma estado 200 Categoría Eliminada.
    And  Con petición GET se prueba a recuperar la categoría eliminada
    And  Se Confirma estado 404 Categoría No encontrada.
