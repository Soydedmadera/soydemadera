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
- **Paleta:** siena `#c47a2a` / ámbar `#e8a43a` / crema `#f5edd8`
- **Variables CSS:** `--ambar`, `--nogal`, `--crema`, `--font-mono`

## Archivos HTML — estado actual

### `index.html` (2920 líneas)
- Sistema de navegación por **pestañas** (no scroll continuo) — JS vanilla
- Hero como pantalla de inicio; logo vuelve al hero
- Secciones: Pilares, Diccionario, Herramientas, Maestros, Dónde estudiar, Sobre, Redes, **Astillas**
- **Sección Astillas:** muestra PDFs, videos YouTube/Vimeo, imágenes. Panel admin protegido con contraseña `madera2026` (texto plano en HTML, línea `const AST_PWD`). Datos en `localStorage` — persisten por dispositivo, no es backend real.
- Limitación conocida de Astillas: el contenido cargado solo se ve en el dispositivo donde se subió. Para visibilidad global hay que migrar a backend (Google Sheets, Supabase, etc.)

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
- [ ] Migrar Astillas a backend real (Google Sheets o Supabase) para visibilidad global
- [ ] Ficha técnica de más maderas en `maderas/`
- [ ] Limpiar proyectos viejos en Netlify

## Cómo responder en este proyecto

- Español rioplatense siempre (vos, te, etc.)
- Directo y técnico, sin vueltas
- En ebanistería Abel es novato — explicar procesos paso a paso cuando corresponda
- Cada herramienta web: archivo HTML autónomo publicable en Cloudflare Pages
- Monetización presente desde el inicio, no como afterthought
- No usar listas de bullets para respuestas conversacionales
