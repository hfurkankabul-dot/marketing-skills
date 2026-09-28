# Secret de Femme × Loresse — Trendyol Mağaza Tasarım Rehberi

> Kapsam: Secret de Femme çatı markası altında Loresse serisi (LRS-016 – LRS-045).
> Hedef: Mağaza sayfası dönüşüm oranı (CVR), takipçi artışı, sepet ortalaması (AOV).
> Kullanım: Her `text` bloğu doğrudan Canva metin kutusuna veya Trendyol paneline kopyalanabilir.

---

## 0. Başlamadan Önce — 3 Kritik Not

1. **Ürün eşleştirmesi:** LRS kodlarının hangi ürüne karşılık geldiği bu rehberde bilinmiyor. Görsel kompozisyonlarda `[LRS-0XX – Kabuki Fırça]` gibi yer tutucular var; köşeli parantezleri kendi ürün kodunuzla değiştirin. Bölüm 5'teki eşleştirme tablosunu bir kez doldurmanız yeterli.
2. **"Anti-bakteriyel" ifadesi:** Bu iddiayı yalnızca elinizde laboratuvar test raporu / sertifika varsa kullanın. Belge yoksa Trendyol içerik denetimi ve Ticaret Bakanlığı reklam mevzuatı açısından risklidir; aynı alanda **"Hijyenik & Kolay Temizlenir"** alternatifini kullanın (metinlerde ikisi de verildi).
3. **Banner ölçüleri:** Aşağıdaki ölçüler sizin belirlediğiniz ölçülerdir. Trendyol mağaza editöründe widget ölçüleri zaman zaman güncellenir; tasarıma başlamadan önce panelde ilgili widget'ın "önerilen görsel boyutu" bilgisini kontrol edin. Oran aynı kalırsa Canva'da **Yeniden Boyutlandır** ile saniyeler içinde uyarlarsınız.

---

## 1. Trendyol Mağaza Dizilimi & Modül Sıralaması

Mantık: **Dikkat → Teşvik → Keşif → Kanıt → Arzu → Güven → Satın alma.** Mobilde ilk ekran (ilk ~700 px) hero + kupon ile bitmeli; kullanıcı kaydırmadan "neden şimdi almalıyım" sorusunun cevabını görmeli.

```text
SIRA | MODÜL                              | ÖLÇÜ          | AMACI
-----|------------------------------------|---------------|--------------------------------------------
01   | Hero Banner                        | 1200 x 400    | Marka + teklif + takip kuponu (ilk izlenim)
02   | Kupon Alanı (Takip Et + Sepet)     | Panel widget  | Anında teşvik, sepet ortalamasını yükseltme
03   | Üçlü Kategori Grid                 | 3 x 400 x 400 | Hızlı yönlendirme (Fırça / Sünger / Set)
04   | Öne Çıkan Ürünler – "Çok Satanlar" | Ürün karuseli | Sosyal kanıt, en yüksek CVR'li 8–12 ürün
05   | İkili Promo Banner                 | 2 x 600 x 600 | Fırçalar vs. Süngerler/Ponponlar hikâyesi
06   | Ürün Listesi – "Setlerde Avantaj"  | Ürün karuseli | Sepet ortalaması (AOV) — set/paket ürünler
07   | Güven Bandı                        | 1200 x 200    | Tereddüt kırma (kalite, orijinallik, kargo)
08   | Ürün Listesi – "Yeni Gelenler"     | Ürün karuseli | Tekrar ziyaret eden takipçiye tazelik
09   | Tüm Ürünler (LRS-016 – LRS-045)    | Ürün grid     | Kapanış; kaydıran kullanıcıya tam katalog
```

**Neden bu sıra?**
- Kupon hero'nun hemen altında: takip kuponu en ucuz müşteri edinim aracıdır; görünmezse kullanılmaz.
- Çok Satanlar, İkili Banner'dan önce: satın almaya hazır kullanıcı hikâyeyi beklemeden ürüne ulaşır.
- Güven Bandı set karuselinin hemen altında: yüksek tutarlı sepette tereddüt en yüksek noktadadır.

**Kampanya dönemleri (Efsane Kasım, Sevgililer Günü, Anneler Günü):** Yalnızca 01 (Hero) ve 06'nın başlığını değiştirin; iskelet sabit kalsın.

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

