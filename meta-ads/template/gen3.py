"""Tee-first templates: the full tee stays large and uncovered; one small UI joke sits above it.

Widgets: chat, captcha, battery, dating. Run: node render.js $(python3 gen3.py)
"""
from gen import TEES, LOGO, HEAD

COPY = {
    'courage': dict(
        chat=dict(who='Manager', them='can you hop on a quick call?', me=None, headline='Every Monday, 9:01 AM.'),
        captcha=dict(label="I'm not scared of Monday", headline='Verification failed.'),
        battery=dict(title='Social Battery Low', body='5% remaining. Cancel all plans?', a='Dismiss', b='Cancel Plans',
                     headline='Scared, but fashionable.'),
        dating=dict(prompt='My most irrational fear', answer='“Can we talk?” with no context.', headline='Swipe right on fear.'),
    ),
    'snorlax': dict(
        chat=dict(who='Mom', them='beta gym gaya aaj?', me='on my way 🏃', headline='(He was not on his way.)'),
        captcha=dict(label="I'm a morning person", headline='Verification failed.'),
        battery=dict(title='Motivation Low', body='2% remaining. Take a nap?', a='Later', b='Nap',
                     headline='Just do it later.'),
        dating=dict(prompt='My love language', answer='Cancelling plans so we can both nap.', headline='Swipe right. Eventually.'),
    ),
    'anxiety': dict(
        chat=dict(who='Boss', them='we need to talk tomorrow', me=None, headline='Same-day anxiety.'),
        captcha=dict(label="I'm totally calm", headline='Verification failed.'),
        battery=dict(title='Peace of Mind Low', body='1% remaining. Overthink instead?', a='Not Now', b='Overthink',
                     headline='Delivered daily.'),
        dating=dict(prompt='I go crazy for', answer='Rereading a text 14 times before sending.', headline='Swipe right. Then panic.'),
    ),
}


def frame(t, widget_css, widget_html, headline):
    return HEAD + f'''
.ad{{width:1080px;height:1350px;background:{t['bg']}}}
.bg{{position:absolute;inset:0;background:url({t['img']}) 50% 100%/108% no-repeat}}
.w{{position:absolute;left:150px;right:150px;top:70px;font-family:Inter,sans-serif}}
{widget_css}
h1{{position:absolute;left:56px;right:56px;bottom:130px;text-align:center;font-family:var(--display);color:var(--ink);font-size:62px;line-height:1.02;letter-spacing:-.02em}}
.foot{{position:absolute;left:56px;right:56px;bottom:52px;display:flex;justify-content:space-between;align-items:center}}
.brand{{display:flex;align-items:center;gap:12px;font-family:var(--mono);font-weight:700;font-size:23px;letter-spacing:.04em;color:var(--ink)}}
.meta{{font-family:var(--mono);font-size:20px;letter-spacing:.16em;color:#5f574c}}
</style></head><body><div class="ad"><div class="bg"></div>
<div class="w">{widget_html}</div>
<h1>{headline}</h1>
<div class="foot"><div class="brand">{LOGO.format(s=36)} BRAINSICK BISCUIT</div><div class="meta">OVERSIZED &#183; 240 GSM</div></div>
</div></body></html>'''


def chat(t, c):
    me = (f'<div class="me">{c["me"]}</div>' if c['me']
          else '<div class="me dots"><i></i><i></i><i></i></div>')
    css = '''.w{display:flex;flex-direction:column;gap:12px}
.them{align-self:flex-start;background:#fff;border-radius:28px 28px 28px 8px;padding:16px 26px 18px;box-shadow:0 12px 30px rgba(40,30,20,.16);max-width:80%}
.them b{display:block;font-size:22px;color:var(--accent)}
.them p{font-size:32px;color:#111}
.me{align-self:flex-end;background:var(--accent);color:#fff;border-radius:28px 28px 8px 28px;padding:18px 26px;font-size:32px;box-shadow:0 12px 30px rgba(40,30,20,.16)}
.dots{display:flex;gap:10px;padding:26px 30px}
.dots i{width:16px;height:16px;border-radius:50%;background:#fff;opacity:.85}
.dots i:nth-child(2){opacity:.6}.dots i:nth-child(3){opacity:.35}'''
    return frame(t, css, f'<div class="them"><b>{c["who"]}</b><p>{c["them"]}</p></div>{me}', c['headline'])


