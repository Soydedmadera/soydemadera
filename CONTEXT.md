# Soy de Madera — Estado del Proyecto
**Última actualización:** 7 octubre 2026 (verificado contra el repo, commit `6d3449a`)
**Autor:** Abel José Anuzis — carpintero; abogado (UNC), maestría en Ciencias de la Ingeniería mención Ambiente

> Identidad pública: Abel se presenta como **carpintero**. El sitio y sus contenidos nuevos **no se asocian a la Spilimbergo / FAD / UPC**. Las menciones que quedan en el sitio están listadas en "Pendientes".

---

## Stack técnico

- **Frontend:** HTML estático puro (sin frameworks). CSS vanilla + JS vanilla.
- **Hosting:** Cloudflare Pages (migrado desde Netlify el 25/03/2026). Deploy automático por push a `main`.
- **Dominio:** soydemadera.com — registrado en Namecheap, DNS en Cloudflare
- **Repo:** https://github.com/Soydedmadera/soydemadera (rama `main`, única rama)
- **Biblioteca · estante Archivo:** Google Sheets + Apps Script (constante `AST_SCRIPT` en `index.html`)
- **Backend IA (sin integrar):** FastAPI + Python + Anthropic API (carpeta `backend/`)
- **Máquina de Abel:** Windows, Git Bash y PowerShell. Sin Python3 ni Node.js; `sed` no es confiable por los finales de línea CRLF.

## Flujo de deploy

```
Editar archivo local → git add . → git commit -m "descripción" → git push → Cloudflare despliega solo
```

Precauciones:
- El repo ya sufrió un commit destructivo que truncó `index.html` (recuperado con force-push). No hacer force-push ni reemplazar `index.html` entero sin comparar antes la cantidad de líneas.
- Ediciones de varias líneas: preparar el archivo completo y entregarlo, no armar scripts en la terminal de Abel.
- Antes de reportar algo como hecho, verificarlo en el repo o en el sitio en vivo.

## Estructura del repo

```
soydemadera/
├── index.html                        ← página principal (3354 líneas)
├── diccionario_carpinteria_v2.html
├── calculadora_pie_madera.html
├── conversor_imperial.html
├── cuando_el_mueble_es_arte.html     ← ensayo
├── historia_oficio_arte.html         ← ensayo "El arte y lo artesanal"
├── tp1_marqueteria.html              ← guía
├── guia_geometria_talla.html         ← guía (no está enlazada desde index ni en el sitemap)
├── tocar_madera_2026.html            ← nota sobre expositores y patrocinadores
├── img/
│   └── og-cuando-el-mueble-es-arte.jpg
├── maderas/
│   └── cedro.md                      ← ficha técnica cedro misionero
├── backend/
│   ├── main.py                       ← servidor FastAPI
│   ├── requirements.txt
│   ├── .env.example
│   └── chat_widget.html              ← widget de chat (sin integrar)
├── sitemap.xml
├── robots.txt
├── .gitignore                        ← excluye .env
├── netlify.toml                      ← legacy, ya no se usa
├── README.md                         ← instrucciones viejas del backend IA
└── CONTEXT.md
```

**No están en el repo** (se construyeron en chats pero nunca se subieron): `estudio_glosario.html`, `estudio_acabados.html`, `taller_digital.html`.

## Sistema visual (vigente desde el 7/10/2026)

Paleta apagada sobre fondo papel, con variante oscura automática (`prefers-color-scheme: dark`). Referencias: Nakashima Woodworkers, Krenov School, Lost Art Press. Reemplaza al sistema oscuro anterior (`#1a1209` + siena `#c47a2a` / ámbar `#e8a43a` / crema `#f5edd8`), que ya no se usa.

Los nombres de las variables se conservaron, pero **cambiaron de sentido**: `--nogal` ahora es el fondo claro y `--crema` es la tinta del texto.

| Rol | Variable | Claro | Oscuro |
|---|---|---|---|
| Fondo | `--nogal` | `#e9e7e1` | `#1f1d1a` |
| Fondo alterno | `--nogal-2` / `--roble` | `#e4e1da` / `#dfdcd4` | `#24221e` / `#2a2824` |
| Texto | `--crema` | `#2b2926` | `#ddd8ce` |
| Texto secundario | `--crema-dim` | `#6a655d` | `#9a9488` |
| Acento madera | `--siena` / `--ambar` | `#7b5d3f` / `#6b5138` | `#b89572` / `#c9a680` |
| Enlaces | `--azul` | `#4f6676` | `#9db2c0` |
| Pie | `--pie` | `#4a5c69` | `#2b363d` |
| Líneas | `--linea` | `#cfcbc2` | `#3a3732` |
| Verde | `--verde` | `#55663f` | `#8fa67a` |

- **Fuentes:** Fraunces (titulares) + Crimson Pro (cuerpo) + IBM Plex Mono (etiquetas)
- El azul grisáceo va solo en enlaces y pie. La navegación no lleva fondo.
- La paleta nueva está aplicada en `index.html`. Falta revisar una por una las páginas internas.
- Fuera del sistema tipográfico: `tp1_marqueteria.html` (DM Serif Display + DM Sans) y `guia_geometria_talla.html` (Cinzel + Libre Baskerville).
- Portada tipo cuaderno (una columna, fondo claro): prototipo aprobado en sandbox, sin aplicar. La sección "cuadernos" se agrega recién cuando haya contenido.

