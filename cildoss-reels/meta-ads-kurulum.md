# Cildoss Lenf Drenaj Fırçası + Hediye Simple SPF30: Meta Ads Kurulum Rehberi

**Teklif:** Starter Set 699 TL · Hediye Simple Protect Glow SPF30 (50 ml, sınırlı sayıda) · Ücretsiz Kargo · Kapıda Ödeme
**Kreatifler (9:16):** `cildoss-reels-A-heyecanli.mp4` · `cildoss-reels-A-samimi.mp4` · `cildoss-reels-B-samimi.mp4` · `cildoss-reels-C-heyecanli.mp4`

---

## 0. Yayına almadan önce (5 dk kontrol)

- [ ] **Pixel + Conversions API** kurulu olmalı. `Purchase` olayı sipariş onay sayfasında tetiklenmeli (kapıda ödemede ödeme kapıda alınsa bile sipariş tamamlandığında), değeri 699 ve para birimi TRY olmalı. Events Manager > Test Events'te test siparişiyle doğrulayın.
- [ ] `AddToCart` ve `InitiateCheckout` olayları da çalışmalı. Düşük bütçede erken sinyal olarak bunlara bakacağız.
- [ ] Alan adı (domain) Business Manager'da doğrulanmış olmalı.
- [ ] Açılış sayfasında da "Simple SPF30 hediye", "699 TL", "ücretsiz kargo" ve "kapıda ödeme" yazmalı. Reklamla sayfa aynı şeyi söylemezse reklam reddedilebilir ve dönüşüm düşer.
- [ ] "Sınırlı sayıda" ifadesi gerçek olmalı. Stok bitince reklam metninden kaldırın.

---

## 1. Kampanya yapısı ve bütçe

### 500 TL hakkında
Bu teklifte (699 TL, kapıda ödeme) Türkiye'de sipariş başı maliyet çoğu zaman **150–400 TL** civarında oluyor.

- **500 TL toplam** bütçeyle 1–3 sipariş gelir. Hangi videonun kazandığını satıştan anlamak için bu yeterli değil. Bu durumda kararı ön sinyallere göre verin: izlenme oranı, tıklama oranı, sepete ekleme maliyeti (bkz. Bölüm 4).
- **Önerim:** Mümkünse 500 TL'yi **günlük** bütçe olarak 5–7 gün çalıştırın. Aşağıdaki yapıyı iki senaryoya göre veriyorum.

### Kampanya ayarları
| Ayar | Seçim |
|---|---|
| Kampanya amacı | **Satışlar (Sales)** |
| Kurulum | Manuel satış kampanyası. Advantage+ Sales kampanyası değil, çünkü kreatif testinde kontrol bizde kalmalı. |
| Dönüşüm yeri | Web sitesi |
| Dönüşüm olayı | **Satın Alma (Purchase)**. Pixel'de son 7 günde neredeyse hiç satın alma yoksa ilk 3–4 gün **Ödeme Başlatma (InitiateCheckout)** ile başlayın. |
| Özel reklam kategorisi | Yok |
| A/B testi | Kapalı (bu bütçede anlamlı sonuç vermez) |
| Kampanya adı | `CLD_Lenf_SPF30Hediye_Sales_Test_2026-10` |

### Bütçe tipi: CBO mu, ABO mu?

| Senaryo | Yapı | Neden |
|---|---|---|
| **500 TL toplam** | **1 reklam seti.** Bütçe reklam seti seviyesinde (ABO), 5 günde yaklaşık 100 TL/gün. | Tek reklam setinde CBO ile ABO arasında fark yok. Bütçeyi bölmek her seti daha da az veriyle bırakır. |
| **500 TL/gün** | **ABO, 2 reklam seti:** Geniş 300 TL/gün + İlgi alanlı 200 TL/gün | ABO her kitlenin harcama almasını garanti eder. CBO bu bütçede tüm parayı ilk günlerde tek sete verebilir ve karşılaştırma yapamazsınız. Kazanan kitle belli olunca ölçeklemeyi CBO kampanyasında yapın. |

