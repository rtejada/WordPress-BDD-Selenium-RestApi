# Created by roxana at 14/11/20
Feature: Gestión de Entradas en Wordpress
  As (Como) usuario con permisos.
  I Want to (Quiero) asegurarme que los pasos informados en la documentacion. hacen
  lo que dicen que deben hacer...
  So that (Para) quien lo necesita y/o solicite.

  Background: Establecer Conexión en la Página web WordPress.
    Given Usuario con credenciales de administración asignados.
    And Inicia una sesion en la web.

  Scenario: Añadir Nueva Etiqueta.
    Given Usuario con un perfil autorizado. Accede al Menú Entradas (Etiquetas)
    When Dentro de la opcion, pulsa y añade los datos de una nueva etiqueta.
    Then Confirma en la WEB los datos de la nueva etiqueta añadida.

  Scenario: Añadir Nueva Categoría.
    Given Usuario autorizado. Accede al Menú Entradas (Categorias)
    When Dentro de la opcion, pulsa y añade los datos de una nueva categoría.
    Then Confirma en la WEB los datos de la nueva categoría añadida.


  Scenario Outline: Añadir Nueva Entrada.
    Given Usuario con perfil autorizado. Accede al Menú Entradas (Nueva Entrada)
    When Dentro de la opcion, pulsa y añade los datos de una nueva entrada <img>, <categoria>, <etiqueta>.
    Then Confirma en la WEB los datos de la nueva entrada añadida.

    Examples:
    |img|categoria|etiqueta|
    |image1.jpg|CategoriaPadre-18|Etiqueta-1|
    |image2.jpg|CategoriaHijo-18 |Etiqueta-2|

