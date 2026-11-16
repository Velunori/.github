#!/usr/bin/env python3
"""Compose the organization overview from local native product previews.
Run from this multi-repository workspace; no network assets or user data.
"""
import base64
from pathlib import Path
import shutil
import subprocess
import tempfile

repo = Path(__file__).resolve().parents[1]
workspace = repo.parent
screens = workspace / 'velunori.github.io/assets/screens'

def embedded(path):
    mime = 'image/svg+xml' if path.suffix == '.svg' else 'image/png'
    return 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()

def shot(name, title, x, y, width, crop=None):
    """Place a preview; crop trims a panel's empty lower area (source pixels)."""
    source = screens / (name + '.png')
    img = f'<img src="{embedded(source)}">'
    if crop:
        native = int(subprocess.run(['magick', 'identify', '-format', '%w', str(source)],
            check=True, capture_output=True, text=True).stdout)
        img = f'<div class="crop" style="height:{round(crop * width / native)}px">{img}</div>'
    return f'<figure style="left:{x}px;top:{y}px;width:{width}px"><figcaption>{title}</figcaption>{img}</figure>'

wallpaper = embedded(workspace / 'velunori.github.io/assets/dusk.png')
mark = embedded(workspace / 'velunori.github.io/assets/mark.svg')
html = '''<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box}html,body{margin:0;width:2400px;height:1740px;overflow:hidden}
body{background:#19191f;color:#eeedf3;font-family:Arial,sans-serif}
header{position:absolute;left:86px;right:86px;top:60px;display:flex;align-items:center;justify-content:space-between}
.brand{display:flex;align-items:center;gap:22px;font:76px Georgia,serif;letter-spacing:-2px}.brand img{width:60px;height:60px}
.tagline{text-align:right;color:#bbb5c9;font-size:28px;line-height:1.5}
.desktop{position:absolute;left:64px;top:218px;width:2272px;height:1322px;border:1px solid #55505f;border-radius:30px;overflow:hidden;background:linear-gradient(#11101822,#11101855),url(WALLPAPER) center/cover}
.bar{position:absolute;top:30px;height:54px;border:1px solid #66606e;border-radius:28px;background:#202026ed;display:flex;align-items:center;gap:26px;padding:0 24px;font-size:23px;color:#c4aff1;box-shadow:0 12px 30px #0003}
.bar.left{left:32px}.bar.center{left:50%;transform:translateX(-50%);color:#eeedf3;min-width:380px;justify-content:center}.bar.right{right:32px;min-width:250px;justify-content:center;color:#c4aff1}.bar img{width:25px;height:25px}.dots{display:flex;gap:9px}.dots i{width:7px;height:7px;background:#8c839a;border-radius:4px}.dots i:first-child{width:24px;background:#c4aff1}
figure{position:absolute;margin:0}figcaption{font-size:25px;color:#f3effb;letter-spacing:.3px;margin:0 0 12px 4px;text-shadow:0 2px 8px #000}
figure>img{display:block;width:100%;height:auto;border-radius:19px;box-shadow:0 20px 45px #07050c77;border:1px solid #635c6d66}
.crop{overflow:hidden;border-radius:19px;box-shadow:0 20px 45px #07050c77;border:1px solid #635c6d66;background:#202026}.crop>img{display:block;width:100%;height:auto}
.caption{position:absolute;bottom:26px;left:40px;color:#d7cee4;font-size:22px;letter-spacing:1px}.caption span{color:#b8abc9}
footer{position:absolute;left:86px;right:86px;top:1580px;display:flex;justify-content:space-between;align-items:start}
.footer-title{font:44px Georgia,serif;letter-spacing:-.5px}.footer-detail{margin-top:16px;color:#aaa4b6;font-size:25px}.footer-right{text-align:right;color:#c4aff1;font-size:25px;line-height:1.6}
</style></head><body>
<header><div class="brand"><img src="MARK">Velunori</div><div class="tagline">Your desktop, together.<br>Nine components for Omarchy.</div></header>
<div class="desktop">
<div class="bar left"><img src="MARK"><div class="dots"><i></i><i></i><i></i><i></i></div></div>
<div class="bar center">09:41 <span style="color:#aaa4b6;font-size:20px">· Friday, 13 November</span></div>
<div class="bar right">♫ <span style="color:#a0ddbf">↗</span> ◌ <span style="color:#aaa4b6">Floating Bars</span></div>
'''.replace('WALLPAPER',wallpaper).replace('MARK',mark)
html += shot('menu','Menu',44,180,600)
html += shot('appearance','Floating Bars · Appearance',710,144,420,crop=520)
html += shot('clock','Clock & Calendar',1180,178,370)
html += shot('control-center','Control Center',1610,146,410)
html += shot('notifications','Notifications',44,720,370)
html += shot('weather','Weather',452,800,320,crop=366)
html += shot('update','Update window',830,826,600)
html += shot('lockscreen','Serene lock screen',1510,820,650)
html += '''<div class="caption">DUSK <span>· Wallpaper, palette &amp; window styling</span></div></div>
<footer><div><div class="footer-title">One palette. A whole desktop.</div><div class="footer-detail">Choose the full suite, or just the components you need.</div></div><div class="footer-right">github.com/Velunori<br><span style="color:#aaa4b6;font-size:21px">Composition of native previews · Sample data</span></div></footer>
</body></html>'''
output = repo / 'profile/assets/velunori-suite.png'
output.parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(prefix='velunori-suite-render-') as profile:
    source = Path(profile) / 'velunori-suite.html'
    source.write_text(html)
    subprocess.run([shutil.which('chromium') or 'chromium','--headless','--no-sandbox','--disable-gpu',
        '--disable-dev-shm-usage','--no-first-run','--hide-scrollbars','--force-device-scale-factor=1',
        '--window-size=2400,1740','--virtual-time-budget=1500','--user-data-dir='+profile+'/chrome',
        '--screenshot='+str(output),source.as_uri()],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=45)
print(output)
