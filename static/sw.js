const CACHE = "pubcrawl-v2";
const ASSETS = [
  "/",
  "/api/pubcrawl",
  "/static/manifest.webmanifest",
  "/static/icon-192.png",
  "/static/icon-512.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.map(k => (k !== CACHE ? caches.delete(k) : Promise.resolve())))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);

  // Network-first for API (så den opdaterer når muligt)
  if (url.pathname === "/api/pubcrawl") {
    event.respondWith(
      fetch(event.request).then(r => {
        const copy = r.clone();
        caches.open(CACHE).then(cache => cache.put(event.request, copy));
        return r;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  // Cache-first ellers
  event.respondWith(
    caches.match(event.request).then(cached => cached || fetch(event.request))
  );
});