def captcha(t, c):
    css = '''.cap{background:#F9F9F9;border:2px solid #D3D3D3;border-radius:6px;box-shadow:0 12px 30px rgba(40,30,20,.16);display:flex;align-items:center;gap:26px;padding:28px 30px}
.box{width:56px;height:56px;border:3px solid #C1C1C1;border-radius:4px;background:#fff;flex:0 0 auto}
.cap span{flex:1;font-size:32px;color:#222}
.rc{text-align:center;font-size:15px;color:#888;flex:0 0 auto}
.rc svg{display:block;margin:0 auto 4px}
.err{font-size:22px;color:#D93025;font-weight:600;margin-bottom:6px}
.cap .l{flex:1}
.cap .l span{display:block}'''
    ic = ('<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="#4A90E2" stroke-width="2.2">'
          '<path d="M20 12a8 8 0 1 1-2.3-5.6"/><path d="M20 4v5h-5"/></svg>')
    return frame(t, css, f'<div class="cap"><div class="box"></div><div class="l"><div class="err">&#9888; Please try again.</div><span>{c["label"]}</span></div><div class="rc">{ic}Privacy - Terms</div></div>', c['headline'])


def battery(t, c):
    css = '''.w{left:220px;right:220px}
.al{background:rgba(242,240,236,.97);border-radius:30px;overflow:hidden;box-shadow:0 16px 40px rgba(40,30,20,.2);text-align:center}
.al .tp{padding:28px 30px 24px}
.bat{display:inline-flex;align-items:center;gap:4px;margin-bottom:10px}
.bat .b{width:64px;height:30px;border:3px solid #111;border-radius:8px;padding:3px}
.bat .b i{display:block;width:12%;height:100%;background:#E5483B;border-radius:3px}
.bat .n{width:5px;height:12px;background:#111;border-radius:0 3px 3px 0}
.al b{display:block;font-size:31px;color:#111}
.al p{font-size:25px;color:#333;margin-top:6px}
.bt{display:flex;border-top:1.5px solid #cfcac2}
.bt div{flex:1;padding:18px;font-size:28px;color:#2F7BF5}
.bt div+div{border-left:1.5px solid #cfcac2;font-weight:700}'''
    return frame(t, css, f'<div class="al"><div class="tp"><div class="bat"><div class="b"><i></i></div><div class="n"></div></div>'
                         f'<b>{c["title"]}</b><p>{c["body"]}</p></div><div class="bt"><div>{c["a"]}</div><div>{c["b"]}</div></div></div>',
                 c['headline'])


def dating(t, c):
    css = '''.pr{position:relative;background:#fff;border-radius:26px;padding:26px 34px 30px;box-shadow:0 14px 36px rgba(40,30,20,.18)}
.pr small{font-size:24px;font-weight:600;color:#444}
.pr p{font-family:Georgia,serif;font-size:40px;line-height:1.15;color:#111;margin-top:8px;padding-right:70px}
.hb{position:absolute;right:20px;bottom:-26px;width:74px;height:74px;border-radius:50%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-size:38px;box-shadow:0 8px 20px rgba(0,0,0,.2)}'''
    return frame(t, css, f'<div class="pr"><small>{c["prompt"]}</small><p>{c["answer"]}</p><div class="hb">&#9829;</div></div>', c['headline'])


if __name__ == '__main__':
    names = []
    for key, t in TEES.items():
        for kind, fn in (('chat', chat), ('captcha', captcha), ('battery', battery), ('dating', dating)):
            name = f'final-{key}-{kind}'
            open(name + '.html', 'w').write(fn(t, COPY[key][kind]))
            names.append(f'{name}:1080:1350')
    print(' '.join(names))
