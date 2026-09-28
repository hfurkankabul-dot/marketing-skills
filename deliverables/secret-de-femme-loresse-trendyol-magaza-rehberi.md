# Secret de Femme × Loresse — Trendyol Mağaza Tasarım Rehberi

> Kapsam: Secret de Femme çatı markası altında Loresse serisi. Vitrinin odağı fırça ve sünger setleri (LRS-016 – LRS-045); dudak ürünleri (LRS-001 – LRS-015: Lip Gloss, Dudak Yağı) çapraz satış için ayrı bir alanda yer alır.
> Hedef: Mağaza sayfası dönüşüm oranı (CVR) ve sepet ortalaması (AOV).
> Kampanya yaklaşımı: **Yeni kupon tanımlanmaz.** Mağazada zaten aktif olan Trendyol kampanyaları (Sepette Ekstra İndirim, Çok Al Az Öde, İkinci Ürüne Özel Fırsat) öne çıkarılır.
> Kullanım: Her `text` bloğu doğrudan Canva metin kutusuna veya Trendyol paneline kopyalanabilir.

---

## 0. Başlamadan Önce — 3 Kritik Not

1. **Ürün isimleri:** LRS-016 – LRS-045 arasındaki her kodun tam ürün adı bu rehberde bulunmuyor. Görsel kompozisyonlardaki `[LRS-0XX – Kabuki Fırça]` gibi yer tutucuları ve Bölüm 5'teki "Ürün Adı" sütununu kendi ürün listenizle doldurun. Kod aralıkları ve ürün grupları (dudak ürünleri / fırça ve sünger setleri) tabloya işlendi.
2. **Onaylı iddia dili:** "Anti-bakteriyel" gibi belge gerektiren sağlık iddiaları kullanılmaz. Tüm metinlerde yalnızca şu iki ifade kullanılır:
   - **Hijyenik & Kolay Temizlenir Sentetik Kıl**
   - **Cilde Dost Yumuşak Dokunuş**
3. **Kampanya metinleri canlı kampanyaya bağlıdır:** Banner ve rozetlerde yalnızca panelde o an **aktif** olan kampanyayı yazın. Kampanya bittiğinde banner'ı aynı gün değiştirin; mağazada geçerli olmayan bir fırsatı göstermek hem müşteri şikâyeti hem de içerik denetimi riski taşır. Oran/tutar alanlarını (`%[X]`, `[X] TL`) paneldeki kampanya koşullarıyla birebir doldurun.

Ek not — **Banner ölçüleri:** Aşağıdaki ölçüler sizin belirlediğiniz ölçülerdir. Trendyol mağaza editöründe widget ölçüleri zaman zaman güncellenir; tasarıma başlamadan önce panelde ilgili widget'ın "önerilen görsel boyutu" bilgisini kontrol edin. Oran aynı kalırsa Canva'da **Yeniden Boyutlandır** ile saniyeler içinde uyarlarsınız.

---

## 1. Trendyol Mağaza Dizilimi & Modül Sıralaması

Mantık: **Dikkat → Fırsat → Keşif → Kanıt → Arzu → Güven → Satın alma.** Mobilde ilk ekran (ilk ~700 px) hero + aktif fırsatlar ile bitmeli; kullanıcı kaydırmadan "neden şimdi almalıyım" sorusunun cevabını görmeli.

```text
SIRA | MODÜL                                    | ÖLÇÜ          | AMACI
-----|------------------------------------------|---------------|--------------------------------------------
01   | Hero Banner                              | 1200 x 400    | Marka + öne çıkan aktif kampanya (ilk izlenim)
02   | Aktif Fırsatlar / Mağaza Kampanyaları    | 1200 x 200    | Aktif Trendyol kampanyalarını tek bantta göstermek
     |   + Kampanyalı Ürünler karuseli          | Ürün karuseli | Kampanyaya dahil ürünlere tek dokunuşla ulaşım
03   | Üçlü Kategori Grid                       | 3 x 400 x 400 | Hızlı yönlendirme (Fırça / Sünger / Set)
04   | Öne Çıkan Ürünler – "Çok Satanlar"       | Ürün karuseli | Sosyal kanıt, en yüksek CVR'li 8–12 ürün
05   | İkili Promo Banner                       | 2 x 600 x 600 | Fırçalar vs. Süngerler/Ponponlar hikâyesi
06   | Ürün Listesi – "Setlerde Avantaj"        | Ürün karuseli | Sepet ortalaması (AOV) — set/paket ürünler
07   | Güven Bandı                              | 1200 x 200    | Tereddüt kırma (kalite, orijinallik, kargo)
08   | Ürün Listesi – "Makyajını Dudakla Tamamla"| Ürün karuseli | Çapraz satış: Lip Gloss & Dudak Yağı (LRS-001 – 015)
09   | Ürün Listesi – "Yeni Gelenler"           | Ürün karuseli | Tekrar ziyaret eden kullanıcıya tazelik
10   | Tüm Ürünler                              | Ürün grid     | Kapanış; kaydıran kullanıcıya tam katalog
```

