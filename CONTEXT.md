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
