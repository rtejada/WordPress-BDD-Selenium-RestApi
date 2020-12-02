# Created by roxana at 29/11/20

Feature: Gestión de Páginas en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con permisos asignados.
    And Inicia nueva sesion en la web.

  Scenario: Crear Páginas.
    Given Usuario con permisos, accede a todas las páginas.
    When En la opcion, pulsa y añade una nueva página.
    Then Se confirman los datos de la página creada.
