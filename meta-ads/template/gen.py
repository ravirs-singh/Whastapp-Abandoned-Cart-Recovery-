"""Generate the three approved Brainsick ad templates (notification, post, split) for every tee.

Add a tee to TEES and run: python3 gen.py && node ../render2.js <names printed>
"""
import html

LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="18" fill="#C0522C"/>'
        '<circle cx="14" cy="18" r="2.8" fill="#1A1815"/><circle cx="24" cy="18" r="2.8" fill="#1A1815"/>'
        '<path d="M13 25 Q20 31 27 25" stroke="#1A1815" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>')

ICONS = {
    'letter': lambda t: f'<span style="font-weight:800;font-size:40px">{t}</span>',
    'bell': lambda t: '<svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/></svg>',
    'box': lambda t: '<svg width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/></svg>',
}

TEES = {
    'courage': dict(
        img='courage.webp', bg='#C5BBB0', zoom=1.3,
        notif=dict(icon='letter', icon_txt='M', icon_bg='#4A5BD4', app='Manager', time='now',
                   msg='hey, got a minute? :)', headline='Every "quick call" ever.'),
        post=['my manager: can you hop on a quick call?', 'me:'],
        split=dict(them='Monday motivation.', them_list=['Rise &amp; grind', 'Inbox zero', 'Back-to-back calls'],
                   us='Monday horror.', us_list=['Unread: 47', '"Got a minute?"', '240 GSM comfort']),
    ),
    'snorlax': dict(
        img='tee.webp', bg='#D6CFC3',
        notif=dict(icon='bell', icon_txt='', icon_bg='#E0673D', app='Reminder: Gym', time='6:00 AM',
                   msg='snoozed 9 times. try again tomorrow?', headline='Just do it later.'),
        post=["me at 9:00: today I'm finally going to be productive", 'me at 9:05:'],
        split=dict(them='Just do it.', them_list=['5 AM alarms', 'Hustle', 'Cardio'],
                   us='Just do it later.', us_list=['Snooze &#215;9', '240 GSM comfort', 'A nap, probably']),
    ),
    'anxiety': dict(
        img='anxiety.webp', bg='#D4CDC1',
        notif=dict(icon='box', icon_txt='', icon_bg='#2E3A4B', app='Out for delivery', time='3:00 AM',
                   msg='1&#215; anxiety, arriving in 5 mins. again.', headline='Same-day anxiety.'),
        post=['added peace of mind to cart', 'what got delivered:'],
        split=dict(them='Delivered tomorrow.', them_list=['Order tracking', 'Easy returns', 'Peace of mind'],
                   us='Anxiety. Delivered daily.', us_list=['Overthinking &#215;&#8734;', '240 GSM comfort', '3 AM thoughts, free']),
    ),
}

HEAD = '<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="base.css"><style>'


def notif(t):
    n = t['notif']
    return HEAD + f'''
.ad{{width:1080px;height:1350px;background:{t['bg']}}}
.bg{{position:absolute;inset:0;background:url({t['img']}) 50% 100%/108% no-repeat}}
.n{{position:absolute;left:150px;right:150px;top:92px;background:rgba(251,249,243,.95);border-radius:34px;padding:26px 30px;display:flex;gap:22px;align-items:center;box-shadow:0 24px 50px rgba(40,30,20,.22);font-family:Inter,sans-serif}}
.ic{{width:78px;height:78px;border-radius:20px;background:{n['icon_bg']};color:#fff;display:flex;align-items:center;justify-content:center;flex:0 0 auto}}
.n .t{{flex:1;min-width:0}}
.n .r{{display:flex;justify-content:space-between;font-size:24px;color:#7a7a7a}}
.n .r b{{color:#111;font-weight:700;font-size:28px}}
.n p{{font-size:29px;color:#111;margin-top:6px}}
h1{{position:absolute;left:56px;right:56px;bottom:130px;text-align:center;font-family:var(--display);color:var(--ink);font-size:62px;line-height:1.02;letter-spacing:-.02em}}
.foot{{position:absolute;left:56px;right:56px;bottom:52px;display:flex;justify-content:space-between;align-items:center}}
.brand{{display:flex;align-items:center;gap:12px;font-family:var(--mono);font-weight:700;font-size:23px;letter-spacing:.04em;color:var(--ink)}}
.meta{{font-family:var(--mono);font-size:20px;letter-spacing:.16em;color:#5f574c}}
</style></head><body><div class="ad"><div class="bg"></div>
<div class="n"><div class="ic">{ICONS[n['icon']](n['icon_txt'])}</div><div class="t"><div class="r"><b>{n['app']}</b><span>{n['time']}</span></div><p>{n['msg']}</p></div></div>
<h1>{html.escape(n['headline'])}</h1>
<div class="foot"><div class="brand">{LOGO.format(s=36)} BRAINSICK BISCUIT</div><div class="meta">OVERSIZED &#183; 240 GSM</div></div>
</div></body></html>'''


