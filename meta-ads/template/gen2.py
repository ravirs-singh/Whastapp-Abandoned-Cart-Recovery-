"""Second batch of Brainsick ad templates: lock screen, captcha, dating app, group chat.

Run: node render.js $(python3 gen2.py)
"""
from gen import TEES, LOGO, HEAD

EXTRA = {
    'courage': dict(
        lock=dict(time='9:01', date='Monday, 9 September', headline='Scared, but fashionable.', zoom=1.5, fy=0.30,
                  notes=[('💼', 'Manager', 'now', 'hey, got a minute? :)'),
                         ('🗓️', 'Calendar', '9:00', 'Quick sync (no agenda)'),
                         ('💬', 'Mom', '8:47', 'call me when free. its important'),
]),
        captcha="someone who's ready for Monday",
        dating=dict(prompt='My most irrational fear', answer='“Can we talk?” with no context.'),
        chat=dict(group='Office Besties', members='Priya, Rohan, You',
                  msgs=[('Priya', 'manager just said "quick call?" 💀'), ('Rohan', 'RIP bro'),
                        ('me', 'me rn'), ('Priya', 'wait where is this tee from')]),
    ),
    'snorlax': dict(
        lock=dict(time='11:47', date='Saturday, 14 September', headline='Just do it later.', zoom=1.5, fy=0.30,
                  notes=[('⏰', 'Alarm', '6:00', 'Gym (snoozed ×9)'),
                         ('🏃', 'Fitness', '9:12', "You haven't moved in 47 days"),
                         ('💬', 'Mom', '10:30', 'beta are you awake??'),
]),
        captcha="someone who's being productive",
        dating=dict(prompt='My love language', answer='Cancelling plans so we can both nap.'),
        chat=dict(group='Mom ❤️', members='online',
                  msgs=[('Mom', 'beta gym gaya aaj?'), ('me', 'spiritually, yes'), ('Mom', '😑'),
                        ('Mom', 'send link, papa needs one')]),
    ),
    'anxiety': dict(
        lock=dict(time='3:00', date='Tuesday, 17 September', headline='Same-day anxiety.', zoom=1.5, fy=0.30,
                  notes=[('📱', 'Screen Time', '2:58', 'Up 312% this week'),
                         ('💬', 'Boss', '2:41', 'we need to talk tomorrow'),
                         ('❓', 'Unknown number', '2:15', 'hi'),
]),
        captcha="someone who's totally calm",
        dating=dict(prompt='I go crazy for', answer='Rereading a text 14 times before sending.'),
        chat=dict(group='3AM Club', members='Ananya, Kabir, You',
                  msgs=[('Ananya', 'why is everyone awake'), ('Kabir', 'overthinking. u?'),
                        ('me', 'just got delivered'), ('Ananya', 'LMAOO link??')]),
    ),
}


def crop_bg(t, zoom, fx=0.5, fy=0.44, w=1080, h=1350):
    iw = w * zoom
    ih = iw * 1.25
    return (f"background:{t['bg']} url({t['img']}) no-repeat;background-size:{iw:.0f}px {ih:.0f}px;"
            f"background-position:{w/2 - fx*iw:.0f}px {h/2 - fy*ih:.0f}px")


