# Created by roxana at 25/09/20
Feature: Gestionar Etiquetas en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexión con el background de destino
    Given Se establece URL base con su respectivo parametro de autentificación.
    And Se establece el parametro necesario para Crear la Etiqueta.
    When Creamos Etiqueta mediante petición POST.
    Then Se Confirma estado 201 (Etiqueta Creada).


  Scenario: Recuperar Etiqueta Creada.
    Given Se establece el parametro necesario para recuperar la etiqueta.
    When Se recupera la Etiqueta con una petición GET.
    Then Se confirma datos de la etiqueta creada

  Scenario: Actualizar Etiqueta Creada.
    Given Se establece el parametro para actualizar la etiqueta.
    When Se actualiza etiqueta con una petición PUT.
    Then Se Confirma estado 200 (etiqueta actualizada).
    And  Se establecen paramentros para recuperar etiqueta actualizada.
    And  Se recupera etiqueta con un petición GET.
    And  Se confirman datos de la etiqueta actualizada.

  Scenario: Eliminar Etiqueta.
    Given Se establece parametros para eliminar la etiqueta.
    When Se elimina etiqueta con una petición DELETE.
    Then Se Confirma estado 200 Etiqueta Eliminada.
    And  Se establecen paramentros para visualizar etiqueta.
    And  Con una petición GET se prueba a recuperar la etiqueta eliminada
    And  Se Confirma estado 404 Etiqueta No encontrada.