**Neden bu sıra?**
- Aktif Fırsatlar bandı hero'nun hemen altında: kampanya görünmezse kampanyanın satışa etkisi olmaz. Bant, kampanyalı ürünler karuseline bağlanır.
- Çok Satanlar, İkili Banner'dan önce: satın almaya hazır kullanıcı hikâyeyi beklemeden ürüne ulaşır.
- Güven Bandı set karuselinin hemen altında: yüksek tutarlı sepette tereddüt en yüksek noktadadır.
- Dudak ürünleri karuseli, "İkinci Ürüne Özel Fırsat" ve "Çok Al Az Öde" kampanyalarıyla sepete ikinci ürün ekletmek için güven bandından sonra gelir.

**Kampanya dönemleri (Efsane Kasım, Sevgililer Günü, Anneler Günü):** Yalnızca 01 (Hero), 02 (Aktif Fırsatlar bandı) ve 06'nın başlığını değiştirin; iskelet sabit kalsın.

---

## 2. Piksel Bazlı Canva Banner Metinleri & Görsel Kompozisyonu

### 2.1 Hero Banner — 1200 x 400 px

**Yerleşim ızgarası (soldan sağa):**

```text
[0–60 px]     Güvenli boşluk (metin/ürün girmez)
[60–640 px]   METİN BÖLGESİ (sol) — logo, başlık, alt başlık, CTA
[640–1140 px] ÜRÜN BÖLGESİ (sağ) — arka planı kaldırılmış LRS ürünleri
[1140–1200]   Güvenli boşluk
Rozet         Sağ üst köşe, x: 980–1120 / y: 30–170 (140 x 140 daire)
Dikey         Üst ve alt 40 px güvenli boşluk
```

**Rozet metinleri — yalnızca o an aktif olan kampanyayı seçin:**

```text
SEPETTE EKSTRA İNDİRİM aktifse:   SEPETTE / EKSTRA %[X]
ÇOK AL AZ ÖDE aktifse:            ÇOK AL / AZ ÖDE
                                  (koşulu netse: 3 AL / 2 ÖDE)
İKİNCİ ÜRÜNE FIRSAT aktifse:      2. ÜRÜNE / %[X] İNDİRİM
Birden fazla kampanya aktifse:    AKTİF / FIRSATLAR
Hiçbir kampanya aktif değilse:    Rozeti kaldırın (boş rozet koymayın)
```

**Metinler — Seçenek A (Önerilen, marka odaklı):**

```text
ÜST ETİKET (küçük, harf aralıklı):   SECRET DE FEMME × LORESSE
ANA BAŞLIK:                           Kusursuz Ten, Tek Dokunuşta
ALT BAŞLIK:                           Hijyenik & kolay temizlenir sentetik kıllı fırçalar ve cilde dost yumuşak dokunuşlu süngerlerle profesyonel makyaj artık evinde.
ROZET:                                (yukarıdaki listeden aktif kampanya)
CTA BUTON:                            Koleksiyonu Keşfet
```

**Seçenek B (kampanya odaklı — Sepette Ekstra İndirim aktifken):**

```text
ÜST ETİKET:   LORESSE FIRÇA & SÜNGER SETLERİ
ANA BAŞLIK:   Makyajın Sırrı Fırçasında
ALT BAŞLIK:   Seçili setlerde sepette ekstra %[X] indirim seni bekliyor. Stoklar sınırlı!
ROZET:        SEPETTE / EKSTRA %[X]
CTA BUTON:    Fırsatları Gör
```

**Seçenek C (kampanya odaklı — Çok Al Az Öde / İkinci Ürün aktifken):**

```text
ANA BAŞLIK:   Setini Tamamla, Daha Az Öde
ALT BAŞLIK:   Fırçanın yanına süngerini ekle; çok al az öde fırsatını kaçırma.
              (İkinci ürün kampanyası için: İkinci ürününde %[X] indirim — fırçana süngerini ekle.)
ROZET:        ÇOK AL / AZ ÖDE   veya   2. ÜRÜNE / %[X] İNDİRİM
CTA BUTON:    Kombinini Oluştur
```

**Tipografi & ölçüler:**

