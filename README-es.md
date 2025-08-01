
[English](README.md) | [日本語](README-ja.md) | [العربية](README-ar.md) | [Português](README-pt.md)

# Raspador de Productos de Depop

## Descripción General
Este script de Python automatiza la extracción de información de productos desde Depop.com utilizando Selenium y BeautifulSoup. Recoge detalles como título, precio, descripción, imágenes, opciones y reseñas, y estructura los datos en formato JSON.

## Características Principales

- **Extracción Automática de Datos**: Usando Selenium WebDriver
- **Detalles Completos del Producto**:
  - Título y precio
  - Descripción detallada
  - Hasta 8 imágenes del producto
  - Opciones y variaciones disponibles
  - Opiniones de clientes con calificación
- **Procesamiento de URLs de Imágenes**: Mediante expresiones regulares
- **Integración con JSON**:
  - Lee `upload_results.json`
  - Sustituye URLs originales por las nuevas
  - Salida final en `product_info.json`

## Implementación Técnica

- **Selenium WebDriver**
- **BeautifulSoup**
- **WebDriverWait**
- **Procesamiento de JSON**
- **Manejo de Errores**: Garantiza ejecución completa aún si faltan elementos

## Instrucciones

1. Establece la URL del producto en `product_page_url`
2. Asegúrate de tener instalado ChromeDriver con ChromeDriverManager
3. Ejecuta el script:
   - Abre la página
   - Extrae y procesa los datos
   - Genera el JSON estructurado
4. El navegador se cierra automáticamente

## Estructura de Salida
```json
{
  "price": "extracted_price",
  "itm_name": "product_title",
  "img1" a "img8": "processed_image_names",
  "itm_dsc": "product_description",
  "cat_id": "category_id",
  "s_id": "seller_id",
  "attr": ["option1", "option2"],
  "eva": [{"name": "reviewer", "content": "review", "level": 5}]
}
