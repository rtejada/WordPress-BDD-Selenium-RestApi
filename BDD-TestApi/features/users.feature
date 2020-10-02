# Created by roxana at 2/10/20
Feature: Gestionar Usuarios en Wordpress
  Como usuario con permisos
  Quiero asegurarme de que los pasos informados en la documentacion, hacen
  lo que supone que debe hacer...

  Background: Establecer conexion con el Background de Destino
    Given Establecer URL base y parametros de autentificación.
    And Establecer parametros para Crear el Usuario.
    When Realizar una petición POST.
    Then Confirmar estado 201 Usuario Creado.


  Scenario: Recuperar Usuario.
    Given Establecer parametros para recuperar el usuario.
    When Recuperar Usuario con una petición GET.
    Then Confirmar los datos del usuario creado.

  Scenario: Actualizar Datos del usuario.
    Given Establecer parametros para actualizar los datos del usuario.
    When Actualizar los datos con una petición PUT.
    Then Confirmar estado 200 Datos actualizados.
    And  Recuperar Datos actualizados con petición GET
    And  Confirmar datos actualizados

  Scenario: Eliminar Usuario.
    Given Establecer parametros para eliminar usuario.
    When Eliminar usuario con una petición DELETE.
    Then Confirmar 200 Datos del usurio elimando.
    And  Con una petición GET probar a recuperar datos del usuario eliminido.
    And  Confirmar estado 404 No encontrado.
