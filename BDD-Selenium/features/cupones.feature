# Created by roxana at 10/12/20
Feature: Gestión de Marketing en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con permisos de acceso.
    And Inicia sesion en la Website.


  Scenario: Añadir nuevos cupones.
    Given Usuario autorizado. Accede al menu marketing (cupones)
    When En la opción, pulsa y añade un nuevo cupón.
    Then Confirma los datos del nuevo cupón añadido.