**Metinler — Seçenek A (Önerilen, marka odaklı):**

```text
ÜST ETİKET (küçük, harf aralıklı):   SECRET DE FEMME × LORESSE
ANA BAŞLIK:                           Kusursuz Ten, Tek Dokunuşta
ALT BAŞLIK:                           Yumuşacık sentetik kıllı fırçalar ve pürüzsüz bitiş veren süngerlerle profesyonel makyaj artık evinde.
ROZET:                                TAKİP ET / KUPONU KAZAN
CTA BUTON:                            Koleksiyonu Keşfet
```

**Seçenek B (teklif odaklı — kampanya dönemleri için):**

```text
ÜST ETİKET:   LORESSE PROFESYONEL SERİ
ANA BAŞLIK:   Makyajın Sırrı Fırçasında
ALT BAŞLIK:   Takip et, ilk siparişine özel indirimi kap. Stoklar sınırlı!
ROZET:        TAKİPÇİYE ÖZEL / 30 TL KUPON
CTA BUTON:    Hemen Alışverişe Başla
```

**Seçenek C (A/B testi için kısa):**

```text
ANA BAŞLIK:   Pürüzsüz Ten İçin Profesyonel Dokunuş
ALT BAŞLIK:   Dökülmeyen kıllar • Yumuşak doku • Uzun ömürlü kullanım
ROZET:        TAKİP ET / KUPON KAZAN
CTA BUTON:    Şimdi İncele
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

KOMPOZİSYON 3 – "Set Vitrini" (set/paket ürününüz varsa)
  • Açık fırça çantası/kutusu ortada, içinden fırçalar dışarı taşıyor: [LRS-0XX – Set]
  • Önde pudra dokusu (serpilmiş pudra fotoğrafı, %60 opaklık)
```

---

### 2.2 İkili Promo Banner — 2 x 600 x 600 px

**Ortak yerleşim:** Üst %45 metin, alt %55 ürün. Kenarlarda 40 px güvenli boşluk. İki banner yan yana aynı hizada görünmeli; başlık satırlarının y-koordinatı eşit olmalı (y: 70).

#### Banner 1 — FIRÇALAR

```text
ÜST ETİKET:     LORESSE FIRÇA KOLEKSİYONU
BAŞLIK:         Kadife Dokunuş, Kusursuz Dağılım
ALT METİN:      Sentetik Kıl Teknolojisi ile ürünü emmez, eşit dağıtır.
ÖZELLİK 1:      ✓ Sentetik Kıl Teknolojisi
ÖZELLİK 2:      ✓ Dökülmeyen Kıl Yapısı
ÖZELLİK 3:      ✓ Anti-Bakteriyel Kıl*   (belge yoksa: ✓ Hijyenik & Kolay Temizlenir)
CTA:            Fırçaları Keşfet →
```

Alternatif sloganlar:

```text
• Her Fırça Darbesinde Profesyonel Sonuç
• Yumuşak Kıl, Keskin Çizgi
• Fondöten'den Fara, Tek Seri
```

Görsel: 3–4 fırça dikey ve hafif çapraz dizilim, zemin #1C1C1C (mat siyah) — fırçaların rose gold/nude tonları bu zeminde öne çıkar. Metinler #FFFFFF, özellik tikleri #D4A5A5.

#### Banner 2 — SÜNGERLER & PONPONLAR

```text
ÜST ETİKET:     LORESSE SÜNGER & PONPON
BAŞLIK:         Pürüzsüz Ten, Doğal Bitiş
ALT METİN:      Nemlendiğinde büyüyen yumuşak dokusuyla iz bırakmadan kapatır.
ÖZELLİK 1:      ✓ Pürüzsüz Ten Etkisi
ÖZELLİK 2:      ✓ Lateks İçermez*  (yalnızca ürün bilgisinde doğrulanmışsa)
ÖZELLİK 3:      ✓ Islak & Kuru Kullanım
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

### 2.3 Üçlü Kategori Grid — 3 x 400 x 400 px

Kural: Görsel üzerinde **en fazla 2 satır**, en az 36 px başlık. Mobilde bu kareler ~115 px'e küçülür; uzun metin okunmaz.

```text
KART 1 — FIRÇALAR
  Başlık:      FIRÇALAR
  Alt satır:   Yüz & Göz
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

