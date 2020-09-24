# Created by roxana at 22/09/20
Feature: Gestionar Páginas en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexion con el background de destino
    Given Se establece la URL base y parametros de autentificación.
    And Se establecen los parametros necesarios para Crear la Página.
    When Se realiza la petición POST.
    Then Se Confirma estado 201 Creado.


  Scenario: Recuperar Pagina.
    Given Se establecen los parametros necesarios para recuperar la pagina.
    When Se recupera la página con una petición GET.
    Then Se confirman los datos de la página creada

  Scenario: Actualizar Pagina.
    Given Se establecen parametros para actualizar la pagina.
    When Se actualiza la página con una petición PUT.
    Then Se Confirma el estado 200 Actualizado.
    And  Se recupera página con petición GET
    And  Se confirman datos de la página actualizada

  Scenario: Eliminar Pagina.
    Given Se establecen parametros para eliminar la pagina.
    When Se elimina la página con una petición DELETE.
    Then Se Confirma el estado 200 Borrado.
    And  Con petición GET se prueba a recuperar página eliminida
    And  Se Confirma el estado 404 No encontrado.
