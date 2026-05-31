import re

with open('C:/Users/aleja/boda-jorge-eva/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix remaining corrupt sequences
more_fixes = [
    ('\u00e2\u20ac\u201c', '\u2014'), ('\u00e2\u20ac\u2122', '\u2019'), ('\u00e2\u20ac\u0153', '\u201c'), ('\u00e2\u20ac\u009d', '\u201d'),
    ('\u00e2\u2020\u2019', '\u2192'), ('\u00e2\u0086\u2019', '\u2192'),
]
for bad, good in more_fixes:
    c = c.replace(bad, good)

# Story section
c = c.replace(
    '<h2>De un amanecer <em>a</em> otro</h2>',
    '<h2>Un amor que <em>eligi\u00f3</em> quedarse</h2>'
)
old_p1 = 'Nos conocimos una ma\u00f1ana de octubre, en un caf\u00e9 peque\u00f1o al pie de las monta\u00f1as de San Miguel. El cielo estaba rosa, el aire ol\u00eda a caf\u00e9 tostado y yo no sab\u00eda que ese caf\u00e9 ser\u00eda el primero de muchos.'
new_p1 = 'De entre toda la gente, nos encontramos. Y en ese encuentro descubrimos que el amor verdadero no llega con prisa \u2014 llega con certeza, con calma y con la sensaci\u00f3n de haber llegado a casa.'
c = c.replace(old_p1, new_p1)

old_p2 = 'Tres a\u00f1os, dos mudanzas y una caminata al Pico de Orizaba despu\u00e9s, Leonardo se hinc\u00f3 bajo el mismo cielo rosa y me pregunt\u00f3 si quer\u00eda seguir caminando a su lado. Dije s\u00ed antes de que terminara la pregunta.'
new_p2 = 'Hemos crecido juntos, aprendido juntos y elegido, todos los d\u00edas, estar el uno para el otro. Hoy queremos dar el paso m\u00e1s importante de nuestras vidas rodeados de las personas que m\u00e1s amamos.'
c = c.replace(old_p2, new_p2)

c = re.sub(r'<p data-reveal="line">Queremos celebrarlo contigo[^<]*</p>',
           '<p data-reveal="line">Con el coraz\u00f3n lleno de gratitud e ilusi\u00f3n, los invitamos a acompa\u00f1arnos en este d\u00eda tan especial. <em>Tu presencia lo es todo.</em></p>',
           c, flags=re.DOTALL)

# Locations
c = c.replace('San Miguel de Allende \u00b7 Guanajuato', 'Tijuana \u00b7 Baja California')
c = c.replace('Parroquia de<br>San Miguel Arc\u00e1ngel', 'Capilla de Nuestra Se\u00f1ora<br>del Sagrado Coraz\u00f3n')
c = c.replace('18:00 hrs', '14:30 hrs')
c = c.replace('Plaza Principal s/n<br>Centro, San Miguel de Allende<br>Guanajuato', 'Tijuana, B.C.')
c = c.replace(
    'href="https://www.google.com/maps/search/?api=1&amp;query=Parroquia%20de%20San%20Miguel%20Arc%C3%A1ngel%20San%20Miguel%20de%20Allende"',
    'href="https://www.google.com/maps/search/?api=1&amp;query=Capilla+Nuestra+Se%C3%B1ora+Sagrado+Coraz%C3%B3n+Tijuana"'
)
c = c.replace('Rosewood<br>San Miguel de Allende', 'Sal\u00f3n de Eventos<br>\u00c9bano 3895')
c = c.replace('19:30 hrs', '19:00 hrs')
c = c.replace('Nemesio Diez 11<br>Centro, San Miguel de Allende<br>Guanajuato', '\u00c9bano 3895, Cubillas Sur<br>22045 Tijuana, B.C.')
c = c.replace(
    'href="https://www.google.com/maps/search/?api=1&amp;query=Rosewood%20San%20Miguel%20de%20Allende"',
    'href="https://www.google.com/maps/search/?api=1&amp;query=Ebano+3895+Cubillas+Sur+Tijuana"'
)

# Countdown date
c = c.replace("new Date('2026-10-17T18:00:00-06:00')", "new Date('2026-08-29T14:30:00-07:00')")

# Itinerary times
c = c.replace('<div class="itin-time">17:30</div>', '<div class="itin-time">13:30</div>')
c = c.replace('<div class="itin-time">18:00</div>', '<div class="itin-time">14:30</div>')
c = c.replace('<div class="itin-time">19:30</div>', '<div class="itin-time">16:30</div>')
c = c.replace('<div class="itin-time">21:00</div>', '<div class="itin-time">19:00</div>')
c = c.replace('<div class="itin-time">22:30</div>', '<div class="itin-time">21:00</div>')
c = c.replace('<div class="itin-time">03:00</div>', '<div class="itin-time">01:00</div>')
c = c.replace(
    'Bienvenida con m\u00fasica en vivo y c\u00f3ctel de llegada en el patio principal.',
    'Bienvenida de invitados con m\u00fasica y c\u00f3ctel de llegada.'
)
c = c.replace(
    'Nos unimos en matrimonio en la Parroquia de San Miguel Arc\u00e1ngel.',
    'Ceremonia religiosa en la Capilla de Nuestra Se\u00f1ora del Sagrado Coraz\u00f3n.'
)

# Dress code swatches
c = c.replace(
    'background:linear-gradient(135deg,#1E2F4E,#0E1826)"></div><div class="swatch-n">Marino</div>',
    'background:linear-gradient(135deg,#3A5C44,#253D2C)"></div><div class="swatch-n">Verde bosque</div>'
)
c = c.replace(
    'background:linear-gradient(135deg,#4A6A8F,#3A5575)"></div><div class="swatch-n">Azul atardecer</div>',
    'background:linear-gradient(135deg,#7A9E82,#5A7E64)"></div><div class="swatch-n">Verde sage</div>'
)
c = c.replace(
    'background:linear-gradient(135deg,#C9A456,#8F7335)"></div><div class="swatch-n">Dorado</div>',
    'background:linear-gradient(135deg,#B8A87A,#8A7A50)"></div><div class="swatch-n">Champagne</div>'
)
c = c.replace(
    'background:linear-gradient(135deg,#E3B3BB,#C97B8B)"></div><div class="swatch-n">Rosa atardecer</div>',
    'background:linear-gradient(135deg,#E8E2D4,#C8C0AC)"></div><div class="swatch-n">Beige claro</div>'
)
c = c.replace(
    'background:linear-gradient(135deg,#D4C8B0,#B8AA8A)"></div><div class="swatch-n">Nude</div>',
    'background:linear-gradient(135deg,#F8F6EF,#E8E4D8)"></div><div class="swatch-n">Blanco marfil</div>'
)

# Dress code text
c = c.replace('black tie opcional', 'tuxedo o traje con corbata')
c = c.replace('Mujeres \u00b7 vestido largo &nbsp;\u00b7&nbsp; Caballeros \u00b7 traje oscuro', 'Mujeres \u00b7 vestido largo &nbsp;\u00b7&nbsp; Caballeros \u00b7 tuxedo o traje con corbata')

# date-hero dark background
c = c.replace('background:#1E2F4E;', 'background:#2A4034;')
c = c.replace('style="--from:var(--surface);--to:#1E2F4E"', 'style="--from:var(--surface);--to:#2A4034"')
c = c.replace('style="--from:#1E2F4E;--to:var(--surface)"', 'style="--from:#2A4034;--to:var(--surface)"')
c = c.replace('rgba(30,47,78,', 'rgba(42,64,52,')

# RSVP
c = c.replace(
    'antes del <b>17 de septiembre de 2026</b>',
    'antes del <b>31 de julio de 2026</b>'
)
c = c.replace(
    'href="https://wa.me/524152348907?text=Hola%21%20Confirmo%20mi%20asistencia%20a%20la%20boda%20de%20Paulina%20%26%20Leonardo"',
    'href="https://wa.me/526642510632?text=Hola%21%20Confirmo%20mi%20asistencia%20a%20la%20boda%20de%20Jorge%20%26%20Eva"'
)
c = c.replace('Fecha l\u00edmite \u00b7 17 Septiembre 2026', 'Fecha l\u00edmite \u00b7 31 Julio 2026')

# Footer
c = c.replace(
    '<div class="footer-names">Paulina <span class="amp">&amp;</span> Leonardo</div>',
    '<div class="footer-names">Jorge <span class="amp">&amp;</span> Eva</div>'
)
c = c.replace(
    '<div class="footer-date">XVII \u00b7 X \u00b7 2026 \u00b7 San Miguel de Allende</div>',
    '<div class="footer-date">XXIX \u00b7 VIII \u00b7 2026 \u00b7 Tijuana, B.C.</div>'
)

# Gifts - update titular
c = c.replace(
    'Paulina Montalvo C\u00e1rdenas',
    'Jorge Ernesto G\u00f3ngora Corona'
)
c = c.replace('No. 72158943', 'Por confirmar')

# QR album update
c = c.replace('paulina-leonardo-2026', 'jorge-eva-2026')
c = c.replace('color=1E2F4E&', 'color=3A5C44&')

with open('C:/Users/aleja/boda-jorge-eva/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Done, size:', len(c))