### Reklam setleri ve hedefleme

**Reklam Seti 1: GENİŞ (ana set, her iki senaryoda da açılır)**
Ad: `AS1_Genis_TR_K25-45_AdvAud`
| Ayar | Seçim |
|---|---|
| Konum | Türkiye (kargo gönderilmeyen bölge varsa onları hariç tutun) |
| Advantage+ kitle | **Açık** |
| Kitle önerisi | Kadın, 25–45 yaş. Advantage+ kitlede yaş ve cinsiyet katı sınır değil, Meta'ya öneri olarak gider. |
| Minimum yaş (katı sınır) | 18 |
| İlgi alanı | Yok. Kitleyi videolar bulacak. |
| Dil | Türkçe |
| Hariç tutma | Son 30 günde satın alanlar (Pixel'den özel kitle oluşturup ekleyin) |

**Reklam Seti 2: İLGİ ALANLI SOĞUK (sadece 500 TL/gün senaryosunda)**
Ad: `AS2_Ilgi_CiltBakimi_TR_K25-45`
| Ayar | Seçim |
|---|---|
| Konum | Türkiye |
| Advantage+ kitle | **Kapalı** (orijinal kitle seçenekleri). Yoksa ilgi alanları sadece öneri olarak kalır ve test anlamını yitirir. |
| Yaş / Cinsiyet | 25–45 / Kadın |
| İlgi alanları (hepsini tek grupta "VEYA" ile ekleyin; Ads Manager'da arayıp listede çıkanları seçin) | Cilt bakımı (Skin care) · Güzellik (Beauty) · Kozmetik · Yüz bakımı · Gua sha · Doğal kozmetik · Kore cilt bakımı (K-beauty) · Güneş kremi · Watsons · Gratis · Sephora · Rossmann |
| Advantage detaylı hedefleme | Kapalı |
| Tahmini kitle | 2–8 milyon arası idealdir |

**Yerleşimler (iki sette de aynı):**
Videolar 9:16 ve üst başlık yazısı Feed'in 4:5 kırpmasına denk geliyor. Bu yüzden testte **Manuel yerleşim** kullanın:
- Instagram: Reels, Stories, Keşfet Reels
- Facebook: Reels, Stories

Feed'i test bittikten sonra 4:5 kırpma önizlemesine bakarak ekleyin.

### Reklamlar (her reklam setinde 4 reklam)

| Reklam adı | Video | Metin seti |
|---|---|---|
| `AD_A-heyecanli_SabahSiskinligi` | cildoss-reels-A-heyecanli.mp4 | Kreatif A metinleri |
| `AD_A-samimi_SabahSiskinligi` | cildoss-reels-A-samimi.mp4 | Kreatif A metinleri |
| `AD_B-samimi_CeneHattiSirrim` | cildoss-reels-B-samimi.mp4 | Kreatif B metinleri |
| `AD_C-heyecanli_TeklifHook` | cildoss-reels-C-heyecanli.mp4 | Kreatif C metinleri |

Her reklamda:
- **Birden fazla metin seçeneği:** "Metin ekle" ile 3 ana metin, 3 başlık ve 2 açıklamayı aynı reklama girin (Meta her alanda 5'e kadar kabul eder). Meta kombinasyonları kendisi dener.
- **Kapak görseli (thumbnail):** A için başlık yazısının göründüğü ilk kare, C için gülümseyerek fırçayı gösteren kare.
- **Web sitesi URL'si:** Ürün sayfası. Sepete değil, doğrudan ürün sayfasına gitsin.
- **URL parametreleri:**
  `utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}`

**Advantage+ Creative ayarları.** Meta menü adlarını sık değiştiriyor, en yakın karşılığını seçin.

| İyileştirme | Durum | Neden |
|---|---|---|
| Metin iyileştirmeleri (girdiğiniz metin seçeneklerini değiştirerek gösterme) | ✅ Açık | Yazdığımız varyasyonları otomatik dener. |
| İlgili yorumlar / yorum gösterme | ✅ Açık | Sosyal kanıt sağlar. |
| CTA'yı iyileştirme | ✅ Açık | |
| Yapay zekâ ile yeni metin **üretme** (generate / text generation) | ❌ Kapalı | AI metni "ödem atar", "lenf temizler" gibi sağlık iddiası ekleyebilir ve ret riski doğurur. |
| Müzik ekleme | ❌ Kapalı | Seslendirmenin üstüne müzik biner. |
| Görsel rötuş / video filtreleri / 3D animasyon | ❌ Kapalı | UGC'nin doğallığını bozar, yazılar kayabilir. |
| Görsel genişletme / otomatik kırpma | ❌ Kapalı | Yazılar 9:16'ya göre yerleştirildi. |

---

## 2. Kreatife özel reklam metinleri

### Meta kişisel nitelik kuralına göre yazım kuralları
- ❌ İzleyicinin bir özelliği olduğunu ima etmeyin: "Yüzün şiş mi?", "Sen de çene hattından şikâyetçi misin?", "Gıdı sorununa son!"
- ✅ Birinci tekil şahıs, kişisel deneyim: "Sabahları yüzüm şiş görünüyordu", "Benim sabah rutinim"
- ❌ Tıbbi veya kesin sonuç iddiası: "ödemi yok eder", "lenf sistemini temizler", "yağ yakar", "%100 sonuç", "3 günde incelen yüz"
- ✅ Görünüm dili: "daha dinç görünüm", "daha belirgin görünen çene hattı"
- ❌ Gerçek olmayan aciliyet ("Son 2 saat!"). ✅ Gerçek aciliyet: "Hediye krem stoklarla sınırlı"

### CTA butonu (hepsinde aynı)
**Birincil:** `Şimdi Alışveriş Yap` (Shop Now)
**Test alternatifi:** `Sipariş Ver` (Order Now). Kapıda ödemeli e-ticarette bazen daha iyi çalışıyor. Kazanan kreatifte ikinci turda deneyin.

---

### KREATİF A: "Sabah şişkinliği" (A-heyecanlı ve A-samimi videolarında ortak)

**Ana metin 1: Kısa / Hook**
```
Sabahları aynada yüzüm hep şiş ve yorgun görünüyordu 😩 Şimdi her sabah 2 dakikalık fırça masajı yapıyorum, yüzüm çok daha dinç görünüyor ✨

🎁 Seti alana Simple SPF30 nemlendirici HEDİYE
🚚 Ücretsiz kargo · Kapıda ödeme
```

**Ana metin 2: PAS (Problem, Ajitasyon, Çözüm)**
```
Benim en büyük derdim sabahları yüzümün şiş ve yorgun görünmesiydi. Kahvaltıya kadar geçsin diye bekliyordum, fotoğraf çekilmek bile istemiyordum 🙈

Sonra Cildoss Lenf Drenaj Fırçası ile tanıştım. Her sabah sadece 2 dakika: aşağıdan yukarıya, içten dışa doğru hafif masaj. Yüzüm daha dinç, çene hattım daha belirgin görünüyor ✨

✅ 2 dakikalık kolay sabah rutini
✅ Adım adım görselli kullanım rehberi
🎁 Simple Protect Glow SPF30 nemlendirici (50 ml) HEDİYE
💰 699 TL · 🚚 Ücretsiz kargo · 💳 Kapıda ödeme

👉 Hediye krem stoklarla sınırlı, hemen sipariş ver!
```

**Ana metin 3: Teklif / Hediye**
```
🎁 SINIRLI SAYIDA: Cildoss Lenf Drenaj Fırçası alana Simple Protect Glow SPF30 Nemlendirici Yüz Kremi (50 ml) HEDİYE!

Starter Set içinde:
✔️ Cildoss Lenf Drenaj Fırçası + saklama kutusu
✔️ Adım adım kullanım rehberi
✔️ Hediye Simple SPF30 krem

💰 Sadece 699 TL
🚚 Ücretsiz kargo
💳 Kapıda nakit veya kartla ödeme

Hediye krem stoklarla sınırlı ⏳
```

**Başlıklar (en fazla 40 karakter)**
```
🎁 Simple SPF30 Krem Hediye!
```
```
699 TL · Kapıda Öde · Kargo Bedava 🚚
```
```
⏳ Hediye Krem Stoklarla Sınırlı
```

**Açıklamalar**
```
🚚 Ücretsiz kargo · Kapıda ödeme
```
```
Önce teslim al, kapıda öde 💳
```

---

### KREATİF B: "Çene hattı sırrım" (B-samimi videosu)

**Ana metin 1: Kısa / Hook**
```
Çene hattımı daha belirgin gösteren sabah rutinimi çok soruyorsunuz, işte bu 🤫 Cildoss Lenf Drenaj Fırçası ile sadece 2 dakika ✨

🎁 Şimdi yanında Simple SPF30 krem hediye
🚚 Ücretsiz kargo · Kapıda ödeme
```

**Ana metin 2: PAS (Problem, Ajitasyon, Çözüm)**
```
Eskiden sabahları yüzüm şiş göründüğü için çene hattım neredeyse kayboluyordu. Makyajla kapatmaya çalışmak da her gün ayrı bir uğraştı 😮‍💨

Rutinimi değiştiren şey çok basit oldu: Cildoss Lenf Drenaj Fırçası. Aşağıdan yukarıya, içten dışa doğru hafifçe tarıyorum, 2 dakika yetiyor. Artık yüzüm daha dinç, çene hattım daha belirgin görünüyor 💫

📖 Görselli adım adım rehber kutudan çıkıyor, nasıl yapacağını düşünmüyorsun
🎁 Simple Protect Glow SPF30 nemlendirici (50 ml) HEDİYE
💰 699 TL · 🚚 Ücretsiz kargo · 💳 Kapıda ödeme

👉 Hediye stoklarla sınırlı, sipariş ver!
```

**Ana metin 3: Teklif / Hediye**
```
Kızlar, sabah rutinime bir fırça ekledim ve şimdi yanında hediye krem de geliyor 🎁

✨ Cildoss Lenf Drenaj Fırçası Starter Set: 699 TL
🎁 Simple Protect Glow SPF30 Nemlendirici (50 ml) HEDİYE
📖 Adım adım kullanım rehberi dahil
🚚 Ücretsiz kargo
💳 Kapıda ödeme, önce teslim al sonra öde

Hediye krem sınırlı sayıda ⏳
```

**Başlıklar (en fazla 40 karakter)**
```
✨ 2 Dakikalık Sabah Rutinim
```
```
🎁 Fırçayı Al, SPF30 Krem Hediye
```
```
🚚 Kapıda Ödeme · Ücretsiz Kargo
```

**Açıklamalar**
```
Kapıda ödeme · Kargo bedava 🚚
```
```
Görselli kullanım rehberi dahil 📖
```

---

### KREATİF C: "Teklif önde" (C-heyecanlı videosu)

**Ana metin 1: Kısa / Hook**
```
Bu fırçayı alana Simple SPF30 krem BEDAVA 🎁 Ama sınırlı sayıda!

✨ Cildoss Lenf Drenaj Fırçası · 699 TL
🚚 Ücretsiz kargo · 💳 Kapıda ödeme
```

**Ana metin 2: PAS (Problem, Ajitasyon, Çözüm)**
```
Sabah uyandığımda yüzümün şiş görünmesi günümün ilk moral bozucusuydu 😩 Buzlu su, soğuk kaşık... hepsini denedim ama hiçbiri rutinime oturmadı.

Cildoss Lenf Drenaj Fırçası ile 2 dakikalık sabah masajı artık en sevdiğim rutin. Yüzüm daha dinç, çene hattım daha belirgin görünüyor ✨

Şu an kampanyada:
🎁 Simple Protect Glow SPF30 Nemlendirici (50 ml) HEDİYE
💰 699 TL
🚚 Ücretsiz kargo
💳 Kapıda ödeme

👉 Stoklar bitmeden sipariş ver!
```

**Ana metin 3: Teklif / Hediye**
```
🚨 HEDİYE KAMPANYASI 🚨

Cildoss Lenf Drenaj Fırçası Starter Set alana:
🎁 Simple Protect Glow SPF30 Nemlendirici Yüz Kremi (50 ml) HEDİYE
📖 Adım adım görselli kullanım rehberi

💰 699 TL
🚚 Ücretsiz kargo
💳 Kapıda ödeme, risk yok

⏳ Hediye kremler sınırlı sayıda, stok bitince kampanya sona erer.
```

**Başlıklar (en fazla 40 karakter)**
```
🎁 SPF30 Krem Bedava, Sınırlı Sayıda!
```
```
699 TL + Hediye Krem 🎁
```
```
⏳ Stoklar Bitmeden Sipariş Ver
```

**Açıklamalar**
```
💳 Kapıda öde · Ücretsiz kargo
```
```
Hediye krem stoklarla sınırlı ⏳
```

---

## 3. Yayın ve inceleme

1. Her şeyi taslak olarak kurun ve reklam önizlemesinde Reels ile Stories görünümünü kontrol edin. Başlık yazısı üst arayüzün, CTA alt arayüzün altında kalmamalı.
2. Yayına alınca incelemeyi bekleyin (genelde 1–24 saat).
3. Reklam reddedilirse: sağlık veya kişisel nitelik ifadesi içeren metin seçeneğini çıkarıp tekrar gönderin. Ret sebebini Account Quality sayfasında görürsünüz. Haklı olduğunuzu düşünüyorsanız "Request review" ile itiraz edin.
4. **İlk 72 saat hiçbir ayara dokunmayın.** Bütçe, kitle ya da metin değiştirmek öğrenme sürecini baştan başlatır.

---

## 4. Karar kuralları (hangi video kazanıyor?)

Bu bütçede satış sayısı az olacağı için kararı ön sinyallere göre verin. Her reklama en az **~80–100 TL harcama** yapılmadan karar vermeyin.

| Metrik | Nasıl hesaplanır | Hedef | Ne gösterir |
|---|---|---|---|
| Hook rate (3 sn izlenme oranı) | 3 sn video oynatma / Gösterim | ≥ %25–30 | Açılış cümlesi çalışıyor mu (A / B / C karşılaştırması) |
| Hold rate | ThruPlay / 3 sn oynatma | ≥ %15 | Video sonuna kadar izletiyor mu |
| Link CTR | Bağlantı tıklaması / Gösterim | ≥ %1,0 | Teklif ilgi çekiyor mu |
| CPC (link) | Harcama / Bağlantı tıklaması | ≤ 5–8 TL | |
| Sepete ekleme maliyeti | Harcama / AddToCart | ≤ 60–80 TL | Satışa en yakın ön sinyal |
| Sipariş maliyeti (CPA) | Harcama / Purchase | ≤ 250 TL (kâr marjınıza göre güncelleyin) | Nihai karar |

**Rapor sütunları:** Ads Manager > Sütunlar > Özelleştir. Şunları ekleyin: Gösterimler, 3 saniyelik video oynatmaları, ThruPlay, Bağlantı tıklamaları, CTR (bağlantı), CPC (bağlantı), Sepete ekleme, Ödeme başlatma, Satın almalar, Satın alma başına maliyet, Harcanan tutar.

**Aksiyon planı**
- Hook rate < %20 ve CTR < %0,7 olan reklamı ~100 TL harcamadan sonra **kapatın**.
- **A-heyecanlı ile A-samimi karşılaştırması** ses tonunun etkisini gösterir. Kazanan tonu gelecek kreatiflerde kullanın.
- Kazanan video ve kazanan kitle netleşince:
  1. Kazanan reklamı "Mevcut gönderiyi kullan" (Post ID) ile yeni bir **CBO** ölçekleme kampanyasına taşıyın. Beğeni ve yorumlar korunur.
  2. Bütçeyi 2–3 günde bir en fazla %20–30 artırın.
  3. Kazanan hook ile yeni varyasyonlar üretin: farklı ilk 3 saniye, farklı CTA ("Sipariş Ver").
