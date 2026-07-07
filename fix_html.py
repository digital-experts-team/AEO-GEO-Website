import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<nav style="position:sticky; top:0; z-index:50; display:flex; align-items:center; justify-content:space-between; padding:18px 40px; background:rgba(242,240,233,0.82); backdrop-filter:blur(12px); border-bottom:1px solid rgba(20,20,15,0.1);">', '<nav class="site-nav" style="position:sticky; top:0; z-index:50; display:flex; align-items:center; justify-content:space-between; padding:18px 40px; background:rgba(242,240,233,0.82); backdrop-filter:blur(12px); border-bottom:1px solid rgba(20,20,15,0.1);">')
content = content.replace('<div style="display:flex; align-items:center; gap:28px;">', '<div class="nav-links" style="display:flex; align-items:center; gap:28px;">', 1)
content = content.replace('<div style="display:flex; flex-wrap:wrap; gap:14px; margin-top:40px;">', '<div class="hero-actions" style="display:flex; flex-wrap:wrap; gap:14px; margin-top:40px;">')
content = content.replace('<section id="impact" style="background:#14140F; color:#F2F0E9; padding:64px 40px;">', '<section id="impact" class="impact-sec" style="background:#14140F; color:#F2F0E9; padding:64px 40px;">')
content = content.replace('<div style="max-width:1240px; margin:0 auto; display:grid; grid-template-columns:repeat(4,1fr); gap:40px;">', '<div class="impact-grid" style="max-width:1240px; margin:0 auto; display:grid; grid-template-columns:repeat(4,1fr); gap:40px;">')
content = content.replace('<section style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">', '<section class="std-sec" style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">')
content = content.replace('<section id="work" style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">', '<section id="work" class="std-sec" style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">')
content = content.replace('<section id="skills" style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">', '<section id="skills" class="std-sec" style="max-width:1240px; margin:0 auto; padding:96px 40px 40px;">')
content = content.replace('<div style="display:grid; grid-template-columns:repeat(2,1fr); gap:20px;">', '<div class="grid-2" style="display:grid; grid-template-columns:repeat(2,1fr); gap:20px;">')
content = content.replace('<div style="background:var(--accent,#16A34A); color:#fff; border-radius:22px; padding:40px; display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center;" style-hover="transform:translateY(-3px);">', '<div class="case-card" style="background:var(--accent,#16A34A); color:#fff; border-radius:22px; padding:40px; display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center;" style-hover="transform:translateY(-3px);">')
content = content.replace('<div style="background:#fff; border:1px solid rgba(20,20,15,0.1); border-radius:22px; padding:36px; display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center;" style-hover="border-color:#14140F;">', '<div class="case-card" style="background:#fff; border:1px solid rgba(20,20,15,0.1); border-radius:22px; padding:36px; display:grid; grid-template-columns:1fr auto; gap:30px; align-items:center;" style-hover="border-color:#14140F;">')
content = content.replace('<section id="contact" style="max-width:1240px; margin:60px auto 0; padding:0 40px;">', '<section id="contact" class="contact-sec" style="max-width:1240px; margin:60px auto 0; padding:0 40px;">')
content = content.replace('<div style="background:#14140F; color:#F2F0E9; border-radius:28px; padding:clamp(40px,6vw,88px); position:relative; overflow:hidden;">', '<div class="contact-box" style="background:#14140F; color:#F2F0E9; border-radius:28px; padding:clamp(40px,6vw,88px); position:relative; overflow:hidden;">')
content = content.replace('<div style="display:flex; flex-wrap:wrap; gap:14px;">', '<div class="contact-actions" style="display:flex; flex-wrap:wrap; gap:14px;">')
content = content.replace('<footer style="max-width:1240px; margin:0 auto; padding:44px 40px 60px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">', '<footer class="site-footer" style="max-width:1240px; margin:0 auto; padding:44px 40px 60px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:16px;">')

css_block = """
  /* Bulletproof Mobile Responsive */
  @media (max-width: 768px) {
    .site-nav { padding: 16px 20px !important; flex-wrap: wrap !important; gap: 12px !important; }
    .nav-links { gap: 16px !important; width: 100% !important; justify-content: flex-start !important; margin-top: 4px !important; }
    header { padding: 60px 20px 40px !important; }
    header h1 { font-size: 40px !important; line-height: 1.05 !important; }
    header p { font-size: 17px !important; margin-top: 24px !important; }
    .hero-actions { flex-direction: column !important; align-items: stretch !important; gap: 10px !important; }
    .hero-actions a { justify-content: center !important; width: 100% !important; }
    
    .impact-sec { padding: 40px 20px !important; }
    .impact-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 32px !important; }
    .impact-grid > div > div:first-child { font-size: 48px !important; }
    
    .std-sec { padding: 60px 20px 20px !important; }
    .std-sec h2 { font-size: 34px !important; margin-bottom: 32px !important; }
    .grid-2 { grid-template-columns: 1fr !important; gap: 16px !important; }
    
    .case-card { grid-template-columns: 1fr !important; padding: 28px 24px !important; gap: 20px !important; align-items: start !important; }
    .case-card > div:last-child { display: none !important; }
    .case-card h3 { font-size: 26px !important; }
    
    .contact-sec { padding: 0 20px !important; margin-top: 40px !important; }
    .contact-box { padding: 40px 24px !important; }
    .contact-box h2 { font-size: 40px !important; }
    .contact-actions { flex-direction: column !important; align-items: stretch !important; }
    .contact-actions a { justify-content: center !important; }
    
    .site-footer { padding: 32px 20px 40px !important; flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }
  }
  @media (max-width: 480px) {
    .impact-grid { grid-template-columns: 1fr !important; gap: 28px !important; }
    header h1 { font-size: 34px !important; }
    .contact-box h2 { font-size: 34px !important; }
    .case-card h3 { font-size: 24px !important; }
  }
"""

content = re.sub(r'  /\* Mobile Responsive Best Practices \*/[\s\S]*?</style>', css_block.strip() + '\n</style>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
