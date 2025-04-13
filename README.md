# Ses Analizi WebSocket Dashboard

Bu proje, çağrı merkezi temsilcilerinin müşteri ile yaptığı görüşmeleri gerçek zamanlı olarak analiz eden bir WebSocket tabanlı dashboard içerir.

## Özellikler

- FastAPI WebSocket sunucusu
- Gerçek zamanlı veri akışı
- Temsilci bazlı:
  - Duygu analizi (pozitif / nötr / negatif)
  - Skor grafiği (Chart.js)
  - Ortalama skor tablosu
- HTML + JS tabanlı frontend (index.html)

## Kurulum

```bash
git clone https://github.com/kullaniciadi/ses-analizi-dashboard.git
cd ses-analizi-dashboard
pip install -r requirements.txt
```

## Kullanım

```bash
python ws_server.py
```

- WebSocket sunucusu `ws://localhost:8000/ws` adresinde çalışır.
- `index.html` dosyasını tarayıcıda açarak dashboard'u görüntüleyebilirsin.

## Demo

![demo](https://via.placeholder.com/800x300?text=Demo+Dashboard)

## Gereksinimler

- Python 3.8+
- Tarayıcı (Chrome, Firefox, Edge, vb.)

## Lisans

MIT