# Dengar Fokus

App latihan fokus mendengar: cerita, pertanyaan, dan kartu bantu. Bisa di-install di Android (PWA) dan jalan offline.

## Isi folder
- `index.html` : aplikasinya
- `stories.json` : semua cerita, pertanyaan, dan kunci jawaban (edit di sini untuk menambah cerita)
- `generate_audio.py` : membuat suara perempuan untuk semua teks
- `manifest.webmanifest`, `sw.js`, `icon-*.png` : agar bisa di-install dan jalan offline

## 1. Buat suara (sekali, di laptop)
```
pip install edge-tts
python generate_audio.py
```
Folder `audio/` akan terisi file mp3. Tanpa folder ini, app memakai suara bawaan HP sebagai cadangan.
Setelah mengubah `stories.json`, jalankan lagi; hanya teks yang berubah yang dibuat ulang.

## 2. Coba di laptop
```
python -m http.server 8000
```
Buka http://localhost:8000

## 3. Taruh di hosting (https wajib agar bisa di-install)
Salah satu yang gratis: Cloudflare Pages, Netlify (drag and drop folder), atau GitHub Pages.
Unggah seluruh isi folder, termasuk `audio/`.

## 4. Install di Android
Buka alamat hosting di Chrome, lalu tekan tombol "📲 Pasang di HP" di menu app, atau menu Chrome (titik tiga) > "Instal aplikasi". Ikonnya muncul di layar utama dan app berjalan layar penuh.

Catatan: setelah mengganti file, naikkan nomor versi `V` di `sw.js` (misalnya `dengar-fokus-v2`) agar HP mengambil versi baru.
# dengarfokus
