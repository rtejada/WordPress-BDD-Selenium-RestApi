# Created by roxana at 28/10/20
Feature: Gestión de Usuarios en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que supone que debe hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer conexión en la página web WordPress.
    Given Un usuario con credenciales de administración asignados.
    And Inicia sesion en la web.



  Scenario Outline: Agregar Nuevos Usuarios con distintos Perfiles.
    Given Un usuario con perfil autorizado. Accede al Menú Usuarios (añadir nuevo)
    When Dentro de la opcion, añade los datos del nuevo usuario: <role>, <name>
    Then Confirmar en la WEB los datos del nuevo usuario añadido.
    And Confirmar en la BBDD los datos del nuevo usuario añadido.

    Examples:
    |role|name|
    |shop_manager|A|
    |customer|B|
    |subscriber|C|
    |author|D|
    |editor|E|
    |administrator|F|