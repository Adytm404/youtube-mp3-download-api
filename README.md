# 🎵 YouTube Audio Downloader API

API sederhana berbasis Flask yang memungkinkan pengguna untuk mengunduh audio dari video YouTube dalam format `.mp3`. File disimpan secara lokal terlebih dahulu, lalu disajikan melalui URL custom domain.

## 🚀 Fitur

- 🔗 Input URL YouTube dan dapatkan metadata beserta link unduhan audio `.mp3`.
- 💾 File disimpan ke folder `downloads/` di server lokal.
- 🌐 Menggunakan domain khusus (`youtube-api.webkulo.com`) untuk menyajikan file unduhan.
- 🔊 Konversi otomatis ke `.mp3` menggunakan `yt-dlp` + `ffmpeg`.

---

## 🛠️ Instalasi

### 1. Clone repositori

```bash
git clone https://github.com/Adytm404/youtube-mp3-download-api
cd youtube-mp3-download-api
```

### 2. Instal dependensi Python

```bash
pip install flask yt-dlp
```

### 3. Instal `ffmpeg`

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS (Homebrew)
```bash
brew install ffmpeg
```

#### Windows
1. Download dari: https://ffmpeg.org/download.html
2. Ekstrak ke `C:\ffmpeg`
3. Tambahkan `C:\ffmpeg\bin` ke Environment Variables → `Path`

---

## 📦 Struktur Proyek

.
├── app.py            # File utama aplikasi Flask
├── downloads/        # Folder tempat menyimpan file audio
└── README.md         # Dokumentasi ini

---

## 🧪 Cara Menjalankan

```bash
python app.py
```

Akses melalui browser atau tool seperti Postman:

GET http://localhost:5000/?play=https://www.youtube.com/watch?v=dQw4w9WgXcQ

Contoh response:
{
  "title": "Rick Astley - Never Gonna Give You Up",
  "duration": "3:33",
  "file_size_bytes": 4123010,
  "download_url": "https://youtube-api.webkulo.com/download/8f3a8c12-5e4b-4a7c-9f39-0ad2b5a6f81c.mp3"
}

Untuk mengunduh file:
GET https://youtube-api.webkulo.com/download/<filename>.mp3

---

## 🌐 Deployment (Opsional)

Kamu bisa deploy API ini di server VPS dan mengarahkan domain `youtube-api.webkulo.com` ke server tersebut menggunakan Nginx sebagai reverse proxy.

Contoh konfigurasi Nginx:

server {
    listen 80;
    server_name youtube-api.webkulo.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

---

## ⚠️ Catatan

- Proyek ini hanya untuk penggunaan pribadi atau pembelajaran. Harap patuhi Terms of Service YouTube: https://www.youtube.com/t/terms
- Tidak disarankan untuk digunakan secara publik tanpa pembatasan akses, rate limiting, atau autentikasi.

---

## 📄 Lisensi

MIT License — bebas digunakan untuk proyek pribadi dan edukasi.

---

## ✨ Kontributor

- 💻 Developer: @Ogya (NyanDrive) — https://nyanhosting.id
- 📦 Teknologi: Flask, yt-dlp, ffmpeg