from PIL import Image, ImageDraw, ImageFont

W, H, M, N = 1080, 1350, 96, 5
TELA, HUESO, SUAVE = (45, 69, 53), (235, 232, 223), (183, 191, 176)
F = '/home/claude/muestrario/fonts/schola-'
def fnt(t, it=False): return ImageFont.truetype(F + ('italic' if it else 'regular') + '.ttf', t)

def fondo():
    im = Image.new('RGB', (W, H), TELA)
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for y in range(0, H, 3): d.line([(0, y), (W, y)], fill=(0, 0, 0, 13) if y % 6 else (255, 255, 255, 13))
    for x in range(0, W, 3): d.line([(x, 0), (x, H)], fill=(0, 0, 0, 13) if x % 6 else (255, 255, 255, 13))
    im.paste(ov, (0, 0), ov)
    return im, ImageDraw.Draw(im)

def txt(d, t, x, y, tam, col, it=False, der=False):
    f = fnt(tam, it)
    if der: x = W - M - d.textlength(t, font=f)
    d.text((x, y), t, font=f, fill=col, anchor='ls')

def parr(d, t, x, y, ancho, tam, inter, col, it=False):
    f = fnt(tam, it); lin, out = '', []
    for p in t.split(' '):
        pr = (lin + ' ' + p).strip()
        if d.textlength(pr, font=f) > ancho and lin: out.append(lin); lin = p
        else: lin = pr
    out.append(lin)
    for i, l in enumerate(out): d.text((x, y + i * inter), l, font=f, fill=col, anchor='ls')
    return y + (len(out) - 1) * inter

def marco(d, n):
    txt(d, 'Palabra de taller n.º 6', M, 130, 32, SUAVE); txt(d, f'{n} / {N}', 0, 130, 30, SUAVE, der=True)
    txt(d, 'soydemadera.com', M, 1270, 26, SUAVE); txt(d, 'Noviembre 2026', 0, 1270, 26, SUAVE, der=True)

def filete(d, y): d.rectangle([M, y, M + 140, y + 2], fill=(140, 152, 140))

def bloque(n, titulo, cuerpos):
    im, d = fondo(); marco(d, n)
    y = parr(d, titulo, M, 330, W - 2 * M, 72, 86, HUESO)
    filete(d, y + 60); y += 160
    for t, tam, col in cuerpos:
        y = parr(d, t, M, y, W - 2 * M, tam, round(tam * 1.38), col) + round(tam * 1.9)
    return im

L = []
im, d = fondo(); marco(d, 1)
txt(d, 'Fluencia', M, 560, 150, HUESO)
txt(d, 'creep · se pronuncia «krip»', M, 650, 40, SUAVE, it=True)
filete(d, 730)
parr(d, 'Por qué un estante cargado de libros se va combando con los años, aunque nadie le haya agregado peso.', M, 840, W - 2 * M, 46, 64, HUESO)
L.append(im)

L.append(bloque(2, 'La madera cede de a poco', [
    ('Cuando cargás un estante, baja enseguida un poco: es la flexión de siempre, y si sacás el peso vuelve.', 42, HUESO),
    ('Si la carga se queda puesta meses o años, la deformación sigue creciendo aunque el peso no cambie. Eso es la fluencia: una deformación que depende del tiempo.', 40, SUAVE)]))

L.append(bloque(3, 'Qué la hace crecer', [
    ('Una carga alta y permanente. Cuanto más cerca del límite que aguanta la pieza, más fluye.', 40, HUESO),
    ('La humedad. La madera húmeda fluye más que la seca, y los cambios de humedad de un ambiente a otro la aceleran.', 40, HUESO),
    ('El calor. A más temperatura, más fluencia.', 40, HUESO)]))

L.append(bloque(4, 'En el banco', [
    ('Acortá la luz. La flecha crece con el cubo de la distancia entre apoyos: con un 20 % menos de luz, el estante queda casi el doble de rígido.', 38, HUESO),
    ('Ganá altura. Un listón de canto en el frente rinde más que engrosar la tabla, porque la rigidez crece con el cubo de la altura.', 38, HUESO),
    ('Usá madera seca y de fibra recta, y no dejes cargas pesadas apoyadas para siempre en un voladizo.', 38, HUESO)]))

L.append(bloque(5, 'Y 47 palabras más', [
    ('Esta semana sumamos al diccionario de soydemadera.com los términos de resistencia y mecánica de la madera: tensión, flecha, pandeo, descuadre, corte rodante y otros.', 42, HUESO),
    ('Salen del capítulo 4 de Understanding Wood, de R. Bruce Hoadley. Cada uno con su pronunciación y una definición en palabras de taller.', 38, SUAVE)]))

for i, im in enumerate(L, 1): im.save(f'palabra6-{i}.jpg', quality=92)
print('ok')