def lock(t, e):
    l = e['lock']
    notes = ''.join(
        f'<div class="nt"><div class="ic">{ic}</div><div class="tx"><div class="r"><b>{a}</b><span>{tm}</span></div><p>{m}</p></div></div>'
        for ic, a, tm, m in l['notes'])
    return HEAD + f'''
.ad{{width:1080px;height:1350px;{crop_bg(t, l['zoom'], fy=l['fy'])}}}
.shade{{position:absolute;inset:0;background:linear-gradient(rgba(10,10,14,.6),rgba(10,10,14,.15) 45%,rgba(10,10,14,0) 60%,rgba(10,10,14,.65))}}
.clk{{position:absolute;top:44px;left:0;right:0;text-align:center;color:#fff;font-family:Inter,sans-serif}}
.clk .d{{font-size:30px;font-weight:600;opacity:.9}}
.clk .t{{font-size:160px;font-weight:700;letter-spacing:-.04em;line-height:1}}
.stack{{position:absolute;left:56px;right:56px;top:330px;display:flex;flex-direction:column;gap:14px}}
.nt{{display:flex;gap:20px;align-items:center;background:rgba(245,242,236,.82);backdrop-filter:blur(20px);border-radius:30px;padding:20px 24px;font-family:Inter,sans-serif}}
.ic{{width:62px;height:62px;border-radius:15px;background:#fff;display:flex;align-items:center;justify-content:center;font-size:34px;flex:0 0 auto}}
.tx{{flex:1;min-width:0}}
.r{{display:flex;justify-content:space-between;font-size:22px;color:#666}}
.r b{{color:#111;font-size:25px}}
.tx p{{font-size:26px;color:#111;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.hl{{position:absolute;left:56px;right:56px;bottom:110px;text-align:center;color:#fff;font-family:var(--display);font-size:60px;line-height:1.02;letter-spacing:-.02em}}
.brand{{position:absolute;left:0;right:0;bottom:50px;display:flex;justify-content:center;align-items:center;gap:12px;color:#fff;font-family:var(--mono);font-weight:700;font-size:22px;letter-spacing:.06em}}
</style></head><body><div class="ad"><div class="shade"></div>
<div class="clk"><div class="d">{l['date']}</div><div class="t">{l['time']}</div></div>
<div class="stack">{notes}</div>
<div class="hl">{l['headline']}</div>
<div class="brand">{LOGO.format(s=34)} BRAINSICK BISCUIT</div>
</div></body></html>'''


def captcha(t, e):
    spots = [(1.5, .5, .45), (2.6, .42, .44), (1.6, .5, .5), (2.2, .5, .5), (1.8, .5, .42),
             (3.2, .45, .43), (2.4, .55, .47), (3.0, .5, .45), (2.0, .48, .44)]
    tiles = ''.join(f'<div class="tl" style="{crop_bg(t, z, fx, fy, 250, 250)}"></div>' for z, fx, fy in spots)
    return HEAD + f'''
.ad{{width:1080px;height:1350px;background:var(--cream);align-items:center;padding-top:48px}}
.card{{width:820px;background:#fff;border:2px solid #d8d8d8;box-shadow:0 20px 50px rgba(0,0,0,.12);font-family:Inter,sans-serif}}
.hd{{background:#4A90E2;color:#fff;margin:12px;padding:24px 30px}}
.hd small{{font-size:24px}}
.hd b{{display:block;font-size:44px;line-height:1.1;margin:4px 0}}
.grid{{display:grid;grid-template-columns:repeat(3,250px);gap:8px;padding:0 12px 12px 23px}}
.tl{{width:250px;height:250px}}
.ft{{display:flex;justify-content:space-between;align-items:center;border-top:2px solid #e5e5e5;padding:18px 24px}}
.ft .ics{{display:flex;gap:26px;font-size:40px;color:#777}}
.ft .v{{background:#4A90E2;color:#fff;font-weight:700;font-size:28px;padding:18px 40px;border-radius:4px}}
.hl{{margin-top:36px;font-family:var(--display);font-size:54px;letter-spacing:-.02em;color:var(--ink)}}
.brand{{position:absolute;left:0;right:0;bottom:44px;display:flex;justify-content:center;align-items:center;gap:12px;font-family:var(--mono);font-weight:700;font-size:22px;letter-spacing:.06em}}
</style></head><body><div class="ad">
<div class="card"><div class="hd"><small>Select all images with</small><b>{e['captcha']}</b><small>If there are none, click skip</small></div>
<div class="grid">{tiles}</div>
<div class="ft"><div class="ics">&#8635; &#127911; &#9432;</div><div class="v">SKIP</div></div></div>
<div class="hl">Yeah. We skipped too.</div>
<div class="brand">{LOGO.format(s=34)} BRAINSICK BISCUIT</div>
</div></body></html>'''