## `index.html` — estado actual

- Navegación por pestañas (JS vanilla), menú hamburguesa en mobile.
- Pestañas: Pilares, Diccionario, Herramientas, Maestros, Dónde estudiar, Sobre, Redes, **Biblioteca**, **Agenda**.
- **Biblioteca** (ex Astillas): tres estantes — Guías (TP1 Marquetería), Ensayos (El arte y lo artesanal; Cuando el mueble es arte) y Archivo (PDFs, videos y fotos desde Google Sheets). El enlace viejo `#astillas` redirige a `#biblioteca`. Los `id` internos siguen llamándose `astillas-*`.
- **Agenda:** Próximos — 23.º Seminario del Foro de la Madera de Entre Ríos (22/10/2026). Ya pasaron — Tocar Madera 2026.
- **Maestros:** perfiles de George Nakashima y Clara Porset (documentales, sin entrevista).
- **Dónde estudiar:** escuelas, maestros particulares y recursos autodidactas; quedan fichas de relleno ("Libro recomendado", "Canal de YouTube", "Curso online").
- **Diccionario:** 131 términos EN/ES/LT en 7 categorías (se sumó "Veta y figura").

## Pendientes

### Correcciones técnicas
- [ ] **Fuentes de `index.html`:** la hoja de Google Fonts apunta a una ruta local que no existe (`./Soy de Madera — …_files/css2`, línea 10). La portada no carga Fraunces, Crimson Pro ni IBM Plex Mono y cae en las fuentes de reemplazo. Hay que restaurar el enlace a `fonts.googleapis.com`.
- [ ] **Contraseña del panel de Biblioteca** en texto plano en el HTML público (`const AST_PWD`, línea 3137). Cambiarla y sacarla del código.
- [ ] El logo de la navegación usa una URL absoluta (`https://soydemadera.com/#`); la convención es ruta relativa.
- [ ] Aplicar la paleta nueva a las páginas internas y verificar cada una.
- [ ] Enlazar `guia_geometria_talla.html` desde Biblioteca y sumarla al sitemap, o retirarla.
- [ ] Actualizar o borrar `README.md` y `netlify.toml`.

### Desvincular el sitio de la FAD / UPC
- [ ] `index.html` línea 2409 (Sobre): "formación real en ebanistería (Spilimbergo / FAD / UPC, Córdoba)".
- [ ] `index.html` línea 2666 (Biblioteca): bajada de TP1 Marquetería.
- [ ] `diccionario_carpinteria_v2.html` línea 1284: mismo texto de Sobre.
- [ ] `historia_oficio_arte.html`: referencias a la cátedra y al prof. Alfonso Teresa (líneas 1090, 1096, 1279, 1285). Son cita de fuente: decidir si se conservan como crédito.
- [ ] La ficha de la Escuela Spilimbergo en "Dónde estudiar" es una entrada de directorio, no identidad: decidir si queda.
- [ ] Glosario del proyecto (`.docx`): quitar las menciones a la institución.

### Contenido y secciones
- [ ] Subir `estudio_glosario.html`, `estudio_acabados.html` y `taller_digital.html`, adaptados a la paleta nueva.
- [ ] Pestaña **Archivero Legal** (decidida, sin construir): artículo sobre derechos de autor de la obra de carpintería; después plantilla de acuerdo de taller, licencia CC BY 4.0 y modelo de declaración jurada de autoría.
- [ ] Maestros: entradas de Dan Bursztyn y Lucas Del Giudice, si aceptan.
- [ ] Completar las fichas de relleno de "Dónde estudiar".
- [ ] Más fichas en `maderas/`.

### Backend IA
- [ ] Integrar `chat_widget.html` en `index.html`
- [ ] Hospedar el backend en Railway o Render
- [ ] Limpiar proyectos viejos en Netlify

## Convenciones de código

- Archivos HTML autónomos: todo el CSS y el JS embebidos en el mismo archivo
- Sin frameworks ni dependencias externas salvo Google Fonts (CDN)
- Rutas relativas para links internos
- Links externos con `target="_blank"` y `rel="noopener noreferrer"`
- `box-sizing: border-box` global
- Breakpoint responsive: 900px
- Usar siempre las variables CSS de la paleta; no escribir colores sueltos

## Cómo responder en este proyecto

- Español rioplatense siempre (vos, te, etc.)
- Directo y técnico, sin vueltas ni lenguaje motivacional
- En carpintería Abel es aprendiz: explicar los procesos paso a paso cuando corresponda
- Abel no programa: el doble chequeo del código es responsabilidad del asistente
- Cada herramienta web: archivo HTML autónomo publicable en Cloudflare Pages
- Monetización presente desde el inicio, no como agregado posterior
- No usar listas de bullets para respuestas conversacionales
