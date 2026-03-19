# Soy de Madera — Integración con IA

## Estructura del proyecto

```
soydemadera/
├── index.html                  ← tu página (ya corregida)
├── calculadora_pie_madera.html
├── conversor_imperial.html
├── diccionario_carpinteria_v2.html
└── backend/
    ├── main.py                 ← el servidor de IA
    ├── requirements.txt        ← dependencias de Python
    ├── .env.example            ← plantilla para tu API key
    ├── .env                    ← TU archivo con la key real (no subir a git)
    └── .gitignore
```

---

## Paso 1 — Conseguir la API key

1. Entrá a https://console.anthropic.com
2. Creá una cuenta
3. Andá a **API Keys** → **Create Key**
4. Copiá la key (empieza con `sk-ant-...`)

---

## Paso 2 — Configurar el backend

```bash
# Entrar a la carpeta del backend
cd backend

# Crear el archivo .env con tu API key real
cp .env.example .env
# Abrí el archivo .env con cualquier editor y pegá tu key
```

---

## Paso 3 — Instalar Python y dependencias

Si no tenés Python instalado: https://python.org/downloads

```bash
# Dentro de la carpeta backend:

# Crear entorno virtual (buena práctica — aisla las dependencias)
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt
```

---

## Paso 4 — Arrancar el servidor

```bash
# Dentro de la carpeta backend, con el entorno virtual activado:
uvicorn main:app --reload

# Deberías ver algo así:
# INFO:     Uvicorn running on http://127.0.0.1:8000
# INFO:     Application startup complete.
```

Verificá que funciona abriendo en el navegador:
→ http://localhost:8000/api/health

---

## Paso 5 — Integrar el widget en index.html

1. Abrí el archivo `chat_widget.html`
2. Copiá TODO el contenido
3. Pegalo en tu `index.html` justo antes de la etiqueta `</body>`

---

## Paso 6 — Probar

1. Con el servidor corriendo, abrí tu `index.html` en el navegador
2. Vas a ver un botón 🪵 flotante en la esquina inferior derecha
3. Hacé clic y empezá a chatear

---

## ¿Qué hace cada archivo?

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `main.py` | El servidor backend | Recibe mensajes del chat y llama a Claude |
| `requirements.txt` | Lista de librerías | Python las instala automáticamente |
| `.env` | Variables secretas | Guarda tu API key de forma segura |
| `chat_widget.html` | El chat en la web | El botón y panel de chat para pegar en index.html |

---

## El stack de tu proyecto (ahora con IA)

```
Frontend (navegador)
  └── HTML + CSS + JavaScript vanilla
        └── Llama al backend via fetch()

Backend (tu computadora)
  └── Python + FastAPI
        └── Llama a la API de Anthropic

IA (en la nube de Anthropic)
  └── Claude Sonnet 4.6
        └── Responde con conocimiento de carpintería
```

---

## Costos aproximados

- La API de Anthropic cobra por tokens (pedazos de texto)
- Una respuesta típica del chat usa ~500-1000 tokens
- Con el crédito inicial gratuito podés hacer miles de consultas de prueba
- Para un sitio pequeño, el costo mensual es de pocos dólares

---

## Próximos pasos cuando quieras escalar

- **Hospedar el backend**: Railway, Render o Fly.io (todos tienen plan gratuito)
- **Variable de entorno en producción**: configura la API key en el panel del hosting
- **CORS en producción**: reemplazá `allow_origins=["*"]` por tu dominio real
