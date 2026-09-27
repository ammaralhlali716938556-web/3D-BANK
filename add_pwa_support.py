import json

# 1. Create manifest.json
manifest = {
    "name": "بنك الحظ 3D - مونوبولي جو",
    "short_name": "بنك الحظ",
    "description": "لعبة بنك الحظ الكلاسيكية بنكهة مونوبولي جو ثلاثية الأبعاد المطفية الفاخرة",
    "start_url": "./index.html",
    "display": "standalone",
    "background_color": "#150c08",
    "theme_color": "#b45309",
    "orientation": "portrait-primary",
    "icons": [
        {
            "src": "icon-192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "icon-512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

# 2. Create Network-First service worker that purges old caches
sw_js = """
const CACHE_NAME = 'bank-el-hazz-v5';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json'
];

self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request)
      .then((networkResponse) => {
        return networkResponse;
      })
      .catch(() => caches.match(e.request))
  );
});
"""

with open("sw.js", "w", encoding="utf-8") as f:
    f.write(sw_js)

# 3. Inject manifest link and service worker registration into index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add manifest link if not present
if '<link rel="manifest"' not in html:
    html = html.replace('<head>', '<head>\n  <link rel="manifest" href="manifest.json">\n  <meta name="apple-mobile-web-app-capable" content="yes">\n  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n  <meta name="theme-color" content="#b45309">')

# Add service worker registration script before </body>
sw_registration_code = """
  <!-- PWA Service Worker Registration with Auto-Cache Invalidation -->
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js?v=5')
          .then(reg => {
            reg.update();
            console.log('PWA ServiceWorker updated successfully!', reg.scope);
          })
          .catch(err => console.log('ServiceWorker registration failed:', err));
      });
    }
  </script>
</body>
"""

if 'serviceWorker.register' not in html:
    html = html.replace('</body>', sw_registration_code)
else:
    # Update existing SW script tag
    import re
    html = re.sub(r'<script>\s*if\s*\(\x27serviceWorker\x27 in navigator\)[\s\S]*?</script>', sw_registration_code.strip(), html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("bank_el_hazz_monopoly_go.html", "w", encoding="utf-8") as f:
    f.write(html)

print("PWA Network-First updated and old caches purged successfully!")