Alternatif (setiniz yoksa 3. kart):

```text
KART 3 — ÇOK SATANLAR
  Başlık:      ÇOK SATANLAR
  Alt satır:   En Sevilenler
```

Yerleşim: Başlık alt kenardan 60 px yukarıda, ortalı; başlığın altında 60 x 2 px #B76E79 çizgi. Metin Montserrat Bold 36 px, harf aralığı 150, #1C1C1C. Ürün görseli karenin üst %65'inde.

---

### 2.4 Güven Bandı — 1200 x 200 px

Yerleşim: 3 eşit sütun (400 px), her sütunda solda 56 px ikon + sağda 2 satır metin. Sütunlar arasında 1 px #D9C3B8 dikey ayırıcı (y: 50–150). Zemin #FAF6F2 veya #1C1C1C (koyu versiyon).

**Seçenek A (önerilen):**

```text
SÜTUN 1  İkon: kalkan/yıldız
  Başlık:  Anti-Bakteriyel & Dökülmeyen Kıl*
  Alt:     Uzun ömürlü, hijyenik kullanım
  (belge yoksa → Başlık: Dökülmeyen Premium Kıl  /  Alt: Hijyenik, kolay temizlenir)

SÜTUN 2  İkon: kutu/mühür
  Başlık:  %100 Orijinal Ambalaj
  Alt:     Secret de Femme güvencesiyle

SÜTUN 3  İkon: kargo kamyonu
  Başlık:  Hızlı Kargo
  Alt:     Aynı gün / 24 saatte kargoda**
```

`**` Kargoya veriliş sürenizi paneldeki "Kargoya Teslim Süresi" ile birebir eşleştirin. Söz veremediğiniz süreyi yazmayın; alternatif: **"Özenle Paketlenir, Hızla Yola Çıkar"**.

**Seçenek B (kısa, mobil dostu):**

```text
✓ Dökülmeyen Kıl   ✓ Orijinal Ambalaj   ✓ Hızlı Kargo
```

Tipografi: Başlık Montserrat SemiBold 18 px #1C1C1C, alt satır Montserrat Regular 14 px #7A6A66. İkonlar tek renk #B76E79, çizgi (outline) stili.

---

## 3. Canva Stil & Renk Rehberi

### 3.1 Renk Paleti

```text
ROL                 İSİM              HEX       KULLANIM
------------------  ----------------  --------  ------------------------------------------
Ana vurgu           Rose Gold         #B76E79   Rozet, ince çizgiler, ikonlar, başlık vurgusu
Ana vurgu (açık)    Dusty Rose        #D4A5A5   Tikler, ikincil vurgular (koyu zeminde)
Nötr zemin 1        Nude              #E8CFC1   Kategori kartları, hero degrade sonu
Nötr zemin 2        Blush Nude        #F7EDE8   Hero degrade başı, açık bannerlar
Nötr zemin 3        Ivory             #FAF6F2   Güven bandı, geniş boşluklar
Lüks aksan          Şampanya          #F7E7CE   Set/premium ürün kartları
Metin & kontrast    Mat Siyah         #1C1C1C   Başlıklar, CTA buton dolgusu, koyu banner
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

ELEMENT / GÖRSEL ARAMALARI
  rose gold line frame
  gold foil circle badge
  soft shadow podium
  beige arch shape
  powder splash
  makeup powder texture
  silk fabric background nude
  water droplet 3d
  minimal line icon shipping / shield / box (outline)

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
4. Dışa aktarım: JPG, kalite %85–90 (Trendyol yükleme sınırını aşmamak için). Metin ağırlıklı güven bandı için PNG.
5. Dosya adı: sdf-loresse-hero-1200x400-v1.jpg (versiyonla; A/B testi için şart).
```

---

## 4. Trendyol Kategori Ağacı & Kupon Kurgusu

### 4.1 Önemli Ayrım

- **Trendyol ürün kategorisi** (ör. Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası) Trendyol'un sabit ağacıdır; ürünü doğru yaprak kategoriye atamak arama görünürlüğünün temelidir.
- **Mağaza içi kategori / koleksiyon** ise mağaza sayfanızda sizin açtığınız ürün listeleridir. Aşağıdaki ağaç bu mağaza içi yapı içindir.