```text
Üst etiket    Montserrat Medium, 14 px, harf aralığı 300, renk #B76E79
Ana başlık    Playfair Display Bold, 46–52 px, satır aralığı 1.1, renk #1C1C1C
Alt başlık    Montserrat Regular, 18 px, maks. 2 satır, renk #5E5250
CTA buton     260 x 52 px, köşe yarıçapı 26, dolgu #1C1C1C, yazı #FFFFFF Montserrat SemiBold 16 px
Rozet         140 px daire, dolgu #B76E79, yazı #FFFFFF Montserrat Bold 15 px, 2 satır, -8° döndürülmüş
Arka plan     #F7EDE8 → #E8CFC1 soldan sağa degrade + sağ bölgede 420 px yumuşak beyaz ışık halkası (%40 opaklık)
```

**Ürün kompozisyonu (sağ bölge) — arka planı kaldırılmış PNG'ler:**

```text
KOMPOZİSYON 1 – "Fan Açılımı" (önerilen)
  • 5 fırça yelpaze şeklinde, sapları aşağıda birleşen, tepeleri 15°'lik aralıklarla açılan
    [LRS-0XX – Kabuki] ortada ve en önde, [LRS-0XX – Pudra], [LRS-0XX – Allık],
    [LRS-0XX – Far], [LRS-0XX – Kontür] iki yana
  • Önde, fırça saplarının dibinde 2 sünger: [LRS-0XX – Damla Sünger] + [LRS-0XX – Ponpon]
  • Zemin gölgesi: Canva "Gölgeler > Kaldırma (Lift)" veya 20 px bulanık, %25 siyah elips

KOMPOZİSYON 2 – "Hero Ürün + Destek"
  • Tek büyük fırça 30° eğik, çerçevenin %70'i yüksekliğinde: [LRS-0XX – En çok satan fırça]
  • Arkasında hafif bulanık (%30) 3 fırça seti silüeti
  • Sağ altta 2 sünger üst üste: [LRS-0XX] + [LRS-0XX]

KOMPOZİSYON 3 – "Set Vitrini" (Seçenek C / kombin kampanyaları için ideal)
  • Açık fırça çantası/kutusu ortada, içinden fırçalar dışarı taşıyor: [LRS-0XX – Fırça Seti]
  • Yanında sünger seti: [LRS-0XX – Sünger Seti]
  • Önde pudra dokusu (serpilmiş pudra fotoğrafı, %60 opaklık)
```

---

### 2.2 Aktif Fırsatlar / Mağaza Kampanyaları Bandı — 1200 x 200 px

Kupon alanı modülünün yerine gelir. Hero'nun hemen altında yer alır ve kampanyalı ürünler karuseline bağlanır.

**Yerleşim:** 3 eşit kutucuk (her biri ~370 x 150 px, aralarında 20 px boşluk, kenarlarda 15 px). Her kutucukta solda büyük rakam/ikon, sağda 2 satır metin. Zemin #1C1C1C, kutucuklar #2A2424, vurgu #D4A5A5. Aktif olmayan kampanyanın kutucuğunu **kaldırın**; 2 kampanya aktifse 2 kutucuk (her biri ~570 px) kullanın.

```text
BANT BAŞLIĞI (bandın üstünde, ayrı metin veya widget başlığı):
  Aktif Fırsatlar
  (alternatif: Mağaza Kampanyaları / Şu An Mağazada)

KUTUCUK 1 — SEPETTE EKSTRA İNDİRİM
  Büyük:   %[X]
  Başlık:  Sepette Ekstra İndirim
  Alt:     Seçili Loresse setlerinde, indirim sepette otomatik

KUTUCUK 2 — ÇOK AL AZ ÖDE
  Büyük:   [3 AL 2 ÖDE]   (koşul farklıysa panel koşulunu yazın)
  Başlık:  Çok Al Az Öde
  Alt:     Fırça & sünger setlerini karıştır, daha az öde

KUTUCUK 3 — İKİNCİ ÜRÜNE ÖZEL FIRSAT
  Büyük:   2.
  Başlık:  İkinci Ürüne %[X] İndirim
  Alt:     Setinin yanına Lip Gloss veya Dudak Yağı ekle
```

**Kısa versiyon (mobilde tek satır, alternatif):**

```text
Sepette Ekstra %[X]  •  Çok Al Az Öde  •  2. Ürüne %[X]
```

**Tipografi:**

```text
Bant başlığı   Playfair Display Bold 28 px, #1C1C1C (bandın üstünde, açık zeminde)
Büyük rakam    Playfair Display Bold 48 px, #D4A5A5
Başlık         Montserrat SemiBold 18 px, #FFFFFF
Alt satır      Montserrat Regular 14 px, #E8CFC1
```

