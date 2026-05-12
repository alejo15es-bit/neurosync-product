#!/usr/bin/env python3
import json
import os
import subprocess
import time

# 1. Crear directorio de assets
os.makedirs('assets', exist_ok=True)

# 2. Cargar configuración
with open('config.json', 'r') as f:
    config = json.load(f)

print(f"📦 Producto: {config['product_name']}")
print(f"💰 Precio: ${config['price']}")

# 3. GUIONES COMPLETOS
scripts = [
    "Welcome to NeuroSync. Session One: Morning Mental Reset. Before your phone buzzes with emails, this is your space. Just twelve minutes. Just you. Find a comfortable position. Shoulders away from your ears. Breathe in through your nose slowly... two... three... four... Hold gently... two... three... four... five... six... seven... Release through your mouth... two... three... four... five... six... seven... eight... Notice the space that just opened. I control my attention. Not the algorithm. Not the ping. End of Session One.",

    "NeuroSync. Session Two: Work Focus Calm. You're at your desk. This is your ten-minute reset. Sit comfortably. Feet flat on floor. Breathe in... two... three... four... Hold... two... three... four... five... six... seven... Out... two... three... four... five... six... seven... eight... Visualize your attention as a spotlight. Aim it at ONE thing. Single focus. Single task. Single breath. I choose depth over speed. End of Session Two.",

    "NeuroSync. Session Three: Evening Digital Detox. The workday is done. But your mind is still scrolling. This is your disconnection ritual. Lie down comfortably. Breathe in through nose... two... three... four... Hold... two... three... four... five... six... seven... Out through mouth... two... three... four... five... six... seven... eight... Imagine unplugging from the digital world. Feel the freedom. I disconnect to reconnect. End of Session Three."
]

# 4. Generar archivos y audio
for i, script_text in enumerate(scripts, 1):
    txt_file = f'session{i}.txt'
    mp3_file = f'assets/neurosync_0{i}_session.mp3'
    
    # Escribir archivo de texto
    print(f"📝 Creando {txt_file}...")
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(script_text)
    
    # Verificar que se escribió
    if os.path.getsize(txt_file) == 0:
        print(f"❌ ERROR: {txt_file} está vacío")
        exit(1)
    
    print(f"🎙️ Generando audio {i} con edge-tts...")
    
    # Ejecutar edge-tts y esperar a que termine
    result = subprocess.run([
        'edge-tts',
        '--voice', 'en-US-AriaNeural',
        '--text-file', txt_file,
        '--write-media', mp3_file
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Error en edge-tts: {result.stderr}")
        exit(1)
    
    # Verificar que se creó el MP3
    if os.path.exists(mp3_file):
        file_size = os.path.getsize(mp3_file)
        print(f"✅ Audio {i} creado: {mp3_file} ({file_size} bytes)")
    else:
        print(f"❌ ERROR: No se creó {mp3_file}")
        exit(1)

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
<h1>5-Minute Digital Anxiety Reset</h1>
<h2>WHEN TO USE THIS</h2>
<ul>
<li>After notification overload</li>
<li>Before important calls</li>
<li>When chest feels tight from screens</li>
</ul>
<h2>PROTOCOL 1: The 4-7-8 Breath</h2>
<ol>
<li>Sit tall, shoulders down</li>
<li>Inhale through nose for 4 counts</li>
<li>Hold breath for 7 counts</li>
<li>Exhale slowly for 8 counts</li>
</ol>
<h2>PROTOCOL 2: Anchor Phrase</h2>
<p>Choose one phrase: "I control my attention." Repeat 10x.</p>
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
<div class="card"><h3>🎧 3 Audio Sessions</h3><p>Morning, Work, Evening.</p></div>
<div class="card"><h3>📄 PDF Guide</h3><p>Emergency protocols.</p></div>
</div>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(landing_html)
print("🌐 Landing page generada")

print("\n✅ ¡TODO GENERADO EXITOSAMENTE!")