**Trendyol ürün kategorisi eşleştirmesi (ürün yüklerken):**

```text
Fırçalar           → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası
Fırça setleri      → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Fırçası Seti
Sünger / Ponpon    → Kozmetik > Makyaj > Makyaj Aksesuarları > Makyaj Süngeri / Pudra Ponponu
```

(Panelde yaprak kategori adları farklı görünebilir; ürün yüklerken en spesifik eşleşmeyi seçin.)

### 4.2 Mağaza İçi Kategori Ağacı (SEO uyumlu adlar)

İsimlendirme kuralı: **Arama yapılan kelime + fayda/tip.** "Koleksiyon 1" gibi soyut isimler yerine kullanıcının aradığı kelimeyi kullanın.

```text
1. Makyaj Fırçaları
   1.1 Fondöten Fırçası
   1.2 Pudra & Kabuki Fırçası
   1.3 Allık & Kontür Fırçası
   1.4 Far & Göz Makyaj Fırçası
   1.5 Kaş & Eyeliner Fırçası
   1.6 Makyaj Fırçası Setleri

2. Makyaj Süngerleri & Ponponlar
   2.1 Damla Makyaj Süngeri
   2.2 Kapatıcı & Detay Süngeri
   2.3 Pudra Ponponu
   2.4 Sünger Setleri

3. Avantajlı Setler & Hediyelik
   3.1 Fırça + Sünger Kombin Setleri
   3.2 Hediyelik Makyaj Setleri

4. Çok Satanlar
5. Yeni Gelenler
```

**Ürün başlığı formülü (arama + CVR için):**

```text
Secret de Femme Loresse [Ürün Tipi] [Ana Fayda] [Özellik] – [Adet/Renk] (LRS-0XX)

Örnek:
Secret de Femme Loresse Kabuki Pudra Fırçası Sentetik Kıllı Dökülmeyen Yumuşak Doku – Rose Gold
Secret de Femme Loresse Damla Makyaj Süngeri Lateks İçermez Pürüzsüz Bitiş – 2'li Set
```

(Ürün kodunu başlıkta değil, "Model Kodu / Stok Kodu" alanında tutmak daha temiz görünür; başlık karakter limitine dikkat.)

### 4.3 Kupon Kurgusu

Ön kabul: Loresse ürünlerinin ortalama satış fiyatı ~150–350 TL aralığında varsayılmıştır. **Kendi ortalama sepet tutarınızı (AOV) panelden kontrol edin** ve alt limitleri ona göre kaydırın: 1. kademe ≈ mevcut AOV'nin %20 üstü, 2. kademe ≈ %70 üstü.

Kupon maliyeti satıcıya aittir; toplam indirim oranı brüt kârın ~%10–12'sini geçmemeli.

#### A) Mağazayı Takip Et Kuponu

```text
Kampanya adı (panel):  SDF Takipçi Hoş Geldin
Müşteriye görünen:     Takip Et, 30 TL Kazan!
İndirim:               30 TL
Alt sepet limiti:      250 TL
Geçerlilik:            Takip tarihinden itibaren 14 gün (panel seçeneğine göre)
Kullanım:              Kişi başı 1
Efektif indirim:       %12 (limitte)
```

Alternatif (yüksek fiyatlı set ağırlıklıysanız): **50 TL / 400 TL alt limit.**

#### B) Kademeli Sepet Kuponları

```text
KADEME | KAMPANYA ADI (PANEL)     | MÜŞTERİYE GÖRÜNEN BAŞLIK            | ALT LİMİT | İNDİRİM | EFEKTİF
-------|--------------------------|-------------------------------------|-----------|---------|--------
1      | SDF Sepet 1 – Başlangıç   | 350 TL'ye 35 TL İndirim             | 350 TL    | 35 TL   | %10
2      | SDF Sepet 2 – Set Avantaj | 600 TL'ye 75 TL İndirim             | 600 TL    | 75 TL   | %12,5
3      | SDF Sepet 3 – Pro Kit     | 1.000 TL'ye 150 TL İndirim          | 1.000 TL  | 150 TL  | %15
```

