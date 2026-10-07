# Soy de Madera — Estado del Proyecto
**Última actualización:** 25 marzo 2026  
**Autor:** Abel José Anuzis — Abogado (UNC) + Tecnicatura Ebanistería Spilimbergo/FAD/UPC

---

## Stack técnico

- **Frontend:** HTML estático puro (sin frameworks). CSS vanilla + JS vanilla.
- **Hosting:** Cloudflare Pages (migrado desde Netlify el 25/03/2026)
- **Dominio:** soydemadera.com — registrado en Namecheap, DNS en Cloudflare
- **Repo:** https://github.com/Soydedmadera/soydemadera (rama `main`)
- **Backend IA (en desarrollo):** FastAPI + Python + Anthropic API (carpeta `backend/`)

## Flujo de deploy

```
Editar archivo local → git add . → git commit -m "descripción" → git push → Cloudflare despliega solo
```

## Estructura del repo

```
soydemadera/
├── index.html                        ← página principal
├── calculadora_pie_madera.html
├── conversor_imperial.html
├── diccionario_carpinteria_v2.html
├── maderas/
│   └── cedro.md                      ← ficha técnica cedro misionero
├── backend/
│   ├── main.py                       ← servidor FastAPI
│   ├── requirements.txt
│   ├── .env.example
│   └── chat_widget.html              ← widget de chat (pendiente integrar)
├── .gitignore                        ← excluye .env
├── netlify.toml                      ← legacy, ya no se usa
└── README.md
```

## Sistema visual

- **Fondo:** `#1a1209`
- **Fuentes:** Fraunces (titulares) + Crimson Pro (cuerpo) + IBM Plex Mono (etiquetas)
- **Paleta (desde 10/2026, "gama apagada"):** papel `#e9e7e1` de fondo, tinta `#2b2926`, madera `#7b5d3f` / `#6b5138` para acentos y botones, azul grisáceo `#4f6676` solo en enlaces y `#4a5c69` en el pie. Tiene variante oscura automática (`prefers-color-scheme: dark`) sobre `#1f1d1a`.
- **Variables CSS:** se conservan los nombres históricos, pero ya no significan lo que dicen: `--nogal` es el fondo, `--crema` el texto, `--siena` y `--ambar` los acentos madera, `--gris-tex` el texto secundario. Nuevas: `--azul`, `--pie`, `--linea`, `--verde`, `--error` y las ternas `--*-rgb` para usar con `rgba(var(--x-rgb), a)`.
- Aplicada en: `index.html`, diccionario, calculadora, conversor, los dos ensayos y la nota de Tocar Madera. Pendientes con su paleta vieja: `tp1_marqueteria.html` (ya era clara) y `guia_geometria_talla.html` (colores de diagramas).

## Archivos HTML — estado actual

### `index.html` (2920 líneas)
- Sistema de navegación por **pestañas** (no scroll continuo) — JS vanilla
- Hero como pantalla de inicio; logo vuelve al hero
- Secciones: Pilares, Diccionario, Herramientas, Maestros, Dónde estudiar, Sobre, Redes, **Biblioteca**, **Agenda**
- **Biblioteca** (ex Astillas, renombrada el 7/10/2026; el ancla vieja `#astillas` redirige): tres estantes. *Guías* y *Ensayos* son links fijos en el HTML; *Archivo* es la grilla de PDFs, videos YouTube/Vimeo e imágenes que se lee de una planilla de Google Sheets (`AST_CSV`) y se escribe vía Apps Script (`AST_SCRIPT`), visible para todos. Los identificadores internos conservan el prefijo `ast-` / `AST_`.
- **Agenda:** eventos escritos a mano en el HTML (`.ag-item`), separados en "Próximos" y "Ya pasaron". El banner superior (`.tm-banner`) apunta al próximo evento.
- Limitación conocida: la contraseña del panel admin está en texto plano (`const AST_PWD`) y el Apps Script acepta escrituras sin validar. La corrección real va en el Apps Script, no en el frontend.

### `calculadora_pie_madera.html`, `conversor_imperial.html`, `diccionario_carpinteria_v2.html`
- Sin modificaciones respecto a versión original

## Backend IA (pendiente)

- `backend/main.py` — servidor FastAPI que conecta con Claude via Anthropic API
- `backend/chat_widget.html` — widget listo para pegar en `index.html` antes de `</body>`
- Pendiente: integrar widget al sitio, correr servidor localmente, eventualmente hospedar en Railway/Render

## Convenciones de código

- Archivos HTML autónomos — todo CSS y JS embebido en el mismo archivo
- Sin frameworks ni dependencias externas salvo Google Fonts (CDN)
- Rutas relativas (no absolutas) para links internos
- `box-sizing: border-box` global
- Breakpoint responsive: 900px

## Pendientes

- [ ] Integrar `chat_widget.html` en `index.html`
- [ ] Hospedar backend en Railway o Render
- [x] Migrar Astillas a backend real (Google Sheets) — hecho; hoy es el estante Archivo de Biblioteca
- [ ] Validar la contraseña del panel admin en el Apps Script (hoy está en texto plano en el frontend)
- [ ] Ficha técnica de más maderas en `maderas/`
- [ ] Limpiar proyectos viejos en Netlify

## Cómo responder en este proyecto

- Español rioplatense siempre (vos, te, etc.)
- Directo y técnico, sin vueltas
- En ebanistería Abel es novato — explicar procesos paso a paso cuando corresponda
- Cada herramienta web: archivo HTML autónomo publicable en Cloudflare Pages
- Monetización presente desde el inicio, no como afterthought
- No usar listas de bullets para respuestas conversacionales
