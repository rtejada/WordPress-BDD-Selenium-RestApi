# Created by roxana at 29/11/20
Feature: Gestión de Medios en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con permisos de administración asignados.
    And Iniciar sesion en la web.

  Scenario: Subir Nuevos Medios.
    Given Usuario con permisos. Accede a los Medios.
    When En la opcion, pulsa y añade un nuevo medio.
    Then Confirma en la WEB los medios añadidos.
