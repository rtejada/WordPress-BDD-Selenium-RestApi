# Created by roxana at 2/10/20
Feature: Gestionar Comentarios en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexión con el background de destino
    Given Establecer URL base y sus parametros de autentificación.
    And Establecer el parametro necesario para Crear el Comentario.
    When Realizar petición POST.
    Then Confirmar estado 201 (Comentario Creada).

  Scenario: Recuperar Comentario Creado.
    Given Establecer el parametro necesario para recuperar el comentario.
    When Recuperar Comentario con una petición GET.
    Then Confirmar datos del comentario creado.

  Scenario: Actualizar Comentario Creado.
    Given Establecer parametro para actualizar comentario.
    When Actualizar comentario con una petición PUT.
    Then Confirmar estado 200 (Comentario actualizado).
    And  Recupera comentario actualizado con una petición GET
    And  Confirmar datos del nuevo comentario (actualizado)

  Scenario: Eliminar Comentario.
    Given Establecer parametros para eliminar comentario.
    When Eliminar comentario con una petición DELETE.
    Then Confirmar estado 200 Comentario eliminado.
    And  Con petición GET probar a recuperar la entrada eliminada
    And  Confirmar estado 404 Comentario No encontrado.

  Scenario: Listar Comentario Existentes
    Given Establecer parametros para listar comentarios.
    When Listar comentarios con petición GET
    Then Confirmar estado 200.