def post(t):
    lines = '<br><br>'.join(html.escape(l) for l in t['post'])
    return HEAD + f'''
body{{background:#fff}}
.ad{{width:1080px;height:1350px;background:#fff;padding:56px 60px 0;font-family:Inter,sans-serif}}
.who{{display:flex;align-items:center;gap:18px;margin-bottom:34px}}
.who .av{{width:84px;height:84px;border-radius:50%;background:var(--cream);display:flex;align-items:center;justify-content:center}}
.who b{{font-size:32px;font-weight:700;display:block}}
.who small{{font-size:26px;color:#6b7280}}
.post{{font-size:50px;line-height:1.28;font-weight:500;color:#0f1419;margin-bottom:40px}}
.photo{{flex:1;min-height:0;margin-bottom:24px;border-radius:30px;overflow:hidden;border:1px solid #e5e7eb;background:{t['bg']} url({t['img']}) 50% 42%/{t.get('zoom',1.12)*100:.0f}% auto no-repeat}}
</style></head><body><div class="ad">
<div class="who"><div class="av">{LOGO.format(s=44)}</div><div><b>Brainsick Biscuit</b><small>@brainsick.in</small></div></div>
<div class="post">{lines}</div>
<div class="photo"></div>
</div>
</body></html>'''


def split(t):
    s = t['split']
    li = lambda xs: ''.join(f'<li>{x}</li>' for x in xs)
    return HEAD + f'''
.ad{{width:1080px;height:1350px}}
.top{{display:flex;height:480px}}
.half{{flex:1;padding:54px 48px;display:flex;flex-direction:column;justify-content:space-between}}
.them{{background:#E4E0D6;color:#8A8377}}
.us{{background:var(--accent);color:#fff}}
.lbl{{font-family:var(--mono);font-size:24px;letter-spacing:.18em}}
.q{{font-family:var(--display);font-size:54px;line-height:1.02}}
.them .q{{text-decoration:line-through;text-decoration-thickness:8px;text-decoration-color:var(--accent)}}
ul{{list-style:none;font-family:var(--mono);font-size:22px;line-height:1.7}}
.photo{{flex:1;min-height:0;overflow:hidden;position:relative;background:{t['bg']} url({t['img']}) 50% 38%/cover no-repeat}}
.bar{{position:absolute;left:40px;right:40px;bottom:40px;display:flex;justify-content:space-between;align-items:center;background:var(--surface);border-radius:60px;padding:16px 18px 16px 26px}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:700;font-size:24px}}
.cta{{background:var(--ink);color:#fff;border-radius:40px;padding:18px 34px;font-weight:700;font-size:24px;letter-spacing:.06em}}
</style></head><body><div class="ad">
<div class="top">
 <div class="half them"><div class="lbl">THEM</div><div class="q">{s['them']}</div><ul>{li(s['them_list'])}</ul></div>
 <div class="half us"><div class="lbl">US</div><div class="q">{s['us']}</div><ul>{li(s['us_list'])}</ul></div>
</div>
<div class="photo"><div class="bar"><div class="brand">{LOGO.format(s=40)} BRAINSICK BISCUIT</div><div class="cta">SHOP NOW &#8594;</div></div></div>
</div></body></html>'''


if __name__ == '__main__':
    names = []
    for key, t in TEES.items():
        for kind, fn in (('notification', notif), ('post', post), ('split', split)):
            name = f'final-{key}-{kind}'
            open(name + '.html', 'w').write(fn(t))
            names.append(f'{name}:1080:1350')
    print(' '.join(names))
