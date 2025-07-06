# 🧠 Welcome to Reality – AI Destekli Kariyer Yönlendirme Platformu

## 🎯 Proje Amacı

Üniversite öğrencilerini gerçek iş ilanlarına göre yönlendiren, sektörel verilerle desteklenmiş, AI tabanlı proje fikirleri ve README çıktıları sunan kişiselleştirilmiş bir kariyer destek platformu geliştirmek.

## 🌍 Hedef Kitle

- Yazılım veya veri alanında kariyer hedefleyen öğrenciler
- Yeni mezunlar
- Alan değiştirmek isteyen bireyler

## 🛠️ Kullanılan Teknolojiler

- Python 3.10+
- FastAPI (Backend)
- PostgreSQL (Veri tabanı)
- Gemini Pro API (LLM entegrasyonu)
- Web Scraping (requests, BeautifulSoup)
- HTML/CSS veya Streamlit (Frontend)
- Render.com (Deployment)

## 📁 Dizin Yapısı

```
/app
  ├── main.py
  ├── routers/
  ├── models/
  ├── schemas/
  ├── database/
data/
  └── sample_jobs.json
images/
  └── sprint1_board.png
```

## 🔧 Kurulum

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

---

# 👥 Takım Üyeleri

| İsim             | Rolü                     | Sorumluluklar |
|------------------|--------------------------|----------------|
| Murat Ertuğrul   | Scrum Master             | Süreç yönetimi, günlük takibin yapılması, engel çözümü |
| Çağan Demir      | Product Owner / LLM      | Ürün vizyonu, prompt tasarımı, proje çıktıları |
| Damla Söylemez   | Veri ve LLM              | Veri temizliği, model çıktısı hazırlığı |
| Sevilay Mete     | Veritabanı & Backend     | PostgreSQL kurulumu, veri şeması |
| Dilara Yavuz     | Frontend                 | Arayüz tasarımı, çıktı sunumu |

---

# 🟩 Sprint 1 Raporu

## 🔎 Sprint Hedefleri

- Veri toplama ve anonimleştirme
- PostgreSQL kurulumu ve şema yapısı
- FastAPI temel uçlarının oluşturulması
- Swagger üzerinden test

## ✅ Gerçekleştirilen Görevler

- [x] Kaggle verisi incelendi ve örnek JSON dosyası hazırlandı
- [x] PostgreSQL veritabanı kuruldu
- [x] FastAPI iskeleti oluşturuldu
- [x] `/register`, `/login`, `/get_jobs` uçları hazırlandı
- [x] Swagger UI ile test edildi

## 🔢 Story Point Tahminleri

| Görev                          | SP  | Durum     |
|--------------------------------|-----|-----------|
| PostgreSQL kurulumu            | 3   | ✅ Tamamlandı |
| Web scraping (örnek JSON)      | 4   | ✅ Tamamlandı |
| FastAPI kullanıcı uçları       | 4   | ✅ Tamamlandı |
| LLM prompt taslağı             | 6   | ⏳ Devam ediyor |
| Kullanıcı senaryosu            | 4   | ✅ Tamamlandı |
| Swagger testleri               | 3   | ✅ Tamamlandı |

Toplam SP hedefi: **24**  
Tamamlanan: **21 SP** → Başarı oranı: **%87**

## 🧠 Tahmin Mantığı

Story point'ler; teknik karmaşıklık, zaman tahmini ve daha önceki tecrübelere göre belirlendi. 
1 SP ≈ 0.5 günlük iş gücü olarak hesaplandı.

## 🕓 Daily Scrum Özetleri

- **Gün 1:** Veriler hazırlandı, veri tabanı yapısı planlandı
- **Gün 2:** FastAPI uçları için temel kod yapısı yazıldı
- **Gün 3:** JSON veriler işlendi, anonimleştirme tamamlandı
- **Gün 4:** Swagger testleri yapıldı
- **Gün 5:** Geriye kalan görevler gözden geçirildi, board güncellendi

## 📋 Sprint Board

![Sprint Board](images/sprint1_board.png)

## 🔄 Retrospective

### ✅ Neler iyi gitti?
- İletişim güçlüydü, görev paylaşımı netti
- API uçları zamanında yetişti

### ⚠️ Zorluklar:
- LLM prompt çıktıları beklenenden daha karmaşık geldi
- Kod entegrasyonları bazı dosyalarda zaman aldı

### 💡 Geliştirmeler:
- LLM prompt kısmı için küçük testler daha erken yapılmalıydı
- Daily Scrum sonrası kısa teknik mini toplantılar yararlı oldu

---

📝 Sprint 2’de LLM entegrasyonu ve proje çıktılarının kişiselleştirilmiş olarak sunulması hedeflenmektedir.