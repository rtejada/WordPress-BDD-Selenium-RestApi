# Created by roxana at 29/11/20

Feature: Gestión de Páginas en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con permisos asignados.
    And Inicia nueva sesion en la web.

  Scenario Outline: Crear Páginas.
    Given Usuario con permisos, accede a las páginas.
    When Dentro de la opcion, pulsa y añade nueva página <titulo>.
    Then Confirma el título de la página creada.

    Examples:
    |titulo|
    |padre|
    |hijo|



