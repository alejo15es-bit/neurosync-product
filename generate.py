#!/usr/bin/env python3
import json
import os

# Crear directorio de assets
os.makedirs('assets', exist_ok=True)

# Cargar configuración
with open('config.json', 'r') as f:
    config = json.load(f)

print("✅ Configuración cargada exitosamente")
print(f"📦 Producto: {config['product_name']}")
print(f"💰 Precio: ${config['price']}")

# Generar archivos de texto para edge-tts
for i, session in enumerate(config['sessions'], 1):
    script_text = session['script'].replace('\n', ' ').replace('"', "'")
    with open(f'session{i}.txt', 'w') as f:
        f.write(script_text)
    print(f"📝 Session {i} preparado: {session['title']}")

# CORRECCIÓN: Preparar contenido PDF fuera del f-string
pdf_content_formatted = config['pdf_content'].replace('\n', '<br>')

# Crear HTML para PDF
pdf_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{config['product_name']} - Guide</title>
<style>
body {{ font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
h1 {{ color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
h2 {{ color: #764ba2; margin-top: 30px; }}
.protocol {{ background: #f7fafc; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #667eea; }}
</style>
</head>
<body>
{pdf_content_formatted}
</body>
</html>"""

with open('guide.html', 'w') as f:
    f.write(pdf_html)
print("📄 HTML para PDF generado")

# Crear landing page
landing_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{config['product_name']} - Digital Wellness</title>
  <style>
    :root{{--primary:#667eea;--secondary:#764ba2;--accent:#fbbf24}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;line-height:1.6}}
    .hero{{text-align:center;padding:4rem 2rem;background:linear-gradient(135deg,var(--primary),var(--secondary));color:#fff}}
    .hero h1{{font-size:2.5rem;margin-bottom:1rem}}
    .btn{{display:inline-block;padding:1rem 2.5rem;background:var(--accent);color:#1a202c;text-decoration:none;border-radius:10px;font-weight:700;margin:1rem}}
    .section{{padding:3rem 2rem;max-width:800px;margin:0 auto}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.5rem;margin:2rem 0}}
    .card{{padding:1.5rem;background:#f7fafc;border-radius:12px;border-left:4px solid var(--primary)}}
    .price{{text-align:center;padding:2rem;background:#f7fafc;border-radius:12px;margin:2rem 0}}
    .price-amount{{font-size:3rem;color:var(--primary);font-weight:800}}
  </style>
</head>
<body>
  <section class="hero">
    <h1>🔥 {config['product_name']}</h1>
    <p>Reset Your Digital Mind in Just 12 Minutes</p>
    <a href="#download" class="btn">Get Instant Access - ${config['price']}</a>
  </section>
  
  <section class="section">
    <h2>What You Get</h2>
    <div class="grid">
      <div class="card"><h3>🎧 3 Audio Sessions</h3><p>Morning Reset • Work Focus • Evening Detox</p></div>
      <div class="card"><h3>📄 Quick Guide PDF</h3><p>5-minute emergency protocols</p></div>
      <div class="card"><h3>♾️ Lifetime Access</h3><p>Download once, use forever</p></div>
    </div>
  </section>
  
  <section class="section price" id="download">
    <p class="price-amount">${config['price']}</p>
    <p>One payment • Forever access • 7-day guarantee</p>
  </section>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(landing_html)
print("🌐 Landing page generada")

print("\n✅ ¡Todos los archivos preparados listos!")
