"""
Soy de Madera — Backend con IA
================================
Servidor FastAPI que conecta el sitio con la API de Claude.
Puerto: 8000  →  http://localhost:8000

Endpoints:
  POST /api/chat     → envía un mensaje y recibe respuesta de la IA
  GET  /api/health   → verifica que el servidor está corriendo
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import anthropic
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# ── INICIALIZACIÓN ──────────────────────────────────────────────────────────

app = FastAPI(title="Soy de Madera API", version="1.0.0")

# CORS: permite que tu página HTML llame a este servidor
# En producción, reemplazá "*" por tu dominio real
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Cliente de Anthropic — lee la API key del archivo .env
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ── SYSTEM PROMPT ───────────────────────────────────────────────────────────
# Esto define la personalidad y conocimiento de la IA.
# Es como el "contrato de trabajo" que vimos en el módulo 2.

SYSTEM_PROMPT = """Sos el asistente oficial de "Soy de Madera", un sitio de divulgación 
técnica de carpintería y ebanistería en español, creado en Córdoba, Argentina.

Tu rol tiene tres modos según lo que necesite el usuario:

## MODO 1 — Asistente de carpintería
Respondés preguntas técnicas sobre carpintería y ebanistería con precisión y rigor de taller.
No romantizás el oficio: sos directo, técnico y práctico.
Usás terminología correcta en español (y mencionás el inglés entre paréntesis cuando es útil).
Ejemplos de preguntas: qué unión usar, cómo preparar una superficie, diferencia entre maderas.

## MODO 2 — Diccionario inteligente
Cuando alguien busca o pregunta por un término técnico, explicás:
- Traducción inglés ↔ español
- Pronunciación fonética del inglés
- Definición en contexto de taller
- Cuándo y para qué se usa

Términos que conocés (entre muchos otros):
Carcass, Face frame, Rail, Stile, Panel, Shelf, Drawer box, Dovetail joint, 
Mortise and tenon, Rabbet joint, Table saw, Router, Planer, Jointer, Chisel,
Plywood, MDF, Veneer, Edge banding, Hardwood, Softwood, PVA glue,
Kerf, Rip cut, Cross cut, Grain direction, Dry fit, Finishing, Stain, Varnish.

## MODO 3 — Generador de planes de corte
Cuando el usuario describe un mueble o proyecto, generás:
- Lista de piezas con dimensiones (largo × ancho × espesor en mm)
- Material recomendado para cada pieza
- Cantidad de tableros necesarios (estándar argentino: 2600×1830mm o 1830×2600mm)
- Notas sobre veta, tolerancias y kerf (~3mm por corte)
- Orden de corte recomendado

## REGLAS GENERALES
- Respondé siempre en español rioplatense (vos, te, etc.)
- Sé conciso: preferí respuestas de 2-4 párrafos salvo que pidan algo extenso
- Si no sabés algo con certeza, decilo — nunca inventes datos técnicos
- Si el usuario hace una pregunta fuera del mundo de la madera y la carpintería,
  respondé amablemente que solo podés ayudar con temas del oficio
- Usá formato Markdown para listas y tablas cuando aporte claridad"""

# ── MODELOS DE DATOS ─────────────────────────────────────────────────────────

class Message(BaseModel):
    """Un mensaje individual de la conversación."""
    role: str        # "user" o "assistant"
    content: str     # El texto del mensaje

class ChatRequest(BaseModel):
    """Lo que el frontend envía al backend."""
    messages: List[Message]  # Historial completo de la conversación

class ChatResponse(BaseModel):
    """Lo que el backend devuelve al frontend."""
    reply: str   # La respuesta de Claude

# ── ENDPOINTS ────────────────────────────────────────────────────────────────

@app.get("/api/health")
def health_check():
    """Verifica que el servidor está corriendo y la API key está configurada."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="ANTHROPIC_API_KEY no está configurada en el archivo .env"
        )
    return {
        "status": "ok",
        "message": "Servidor de Soy de Madera funcionando correctamente"
    }

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Endpoint principal: recibe el historial de mensajes y devuelve
    la respuesta de Claude.
    
    El frontend envía TODA la conversación en cada llamada porque
    Claude no tiene memoria entre llamadas — eso lo vimos en el módulo 1.
    """
    if not request.messages:
        raise HTTPException(status_code=400, detail="No hay mensajes en la solicitud")

    try:
        # Convertimos los mensajes al formato que espera la API de Anthropic
        api_messages = [
            {"role": msg.role, "content": msg.content}
            for msg in request.messages
        ]

        # Llamada a la API de Claude — acá es donde ocurre la magia
        response = client.messages.create(
            model="claude-sonnet-4-6",      # Modelo actual recomendado
            max_tokens=1024,                 # Máximo de tokens en la respuesta
            system=SYSTEM_PROMPT,            # El "contrato" de la IA
            messages=api_messages            # El historial de la conversación
        )

        # Extraemos el texto de la respuesta
        reply_text = response.content[0].text
        return ChatResponse(reply=reply_text)

    except anthropic.AuthenticationError:
        raise HTTPException(
            status_code=401,
            detail="API key inválida. Verificá tu archivo .env"
        )
    except anthropic.RateLimitError:
        raise HTTPException(
            status_code=429,
            detail="Límite de uso alcanzado. Esperá unos segundos y reintentá"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al llamar a la API: {str(e)}"
        )
