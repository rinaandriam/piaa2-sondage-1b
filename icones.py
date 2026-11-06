# Icônes de l'appli Sondage 1B : fond orange (couleur du groupe « volonté et contribution »), « 1B » en blanc, coche.
import sys
from PIL import Image, ImageDraw, ImageFont
out = sys.argv[1]
BG = (197, 90, 17, 255); WHITE = (255, 255, 255, 255)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def make(size, maskable):
    S = size * 4
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if maskable: d.rectangle([0, 0, S, S], fill=BG); k = 0.62
    else: d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.22), fill=BG); k = 0.80
    f = ImageFont.truetype(FONT, int(S * 0.36 * k / 0.8))
    w = d.textlength('1B', font=f)
    d.text(((S - w) / 2, S * 0.20 + S * (0.8 - k) * 0.35), '1B', font=f, fill=WHITE)
    c = S / 2; y = S * 0.70 - S * (0.8 - k) * 0.15; s = S * 0.11 * k / 0.8
    d.line([(c - 1.6 * s, y), (c - 0.4 * s, y + 1.1 * s), (c + 1.8 * s, y - 1.2 * s)], fill=WHITE, width=int(S * 0.045 * k / 0.8), joint='curve')
    return im.resize((size, size), Image.LANCZOS)
make(192, False).save(f'{out}/icon-192.png')
make(512, False).save(f'{out}/icon-512.png')
make(512, True).save(f'{out}/maskable-512.png')
make(180, True).save(f'{out}/apple-touch-icon.png')
print('icones ok')
