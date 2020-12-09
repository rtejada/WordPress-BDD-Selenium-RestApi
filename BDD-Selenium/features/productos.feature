# Created by roxana at 9/12/20
Feature: Gestión de Productos en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con permisos de administración de productos asignados.
    And Inicia sesion en la página web.


  Scenario: Añadir Nueva Categoría.
    Given Usuario autorizado. Accede al menu de productos (categorías)
    When En la opcion, pulsa y añade los datos de una nueva categoría.
    Then Confirma los datos de la nueva categoría añadida.


  Scenario: Añadir Nueva Etiqueta.
    Given Usuario autorizado. Accede al menú de productos (etiquetas)
    When En la opcion, pulsa y añade los datos de una nueva etiqueta.
    Then Confirma los datos de la nueva etiqueta añadida.


  Scenario: Añadir Nuevo Atributo.
    Given Usuario autorizado. Accede al menú de productos (atributos)
    When En la opcion, pulsa y añade los datos de un nuevo atributo.
    Then Confirma los datos del nuevo atributo añadida.


  Scenario: Añadir Nuevo Producto.
    Given Usuario autorizado. Accede al menú de productos.
    When En la opcion, pulsa y añade los datos de un nuevo producto.
    Then Confirma los datos del nuevo producto añadida.