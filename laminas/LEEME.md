# Láminas y cuadernos: una sola línea

Decisión 5A del 20/11/2026. El sitio, las láminas de Instagram y los cuadernos de Técnica Clásica comparten la misma piel.

## Común a los tres

- Tela verde #2d4535 como fondo de tapa (en el sitio, la tapa y el pie; en Instagram, el fondo de cada lámina; en los cuadernos, la tapa) y papel #ebebe6 para lo que se lee largo.
- Una sola fuente: Schola SdM regular, con cursiva solo para nombres científicos y títulos de obras. Sin negrita de acento.
- Sin emojis, sin mayúsculas espaciadas, sin contadores (nada de «1 / 5»), sin íconos.
- Créditos de una línea, siempre con la misma forma: «Qué se ve · Foto: autor, licencia o forma de uso, recortada».
- Colofón al final: «Compuesto en Schola SdM, derivada de TeX Gyre Schola (licencia GUST)».

## Láminas de Instagram (1080 × 1350)

- `plantilla.js` trae las piezas: fondo de tela, cabecera con el nombre de la serie, pie con sitio y mes, párrafo, filete y `lamina()` para pegar una foto o un croquis sobre papel con su crédito debajo.
- Ningún texto por debajo de 36 px (en el celular queda en unos 13 px); el cuerpo, a 44 px o más.
- Una Palabra de taller puede llevar un croquis de línea. Debajo del croquis no va crédito ni firma.
- Las láminas de «Maderas de la tapa» usan la misma foto y el mismo crédito que la carta del sitio.
- `ejemplo.html` muestra cuatro láminas de muestra. Para un carrusel nuevo: copiar `ejemplo.html`, cambiar el contenido y abrirlo desde la vista previa de la rama (la fuente no carga si se abre el archivo directo desde la compu). Cada lámina tiene su enlace de descarga.

## Cuadernos de Técnica Clásica (17 × 24 cm)

- Tapa en tela verde con el título en Schola; interior en papel, cuerpo de 10,5 a 11 pt.
- Créditos de figuras con la forma de arriba, y fuente y licencia en el colofón.
- En el sitio, cada cuaderno entra al índice de la Biblioteca con precio y enlace de pedido, y la pestaña Cuadernos aparece cuando salga el primero (decisión 4C).