def dating(t, e):
    d = e['dating']
    heart = '<div class="hb">&#9829;</div>'
    return HEAD + f'''
.ad{{width:1080px;height:1350px;background:#F5F1EA;padding:36px 48px 0;font-family:Inter,sans-serif}}
.top{{display:flex;justify-content:center;align-items:center;gap:12px;font-family:var(--mono);font-weight:700;font-size:22px;letter-spacing:.06em;margin-bottom:24px}}
.ph{{position:relative;height:720px;border-radius:26px;{crop_bg(t, 1.25, fy=0.47, w=984, h=720)}}}
.nm{{position:absolute;left:28px;bottom:24px;background:rgba(255,255,255,.92);border-radius:40px;padding:10px 24px;font-weight:700;font-size:28px}}
.pr{{position:relative;margin-top:22px;background:#fff;border-radius:26px;padding:40px 44px 46px}}
.pr small{{font-size:28px;font-weight:600;color:#333}}
.pr p{{font-family:Georgia,serif;font-size:62px;line-height:1.15;color:#111;margin-top:14px;padding-right:90px}}
.hb{{position:absolute;right:24px;bottom:24px;width:84px;height:84px;border-radius:50%;background:#fff;box-shadow:0 6px 20px rgba(0,0,0,.18);display:flex;align-items:center;justify-content:center;font-size:44px;color:var(--accent)}}
.acts{{position:absolute;left:0;right:0;bottom:44px;display:flex;justify-content:center;gap:60px}}
.acts div{{width:112px;height:112px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:54px;box-shadow:0 10px 26px rgba(0,0,0,.15)}}
.x{{background:#fff;color:#999}}
.lk{{background:var(--accent);color:#fff}}
</style></head><body><div class="ad">
<div class="top">{LOGO.format(s=32)} BRAINSICK BISCUIT</div>
<div class="ph"><div class="nm">Oversized, 240 GSM</div>{heart}</div>
<div class="pr"><small>{d['prompt']}</small><p>{d['answer']}</p>{heart}</div>
<div class="acts"><div class="x">&#10005;</div><div class="lk">&#9829;</div></div>
</div></body></html>'''


def chat(t, e):
    c = e['chat']
    out = []
    for who, m in c['msgs']:
        if who == 'me':
            out.append(f'<div class="me"><div class="img" style="{crop_bg(t, 1.15, fy=0.47, w=560, h=560)}"></div><p>{m}</p><span>2:14 &#10003;&#10003;</span></div>')
        else:
            out.append(f'<div class="them"><b>{who}</b><p>{m}</p><span>2:13</span></div>')
    return HEAD + f'''
.ad{{width:1080px;height:1350px;background:#EDE6DB;font-family:Inter,sans-serif}}
.hdr{{display:flex;align-items:center;gap:22px;background:#F7F4EE;padding:34px 40px;border-bottom:1px solid #ddd}}
.hdr .bk{{font-size:44px;color:#555}}
.av{{width:78px;height:78px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:700}}
.hdr b{{display:block;font-size:34px}}
.hdr small{{font-size:24px;color:#777}}
.body{{padding:28px 40px;display:flex;flex-direction:column;gap:16px}}
.them,.me{{max-width:74%;padding:16px 22px 12px;border-radius:24px;position:relative;box-shadow:0 1px 1px rgba(0,0,0,.08)}}
.them{{background:#fff;align-self:flex-start;border-top-left-radius:6px}}
.me{{background:#F4D9CC;align-self:flex-end;border-top-right-radius:6px;padding:10px 10px 12px}}
.them b{{font-size:22px;color:var(--accent)}}
p{{font-size:32px;color:#111;margin-top:2px}}
.me p{{padding:10px 12px 0}}
span{{display:block;text-align:right;font-size:18px;color:#8a8a8a;margin-top:4px}}
.me span{{color:#4A90E2;padding-right:8px}}
.img{{width:560px;height:560px;border-radius:18px}}
.brand{{position:absolute;right:30px;bottom:24px;display:flex;align-items:center;gap:10px;font-family:var(--mono);font-weight:700;font-size:20px;color:rgba(26,24,21,.6)}}
</style></head><body><div class="ad">
<div class="hdr"><div class="bk">&#8249;</div><div class="av">{c['group'][0]}</div><div><b>{c['group']}</b><small>{c['members']}</small></div></div>
<div class="body">{''.join(out)}</div>
<div class="brand">{LOGO.format(s=28)} BRAINSICK BISCUIT</div>
</div></body></html>'''


if __name__ == '__main__':
    names = []
    for key, t in TEES.items():
        for kind, fn in (('lockscreen', lock), ('captcha', captcha), ('dating', dating), ('chat', chat)):
            name = f'final-{key}-{kind}'
            open(name + '.html', 'w').write(fn(t, EXTRA[key]))
            names.append(f'{name}:1080:1350')
    print(' '.join(names))