**Panel notu:** Bandın hemen altına "Kampanyalı Ürünler" başlıklı bir ürün karuseli ekleyin ve yalnızca aktif kampanyaya dahil ürünleri seçin. Banner görsel olduğu için tıklanabilir bir ürün listesine bağlanmazsa kullanıcı fırsatı bulamaz.

---

### 2.3 İkili Promo Banner — 2 x 600 x 600 px

**Ortak yerleşim:** Üst %45 metin, alt %55 ürün. Kenarlarda 40 px güvenli boşluk. İki banner yan yana aynı hizada görünmeli; başlık satırlarının y-koordinatı eşit olmalı (y: 70). Sağ üst köşede opsiyonel küçük kampanya etiketi (120 x 36 px hap, #B76E79 dolgu): yalnızca ilgili ürün grubunda aktif kampanya varsa.

#### Banner 1 — FIRÇALAR

```text
ÜST ETİKET:     LORESSE FIRÇA SETLERİ
BAŞLIK:         Kadife Dokunuş, Kusursuz Dağılım
ALT METİN:      Sentetik kıl teknolojisi ürünü emmez, eşit dağıtır.
ÖZELLİK 1:      ✓ Sentetik Kıl Teknolojisi
ÖZELLİK 2:      ✓ Hijyenik & Kolay Temizlenir Sentetik Kıl
ÖZELLİK 3:      ✓ Cilde Dost Yumuşak Dokunuş
KAMPANYA ETİKETİ (opsiyonel):  SEPETTE EKSTRA %[X]
CTA:            Fırçaları Keşfet →
```

Alternatif sloganlar:

```text
• Her Fırça Darbesinde Profesyonel Sonuç
• Yumuşak Kıl, Keskin Çizgi
• Fondötenden Fara, Tek Set
```

Görsel: 3–4 fırça dikey ve hafif çapraz dizilim, zemin #1C1C1C (mat siyah) — fırçaların rose gold/nude tonları bu zeminde öne çıkar. Metinler #FFFFFF, özellik tikleri #D4A5A5.

#### Banner 2 — SÜNGERLER & PONPONLAR

```text
ÜST ETİKET:     LORESSE SÜNGER & PONPON SETLERİ
BAŞLIK:         Pürüzsüz Ten, Doğal Bitiş
ALT METİN:      Nemlendiğinde büyüyen yumuşak dokusuyla iz bırakmadan kapatır.
ÖZELLİK 1:      ✓ Pürüzsüz Ten Etkisi
ÖZELLİK 2:      ✓ Cilde Dost Yumuşak Dokunuş
ÖZELLİK 3:      ✓ Islak & Kuru Kullanım
KAMPANYA ETİKETİ (opsiyonel):  ÇOK AL AZ ÖDE
CTA:            Süngerleri Keşfet →
```

Alternatif sloganlar:

```text
• Fondötenin En İyi Arkadaşı
• Tap Tap, Kusursuz!
• İz Bırakmayan Bitiş, Yumuşacık Doku
```

Görsel: 1 damla sünger önde (büyük), arkasında 2 sünger + 1 ponpon; zemin #F7EDE8 (açık nude). Metinler #1C1C1C, başlık vurgusu #B76E79. Opsiyonel: süngerin yanında küçük su damlası grafiği (Canva: "water droplet 3d").

**Tipografi (her iki banner):**

```text
Üst etiket   Montserrat Medium 13 px, harf aralığı 250
Başlık       Playfair Display Bold 40 px, maks. 2 satır
Alt metin    Montserrat Regular 17 px, maks. 2 satır
Özellikler   Montserrat Medium 16 px, satır aralığı 1.6
CTA          Montserrat SemiBold 16 px, altı çizili veya 200 x 46 px hap buton
```

---

### 2.4 Üçlü Kategori Grid — 3 x 400 x 400 px

Kural: Görsel üzerinde **en fazla 2 satır**, en az 36 px başlık. Mobilde bu kareler ~115 px'e küçülür; uzun metin okunmaz.

```text
KART 1 — FIRÇALAR
  Başlık:      FIRÇALAR
  Alt satır:   Yüz & Göz Setleri
  Görsel:      2–3 fırça çapraz, nude zemin (#E8CFC1)

KART 2 — SÜNGER & PONPON
  Başlık:      SÜNGERLER
  Alt satır:   & Ponponlar
  Görsel:      Damla sünger + ponpon, açık pembe zemin (#F3DCDC)

KART 3 — SETLER
  Başlık:      SETLER
  Alt satır:   Avantajlı Paketler
  Görsel:      Fırça seti/çantası, şampanya zemin (#F7E7CE)
```

Alternatif 3. kart (dudak ürünlerini de vitrine taşımak isterseniz):

```text
KART 3 — DUDAK
  Başlık:      DUDAK
  Alt satır:   Lip Gloss & Dudak Yağı
  Görsel:      Lip gloss + dudak yağı şişeleri, şampanya zemin (#F7E7CE)
```

Yerleşim: Başlık alt kenardan 60 px yukarıda, ortalı; başlığın altında 60 x 2 px #B76E79 çizgi. Metin Montserrat Bold 36 px, harf aralığı 150, #1C1C1C. Ürün görseli karenin üst %65'inde.

---

### 2.5 Güven Bandı — 1200 x 200 px

Yerleşim: 3 eşit sütun (400 px), her sütunda solda 56 px ikon + sağda 2 satır metin. Sütunlar arasında 1 px #D9C3B8 dikey ayırıcı (y: 50–150). Zemin #FAF6F2 veya #1C1C1C (koyu versiyon).

**Seçenek A (önerilen):**

```text
SÜTUN 1  İkon: yaprak/kalkan
  Başlık:  Hijyenik & Kolay Temizlenir Sentetik Kıl
  Alt:     Cilde dost yumuşak dokunuş

SÜTUN 2  İkon: kutu/mühür
  Başlık:  %100 Orijinal Ambalaj
  Alt:     Secret de Femme güvencesiyle

SÜTUN 3  İkon: kargo kamyonu
  Başlık:  Hızlı Kargo
  Alt:     Aynı gün / 24 saatte kargoda*
```

`*` Kargoya veriliş sürenizi paneldeki "Kargoya Teslim Süresi" ile birebir eşleştirin. Söz veremediğiniz süreyi yazmayın; alternatif: **"Özenle Paketlenir, Hızla Yola Çıkar"**.

**Seçenek B (kısa, mobil dostu):**

```text
✓ Hijyenik Sentetik Kıl   ✓ Orijinal Ambalaj   ✓ Hızlı Kargo
```

Tipografi: Başlık Montserrat SemiBold 18 px #1C1C1C, alt satır Montserrat Regular 14 px #7A6A66. İkonlar tek renk #B76E79, çizgi (outline) stili.

---

## 3. Canva Stil & Renk Rehberi

### 3.1 Renk Paleti

```text
ROL                 İSİM              HEX       KULLANIM
------------------  ----------------  --------  ------------------------------------------
Ana vurgu           Rose Gold         #B76E79   Rozet, ince çizgiler, ikonlar, başlık vurgusu
Ana vurgu (açık)    Dusty Rose        #D4A5A5   Tikler, kampanya rakamları (koyu zeminde)
Nötr zemin 1        Nude              #E8CFC1   Kategori kartları, hero degrade sonu
Nötr zemin 2        Blush Nude        #F7EDE8   Hero degrade başı, açık bannerlar
Nötr zemin 3        Ivory             #FAF6F2   Güven bandı, geniş boşluklar
Lüks aksan          Şampanya          #F7E7CE   Set/premium ürün kartları
Metin & kontrast    Mat Siyah         #1C1C1C   Başlıklar, CTA buton dolgusu, koyu bantlar
İkincil metin       Kakao Gri         #5E5250   Alt başlıklar, açıklamalar
Üçüncül metin       Taupe             #7A6A66   Güven bandı alt satırları
Ayırıcı             Kum               #D9C3B8   İnce çizgiler, kart kenarlıkları
```

**Okunabilirlik kuralları:**
- Beyaz metni #B76E79 üzerinde yalnızca **24 px ve üzeri kalın** metinde kullanın (rozet gibi). Küçük metinde kontrast yetersiz kalır.
- Uzun metin her zaman #1C1C1C veya #5E5250 ile açık zemin üzerinde.
- CTA butonu her yerde **aynı**: #1C1C1C dolgu + #FFFFFF yazı. Tutarlılık tıklama alışkanlığı yaratır.
- Oran: %60 nötr zemin, %30 mat siyah/metin, %10 rose gold vurgu.

### 3.2 Yazı Tipleri (Canva'da mevcut)

```text
Başlık (serif, lüks):     Playfair Display  (alternatif: Cormorant Garamond Bold)
Gövde/CTA (sans, modern): Montserrat        (alternatif: Poppins)
Rozet/etiket:             Montserrat Bold, BÜYÜK HARF, geniş harf aralığı
```

### 3.3 Canva'da Aratılacak Anahtar Kelimeler

```text
ŞABLON ARAMALARI
  beauty banner minimal
  cosmetics web banner nude
  makeup brush banner
  luxury beauty sale banner
  skincare hero banner
  rose gold beauty promo
  beauty trust badges banner
  offer strip banner dark (Aktif Fırsatlar bandı için)

ELEMENT / GÖRSEL ARAMALARI
  rose gold line frame
  gold foil circle badge
  sale tag pill minimal
  soft shadow podium
  beige arch shape
  powder splash
  makeup powder texture
  silk fabric background nude
  water droplet 3d
  minimal line icon shipping / leaf / box (outline)

FOTOĞRAF ARAMALARI (arka plan)
  nude aesthetic background
  beige marble texture
  soft pink gradient
  vanity table flatlay
```

### 3.4 Canva İş Akışı

```text
1. Marka Kiti → Renkler: yukarıdaki 10 HEX kodunu ekle; Yazı Tipleri: Başlık=Playfair Display, Alt başlık=Montserrat SemiBold, Gövde=Montserrat Regular.
2. Ürün fotoğraflarını yükle → Düzenle → Arka Plan Kaldırıcı → PNG olarak Klasör: "LRS Kesilmiş".
3. Önce Hero'yu tasarla; diğer bannerları "Kopyasını oluştur + Yeniden boyutlandır" ile türet (renk/tipografi tutarlılığı).
4. Kampanya rozetleri ve Aktif Fırsatlar kutucuklarını ayrı sayfalarda tut (her kampanya için bir varyant); kampanya değişince yalnızca ilgili sayfayı dışa aktar.
5. Dışa aktarım: JPG, kalite %85–90 (Trendyol yükleme sınırını aşmamak için). Metin ağırlıklı bantlar için PNG.
6. Dosya adı: sdf-loresse-hero-1200x400-sepette-ekstra-v1.jpg (kampanya adını dosya adına yaz; hangi görselin hangi kampanyaya ait olduğu karışmaz).
```

---

## 4. Trendyol Kategori Ağacı & Kampanya Kurgusu

### 4.1 Önemli Ayrım

- **Trendyol ürün kategorisi** (ör. Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası) Trendyol'un sabit ağacıdır; ürünü doğru yaprak kategoriye atamak arama görünürlüğünün temelidir.
- **Mağaza içi kategori / koleksiyon** ise mağaza sayfanızda sizin açtığınız ürün listeleridir. Aşağıdaki ağaç bu mağaza içi yapı içindir.

**Trendyol ürün kategorisi eşleştirmesi (ürün yüklerken):**

```text
Fırçalar             → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası
Fırça setleri        → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası Seti
Sünger / Ponpon      → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Süngeri / Pudra Ponponu
Lip Gloss            → Kozmetik > Makyaj > Dudak Makyajı > Dudak Parlatıcısı
Dudak Yağı (Lip Oil) → Kozmetik > Makyaj > Dudak Makyajı (veya Cilt Bakım > Dudak Bakımı)
```

(Panelde yaprak kategori adları farklı görünebilir; ürün yüklerken en spesifik eşleşmeyi seçin.)

### 4.2 Mağaza İçi Kategori Ağacı (SEO uyumlu adlar)

İsimlendirme kuralı: **Arama yapılan kelime + fayda/tip.** "Koleksiyon 1" gibi soyut isimler yerine kullanıcının aradığı kelimeyi kullanın.

```text
1. Makyaj Fırçaları (LRS-016 – LRS-045 içindeki fırça ürünleri)
   1.1 Fondöten Fırçası
   1.2 Pudra & Kabuki Fırçası
   1.3 Allık & Kontür Fırçası
   1.4 Far & Göz Makyaj Fırçası
   1.5 Kaş & Eyeliner Fırçası
   1.6 Makyaj Fırçası Setleri

2. Makyaj Süngerleri & Ponponlar (LRS-016 – LRS-045 içindeki sünger ürünleri)
   2.1 Damla Makyaj Süngeri
   2.2 Kapatıcı & Detay Süngeri
   2.3 Pudra Ponponu
   2.4 Sünger Setleri

3. Dudak Ürünleri (LRS-001 – LRS-015)
   3.1 Lip Gloss
   3.2 Dudak Yağı (Lip Oil)

4. Avantajlı Setler & Hediyelik
   4.1 Fırça + Sünger Kombin Setleri
   4.2 Hediyelik Makyaj Setleri

5. Aktif Fırsatlar (kampanyalı ürünler; kampanya değiştikçe güncellenir)
6. Çok Satanlar
7. Yeni Gelenler
```

**Ürün başlığı formülü (arama + CVR için):**

```text
Secret de Femme Loresse [Ürün Tipi] [Ana Fayda] [Özellik] – [Adet/Renk]

Örnekler:
Secret de Femme Loresse Kabuki Pudra Fırçası Hijyenik Kolay Temizlenir Sentetik Kıl – Rose Gold
Secret de Femme Loresse Damla Makyaj Süngeri Cilde Dost Yumuşak Dokunuş Pürüzsüz Bitiş – 2'li Set
```

(Ürün kodunu başlıkta değil, "Model Kodu / Stok Kodu" alanında tutmak daha temiz görünür; başlık karakter limitine dikkat.)

### 4.3 Aktif Kampanya Kurgusu (Kupon Yok)

Yeni kupon tanımlanmaz. Mağazada halihazırda aktif olan Trendyol kampanyaları vitrinde üç noktada görünür: **Hero rozeti**, **Aktif Fırsatlar bandı** ve **ilgili ürün karuselleri.** Aşağıdaki tablo her kampanyanın hangi ürün grubuyla ve hangi mesajla eşleşeceğini gösterir.

```text
KAMPANYA                  | EN UYGUN ÜRÜN GRUBU                      | VİTRİN BAŞLIĞI                        | ROZET / ETİKET
--------------------------|------------------------------------------|---------------------------------------|----------------------
Sepette Ekstra İndirim    | Fırça setleri, yüksek fiyatlı setler     | Sepette Ekstra %[X] İndirim           | SEPETTE EKSTRA %[X]
Çok Al Az Öde             | Sünger & ponpon setleri (sarf ürün,      | Çok Al Az Öde: Setini Tamamla         | ÇOK AL AZ ÖDE
                          | tekrar alınır)                           |                                       |
İkinci Ürüne Özel Fırsat  | Fırça/sünger seti + Lip Gloss/Dudak Yağı | İkinci Ürününe %[X] İndirim           | 2. ÜRÜNE %[X]
                          | (çapraz satış)                           |                                       |
```

**Neden bu eşleştirme?**
- **Sepette Ekstra İndirim** fiyat algısını en çok yüksek tutarlı üründe değiştirir; set ürünlerinde indirimin TL karşılığı büyük görünür.
- **Çok Al Az Öde** sarf ürünlerde (sünger, ponpon) doğal çalışır; müşteri zaten yedek almak ister.
- **İkinci Ürüne Özel Fırsat** en düşük fiyatlı ürünü sepete ekletmek için idealdir; dudak ürünleri ikinci ürün olarak sepet ortalamasını yükseltir.

**Vitrin başlığı alternatifleri (Aktif Fırsatlar bandı ve karusel başlıkları için):**

```text
• Şu An Mağazada: Aktif Fırsatlar
• Sepette Ekstra İndirimli Setler
• Fırçanı Al, Süngerini Ekle — Çok Al Az Öde
• İkinci Ürünün Bizden Avantajlı
• Makyajını Dudakla Tamamla: 2. Ürüne %[X]
• Setini Tamamla, Daha Az Öde
```

**Ürün karuseli başlıkları (Modül 02 ve 06):**

```text
Modül 02 (Kampanyalı Ürünler):  Aktif Fırsatlardaki Ürünler
Modül 06 (Setler):              Setlerde Avantaj — Sepette Ekstra İndirim   (kampanya aktifken)
                                Setlerde Avantaj                           (kampanya yokken)
Modül 08 (Dudak):               Makyajını Dudakla Tamamla                  (İkinci ürün kampanyası aktifken
                                                                            alt başlık: 2. Ürüne %[X])
```

#### Dönemsel Kampanya Takvimi (öneri — kupon yok)

Trendyol'un dönemsel kampanyalarına katıldığınızda vitrinde yalnızca başlık ve rozeti değiştirin:

```text
Efsane Kasım             Hero başlığı: "Efsane Güzellik Günleri" — rozet: aktif kampanya (ör. SEPETTE EKSTRA %[X])
Sevgililer Günü (Şubat)  Set karuseli başlığı: "Kendine Güzel Bir Hediye" — İkinci Ürüne Fırsat ile dudak ürünü çapraz satışı
Anneler Günü (Mayıs)     Hediyelik setler öne — başlık: "Annene Profesyonel Dokunuş"
Maaş günleri (ayın 15'i) Aktif kampanya varsa bant başlığı: "Güzellik Molası: Aktif Fırsatlar"
```

---

## 5. Ürün Eşleştirme Tablosu

Kod aralıkları ve ürün grupları işlendi. **"Ürün Adı" sütunu** ürün listeniz bu rehbere aktarılmadığı için boş bırakıldı; doldurduğunuzda Bölüm 2'deki `[LRS-0XX – ...]` yer tutucuları buradan beslenir.

**LRS-001 – LRS-015 — Dudak Ürünleri (çapraz satış, Modül 08)**

```text
KOD      | ÜRÜN GRUBU                    | ÜRÜN ADI (doldurun) | ROL
---------|-------------------------------|---------------------|-------------------------------
LRS-001  | Dudak (Lip Gloss / Dudak Yağı)|                     | Çapraz satış / 2. ürün
LRS-002  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-003  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-004  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-005  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-006  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-007  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-008  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-009  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-010  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-011  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-012  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-013  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-014  | Dudak (Lip Gloss / Dudak Yağı)|                     |
LRS-015  | Dudak (Lip Gloss / Dudak Yağı)|                     |
```

**LRS-016 – LRS-045 — Fırça & Sünger Setleri (vitrinin odağı)**

```text
KOD      | ÜRÜN GRUBU            | FIRÇA / SÜNGER | ÜRÜN ADI (doldurun) | ROL
---------|-----------------------|----------------|---------------------|------------------------------------
LRS-016  | Fırça & Sünger Seti   |                |                     | Hero / Çok Satan / Set / Kampanya
LRS-017  | Fırça & Sünger Seti   |                |                     |
LRS-018  | Fırça & Sünger Seti   |                |                     |
LRS-019  | Fırça & Sünger Seti   |                |                     |
LRS-020  | Fırça & Sünger Seti   |                |                     |
LRS-021  | Fırça & Sünger Seti   |                |                     |
LRS-022  | Fırça & Sünger Seti   |                |                     |
LRS-023  | Fırça & Sünger Seti   |                |                     |
LRS-024  | Fırça & Sünger Seti   |                |                     |
LRS-025  | Fırça & Sünger Seti   |                |                     |
LRS-026  | Fırça & Sünger Seti   |                |                     |
LRS-027  | Fırça & Sünger Seti   |                |                     |
LRS-028  | Fırça & Sünger Seti   |                |                     |
LRS-029  | Fırça & Sünger Seti   |                |                     |
LRS-030  | Fırça & Sünger Seti   |                |                     |
LRS-031  | Fırça & Sünger Seti   |                |                     |
LRS-032  | Fırça & Sünger Seti   |                |                     |
LRS-033  | Fırça & Sünger Seti   |                |                     |
LRS-034  | Fırça & Sünger Seti   |                |                     |
LRS-035  | Fırça & Sünger Seti   |                |                     |
LRS-036  | Fırça & Sünger Seti   |                |                     |
LRS-037  | Fırça & Sünger Seti   |                |                     |
LRS-038  | Fırça & Sünger Seti   |                |                     |
LRS-039  | Fırça & Sünger Seti   |                |                     |
LRS-040  | Fırça & Sünger Seti   |                |                     |
LRS-041  | Fırça & Sünger Seti   |                |                     |
LRS-042  | Fırça & Sünger Seti   |                |                     |
LRS-043  | Fırça & Sünger Seti   |                |                     |
LRS-044  | Fırça & Sünger Seti   |                |                     |
LRS-045  | Fırça & Sünger Seti   |                |                     |
```

**Rol atama kuralları:**
- **Hero:** En çok satan 1 fırça seti + en çok satan 1 sünger seti (görsel olarak en fotojenik olanlar).
- **Kampanya (Modül 02):** Yalnızca aktif kampanyaya dahil ürünler; kampanya bitince listeden çıkarın.
- **Çok Satanlar karuseli (Modül 04):** Son 30 günün satış adedine göre ilk 8–12 ürün; puanı 4,3 altı olanları çıkarın.
- **Setler karuseli (Modül 06):** Çoklu paketler ve sepet ortalamasını en çok yükselten ürünler.
- **Dudak karuseli (Modül 08):** LRS-001 – LRS-015 arasından en çok satan 6–8 ürün; İkinci Ürüne Özel Fırsat aktifse kampanyaya dahil olanlar önde.

---

## 6. Yayın Sonrası Ölçüm (ilk 30 gün)

```text
METRİK                               | NEREDEN                       | HEDEF / AKSİYON
-------------------------------------|-------------------------------|----------------------------------------------
Mağaza sayfası → ürün tıklama        | Panel mağaza istatistikleri   | Hero değişikliği sonrası artış
Aktif Fırsatlar bandı → karusel tık  | Mağaza istatistikleri         | Düşükse bant metnini kısalt, rakamı büyüt
Kampanyalı ürün satış payı           | Kampanya / satış raporları    | Toplam satış içinde artış
Sepet başına ürün adedi              | Satış raporları               | Çok Al Az Öde + 2. Ürün sonrası 1'in üzerine
Dudak ürünü çapraz satış oranı       | Sipariş raporları             | Fırça/sünger siparişlerinde dudak ürünü payı
Ortalama sepet tutarı (AOV)          | Satış raporları               | Kampanya dönemlerinde artış
```

A/B testi: Hero'yu 14 günde bir Seçenek A ↔ B/C arasında değiştirin; diğer her şey sabitken yalnızca bir değişkeni test edin. Kampanya değiştiğinde test sayacını sıfırlayın.
