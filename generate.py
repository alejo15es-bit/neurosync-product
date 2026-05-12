#!/usr/bin/env python3
import json
import os
import subprocess

# 1. Crear directorio de assets
os.makedirs('assets', exist_ok=True)

# 2. Cargar configuración (solo metadata)
with open('config.json', 'r') as f:
    config = json.load(f)

print(f"📦 Producto: {config['product_name']}")
print(f"💰 Precio: ${config['price']}")

# 3. DEFINIR GUIONES AQUÍ (Seguro, sin problemas de JSON)
scripts = [
    """Welcome to NeuroSync. Session One: Morning Mental Reset.
    
    Before your phone buzzes with emails, before Slack notifications pile up, this is your space. Just twelve minutes. Just you.
    
    If your mind feels like a browser with too many tabs open, you're not broken. You're human in an inhuman pace. Let's reset.
    
    Find a comfortable position. Shoulders away from your ears. Jaw unclenched. 
    Breathe in through your nose slowly... 2... 3... 4...
    Hold gently... 2... 3... 4... 5... 6... 7...
    Release through your mouth like a sigh... 2... 3... 4... 5... 6... 7... 8...
    
    Notice the space that just opened. This is your mental bandwidth returning.
    I control my attention. Not the algorithm. Not the ping.
    
    End of Session One.""",

    """NeuroSync. Session Two: Work Focus Calm.
    
    You're at your desk. Or about to start work. This is your ten-minute reset.
    Sit comfortably. Feet flat on floor. Hands resting. 
    We're shifting from reactive to responsive.
    
    Breathe in... 2... 3... 4...
    Hold... 2... 3... 4... 5... 6... 7...
    Out... 2... 3... 4... 5... 6... 7... 8...
    
    Now, visualize your attention as a spotlight.
    Aim it at ONE thing. Single-tasking is your superpower.
    
    Single focus. Single task. Single breath. I choose depth over speed.
    
    End of Session Two.""",

    """NeuroSync. Session Three: Evening Digital Detox.
    
    The workday is done. But your mind is still scrolling. Still plugged in.
    This is your disconnection ritual. Fifteen minutes to unplug from digital and plug into yourself.
    
    Lie down or sit comfortably. This is permission to stop.
    
    Breathe in through nose... 2... 3... 4...
    Hold... 2... 3... 4... 5... 6... 7...
    Out through mouth... 2... 3... 4... 5... 6... 7... 8...
    
    Imagine a cable connecting you to the digital world.
    With your next breath, gently unplug. Feel the freedom.
    I disconnect to reconnect.
    
    End of Session Three."""
]

# 4. Generar archivos de texto y Audio
for i, script_text in enumerate(scripts, 1):
    # Limpiar texto para audio (una sola línea)
    script_clean = script_text.replace('\n', ' ').replace('"', "'")
    
    txt_file = f'session{i}.txt'
    mp3_file = f'assets/neurosync_0{i}_session.mp3'
    
    with open(txt_file, 'w') as f:
        f.write(script_clean)
    
    print(f"🎙️ Generando Audio {i}...")
    # Ejecutar edge-tts
    subprocess.run(['edge-tts', '--voice', 'en-US-AriaNeural', '--text-file', txt_file, '--write-media', mp3_file])
    
    print(f"✅ Audio {i} creado: {mp3_file}")

# 5. Generar PDF HTML
pdf_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{config['product_name']} Guide</title>
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 600px; margin: 40px auto; padding: 20px; }}
h1 {{ color: #667eea; }}
h2 {{ color: #764ba2; margin-top: 30px; }}
.box {{ background: #f7fafc; padding: 15px; border-radius: 8px; margin: 15px 0; }}
</style>
</head>
<body>
{config['pdf_content'].replace(chr(10), '<br>').replace('# ', '<h1>').replace('## ', '<h2>').replace('### ', '<h3>')}
</body>
</html>"""

with open('guide.html', 'w') as f:
    f.write(pdf_html)
print("📄 HTML Guía generado")

# 6. Generar Landing Page
landing_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{config['product_name']}</title>
<style>
body{{font-family:sans-serif;margin:0;line-height:1.6}}
.hero{{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:4rem 1rem;text-align:center}}
.btn{{display:inline-block;padding:1rem 2rem;background:#fbbf24;color:#1a202c;text-decoration:none;border-radius:8px;font-weight:bold;margin-top:1rem}}
.section{{max-width:700px;margin:3rem auto;padding:0 1rem}}
.card{{background:#f7fafc;padding:1.5rem;border-radius:8px;margin-bottom:1rem}}
</style>
</head>
<body>
<div class="hero">
<h1>{config['product_name']}</h1>
<p>Reset Your Digital Mind in Just 12 Minutes</p>
<a href="#buy" class="btn">Get Kit - ${config['price']}</a>
</div>
<div class="section">
<h2>What You Get</h2>
<div class="card"><h3> 3 Audio Sessions</h3><p>Morning, Work, Evening.</p></div>
<div class="card"><h3>📄 PDF Guide</h3><p>Emergency protocols.</p></div>
</div>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(landing_html)
print("🌐 Landing page generada")