**Neden bu kademe?** Her basamak bir öncekinden daha yüksek efektif oran sunar; müşteri "bir ürün daha eklersem daha kârlı" hesabı yapar. Kademe 2, "fırça + sünger" kombinini hedefler.

**Kampanya başlığı alternatifleri (kupon widget'ı ve hero rozeti için):**

```text
• Sepette Kademeli İndirim: 150 TL'ye Varan Fırsat
• Ne Kadar Çok, O Kadar Avantaj
• Makyaj Çantanı Tamamla, İndirimi Büyüt
• Fırça + Sünger Al, Sepette Kazan
• Takipçilere Özel: İlk Siparişte 30 TL Hediye
```

#### C) Dönemsel Kupon Takvimi (öneri)

```text
Efsane Kasım             Kademeler +%20 (ör. 350'ye 45 / 600'e 90 / 1000'e 180) — başlık: "Efsane Güzellik Günleri"
Sevgililer Günü (Şubat)  Set kategorisine özel 60 TL — başlık: "Kendine Güzel Bir Hediye"
Anneler Günü (Mayıs)     Hediyelik setlere 75 TL — başlık: "Annene Profesyonel Dokunuş"
Maaş günleri (ayın 15'i) 48 saatlik flaş kupon 40 TL / 300 TL — başlık: "48 Saatlik Güzellik Molası"
```

---

## 5. Ürün Eşleştirme Tablosu (Doldurulacak)

Bu tabloyu bir kez doldurun; bölüm 2'deki tüm `[LRS-0XX – ...]` yer tutucuları buradan beslenir.

```text
KOD      | ÜRÜN ADI / TİPİ       | ALT KATEGORİ (4.2) | ROL
---------|-----------------------|--------------------|-------------------------------------
LRS-016  |                       |                    | Hero / Çok Satan / Set / Katalog
LRS-017  |                       |                    |
LRS-018  |                       |                    |
LRS-019  |                       |                    |
LRS-020  |                       |                    |
LRS-021  |                       |                    |
LRS-022  |                       |                    |
LRS-023  |                       |                    |
LRS-024  |                       |                    |
LRS-025  |                       |                    |
LRS-026  |                       |                    |
LRS-027  |                       |                    |
LRS-028  |                       |                    |
LRS-029  |                       |                    |
LRS-030  |                       |                    |
LRS-031  |                       |                    |
LRS-032  |                       |                    |
LRS-033  |                       |                    |
LRS-034  |                       |                    |
LRS-035  |                       |                    |
LRS-036  |                       |                    |
LRS-037  |                       |                    |
LRS-038  |                       |                    |
LRS-039  |                       |                    |
LRS-040  |                       |                    |
LRS-041  |                       |                    |
LRS-042  |                       |                    |
LRS-043  |                       |                    |
LRS-044  |                       |                    |
LRS-045  |                       |                    |
```

**Rol atama kuralları:**
- **Hero:** En çok satan 1 fırça + en çok satan 1 sünger (görsel olarak en fotojenik olanlar).
- **Çok Satanlar karuseli (Modül 04):** Son 30 günün satış adedine göre ilk 8–12 ürün; puanı 4,3 altı olanları çıkarın.
- **Setler karuseli (Modül 06):** Çoklu paketler ve sepet ortalamasını en çok yükselten ürünler.

---

## 6. Yayın Sonrası Ölçüm (ilk 30 gün)

```text
METRİK                        | NEREDEN                      | HEDEF
------------------------------|------------------------------|-----------------------------------
Mağaza sayfası → ürün tıklama | Panel mağaza istatistikleri  | Hero değişikliği sonrası artış
Takipçi artışı                | Mağaza takipçi sayısı        | Haftalık düzenli artış
Takip kuponu kullanım oranı   | Kupon raporları              | Kullanılmıyorsa limit düşür
Kademe 2–3 kupon kullanımı    | Kupon raporları              | Az kullanılıyorsa limitleri %10 düşür
Ortalama sepet tutarı (AOV)   | Satış raporları              | Kademe 1 limitine yaklaşmalı
```

A/B testi: Hero'yu 14 günde bir Seçenek A ↔ B/C arasında değiştirin; diğer her şey sabitken yalnızca bir değişkeni test edin.
