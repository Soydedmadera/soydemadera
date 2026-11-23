# Cartas de maderas: plantilla

Cada madera que pasa por la tapa del inicio tiene su carta, en la raíz del sitio: `madera_<nombre>.html` (por ejemplo `madera_lapacho_negro.html`). La carta reúne lo que se sabe de esa madera y lo lleva al taller. Para armar una nueva, copiar la carta más reciente y cambiar solo el contenido: el CSS y la estructura son los mismos en todas.

## Número

Orden de paso por la tapa: 1 palo santo, 2 quebracho colorado, 3 urunday, 4 lapacho negro, 5 cedro misionero, 6 caroba. La siguiente es la 7.

## La carta (arriba)

- Encabezado: «Maderas nativas argentinas» y «N.º x».
- Nombre común, nombre científico aceptado en la bibliografía argentina y familia.
- Foto de la tapa (900 × 700, la misma de `img/`).
- Debajo de la foto, el crédito en una línea (`<p class="carta-credito">`): «Foto: autor, licencia, recortada.» El nombre del autor enlaza al archivo original y la licencia, a su texto; si es de dominio público, «dominio público» va sin enlace. Si no se recortó, no se dice «recortada».
- Cuadrícula, siempre en este orden: Otros nombres y Dónde crece (a lo ancho); Color, Peso, Dureza, Durabilidad, En el taller, Protección (de a dos).
- Pie: floración y soydemadera.com.
- Debajo de la carta, una nota corta con las fuentes y las aclaraciones de los valores (humedad, especie de la que sale el dato). El crédito de la foto ya no va acá.

En la cuadrícula va lo esencial y comparable entre maderas. Los datos muy técnicos (flexión, elasticidad, contracción) no van.

## El texto (abajo)

No repite nada de la cuadrícula.

1. Cita literaria, si hay una de dominio público (autor muerto hace más de 70 años) verificada en dos ediciones. Solo el autor bajo la cita y un asterisco; la obra, el año, el contexto y la aclaración de dominio público van en Notas, al final. Si no hay cita verificada, no se pone.
2. En el taller, paso a paso: elegir la tabla, secar, cortar, cepillar, unir, tornear, terminar, cuidarse. Solo los pasos sobre los que haya datos.
3. Para qué se usa.
4. Si la comprás: CITES, normativa argentina, UICN si está confirmada, y cómo pedirla (nombre científico, procedencia).
5. Notas, Fuentes (numeradas, con enlace), Glosario y Seguir leyendo (enlaces a las otras cartas y a la lista de correo).

## Letra y créditos

Desde el 20/11/2026: 15 px como mínimo en todo, salvo pies de foto, fichas y notas, que van a 13,6 px (0,85 rem). Todos los créditos del sitio y de las láminas siguen la misma forma de una línea: «Qué se ve · Foto: autor, licencia o forma de uso, recortada».

## Reglas de datos

- Cada dato lleva su número de fuente. Si dos fuentes no coinciden, se dice.
- Si el dato es de otra especie o del grupo comercial, se aclara.
- Si no se encuentra un dato en una fuente seria, no se pone.
- Fuentes preferidas: CITES, CIRAD (Tropix), INTI, INTA, universidades argentinas, Embrapa, The Wood Database, Botanical Dermatology Database.

## Al publicar

Sumar la carta al sitemap, enlazarla desde el pie de la tapa («Ver la carta») y desde la franja, y agregarla al «Seguir leyendo» de las demás.
