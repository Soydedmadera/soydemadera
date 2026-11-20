// Plantilla común de láminas de Instagram (decisión 5A del 20/11/2026).
// Misma línea que el sitio y los cuadernos: tela verde, Schola SdM regular, crédito de una línea.
// Reglas: sin contador de láminas («1 / 5»), sin emojis, sin mayúsculas espaciadas;
// cabecera, pie y créditos a 36 px como mínimo (se leen en el celular); cuerpo de 44 px o más.

const SDM = {
  W: 1080, H: 1350, M: 96,
  TELA: '#2d4535', HUESO: '#ebe8df', SUAVE: '#b7bfb0', PAPEL: '#ebebe6', TINTA: '#1c1c1a', GRIS: '#5f5e58',
  FUENTE: '"Schola SdM"',
  MIN: 36,   // tamaño mínimo de cualquier texto
};

SDM.cargarFuentes = async function () {
  await document.fonts.load(`400 40px ${SDM.FUENTE}`);
  await document.fonts.load(`italic 400 40px ${SDM.FUENTE}`);
};

SDM.cargarImagen = function (src) {
  return new Promise((ok, mal) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => mal(new Error('No cargó ' + src)); i.src = src; });
};

// Fondo de tela: trama fina, como la tapa de un cuaderno encuadernado
SDM.fondo = function (c) {
  const { W, H } = SDM;
  c.fillStyle = SDM.TELA; c.fillRect(0, 0, W, H);
  c.globalAlpha = 0.05;
  for (let y = 0; y < H; y += 3) { c.fillStyle = y % 6 ? '#000' : '#fff'; c.fillRect(0, y, W, 1); }
  for (let x = 0; x < W; x += 3) { c.fillStyle = x % 6 ? '#000' : '#fff'; c.fillRect(x, 0, 1, H); }
  c.globalAlpha = 1;
};

SDM.texto = function (c, t, x, y, tam, color, estilo = '') {
  tam = Math.max(tam, SDM.MIN);
  c.font = `${estilo} 400 ${tam}px ${SDM.FUENTE}`; c.fillStyle = color; c.fillText(t, x, y);
};

SDM.derecha = function (c, t, y, tam, color) {
  tam = Math.max(tam, SDM.MIN);
  c.font = `400 ${tam}px ${SDM.FUENTE}`;
  SDM.texto(c, t, SDM.W - SDM.M - c.measureText(t).width, y, tam, color);
};

// Párrafo con corte de línea; devuelve la línea de base de la última línea
SDM.parrafo = function (c, t, x, y, ancho, tam, color, estilo = '', interlinea = 1.38) {
  tam = Math.max(tam, SDM.MIN);
  c.font = `${estilo} 400 ${tam}px ${SDM.FUENTE}`; c.fillStyle = color;
  const paso = Math.round(tam * interlinea);
  let linea = '', lineas = [];
  for (const p of t.split(' ')) {
    const prueba = linea ? linea + ' ' + p : p;
    if (c.measureText(prueba).width > ancho && linea) { lineas.push(linea); linea = p; } else linea = prueba;
  }
  lineas.push(linea);
  lineas.forEach((l, i) => c.fillText(l, x, y + i * paso));
  return y + (lineas.length - 1) * paso;
};

// Cabecera: solo el nombre de la serie (sin «n / total»)
SDM.cabecera = function (c, serie) { SDM.texto(c, serie, SDM.M, 140, 36, SDM.SUAVE); };

// Pie: sitio y mes
SDM.pie = function (c, mes) {
  SDM.texto(c, 'soydemadera.com', SDM.M, 1262, 36, SDM.SUAVE);
  SDM.derecha(c, mes, 1262, 36, SDM.SUAVE);
};

SDM.filete = function (c, y) { c.fillStyle = 'rgba(183,191,176,.45)'; c.fillRect(SDM.M, y, 140, 2); };

// Lámina pegada: un papel claro sobre la tela con una foto o un croquis, y el crédito de una línea debajo.
// credito sigue la forma del sitio: «Qué se ve · Foto: autor, licencia, recortada».
SDM.lamina = function (c, img, x, y, w, h, credito) {
  c.fillStyle = 'rgba(0,0,0,.18)'; c.fillRect(x + 6, y + 8, w, h);   // sombra corta, de papel apoyado
  c.fillStyle = SDM.PAPEL; c.fillRect(x, y, w, h);
  const pad = 22, iw = w - 2 * pad, ih = h - 2 * pad;
  if (img) {
    // recorte centrado (cover) dentro del papel
    const r = Math.max(iw / img.width, ih / img.height), sw = iw / r, sh = ih / r;
    c.drawImage(img, (img.width - sw) / 2, (img.height - sh) / 2, sw, sh, x + pad, y + pad, iw, ih);
  }
  // devuelve la línea de base de la última línea del crédito (o el borde inferior del papel)
  return credito ? SDM.parrafo(c, credito, x, y + h + 62, w, 36, SDM.SUAVE) : y + h;
};

// Guarda cada lámina con un enlace de descarga (no hace falta servidor)
SDM.publicar = function (cv, nombre) {
  const fig = document.createElement('figure');
  const a = document.createElement('a'); a.download = nombre; a.textContent = 'Descargar ' + nombre;
  a.href = cv.toDataURL('image/jpeg', 0.92);
  fig.appendChild(cv); fig.appendChild(document.createElement('br')); fig.appendChild(a);
  document.getElementById('laminas').appendChild(fig);
};

SDM.generar = async function (laminas, prefijo) {
  await SDM.cargarFuentes();
  for (let i = 0; i < laminas.length; i++) {
    const cv = document.createElement('canvas'); cv.width = SDM.W; cv.height = SDM.H;
    await laminas[i](cv.getContext('2d'));
    SDM.publicar(cv, `${prefijo}-${i + 1}.jpg`);
  }
  document.getElementById('estado').textContent = `Listo: ${laminas.length} láminas`;
};
