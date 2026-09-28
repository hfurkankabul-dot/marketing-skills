"""Cildoss UGC Reels kurgu betiği.

Ham UGC videolarını 9:16 1080x1920'ye keser, ElevenLabs seslendirmesini ekler,
başlık yazıları + altyazı + kapanış kartını (ürün görseli, fiyat) bindirir.

Kullanım: python3 build_reels.py
"""
import os
import subprocess
import textwrap

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.environ.get("CILDOSS_SRC", "/root/.claude/uploads/dd5e789e-63e3-5a64-8cc1-cd4590aea9d6")
PRODUCT_IMG = os.environ.get(
    "CILDOSS_PRODUCT",
    "/tmp/claude-0/-home-user-marketing-skills/dd5e789e-63e3-5a64-8cc1-cd4590aea9d6/images/1.jpg",
)
VO = os.path.join(ROOT, "seslendirme")
OUT = os.path.join(ROOT, "cikti")
TMP = os.path.join(ROOT, ".build")
FFMPEG = "ffmpeg"

W, H, FPS = 1080, 1920, 30
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BROWN = (59, 36, 24)
CREAM = (239, 230, 218)

CLIPS = {
    "ugc1": f"{SRC}/dc77d52d-ugc1.mp4",
    "ugc3": f"{SRC}/cbcc854d-ugc3.mp4",
    "ugc4": f"{SRC}/28549b3f-ugc4.mp4",
    "dl12": f"{SRC}/828cf0af-Download_12.mp4",
}

# Bölüm = (bitiş sn, başlık yazısı, altyazı, [(klip, başlangıç sn), ...] veya "END")
VARIANTS = {
    "A-heyecanli": {
        "vo": "A-heyecanli.mp3",
        "sections": [
            (3.9, "SABAH ŞİŞKİNLİĞİ?", "Sabah uyanınca yüzüm hep böyle şiş görünüyordu...",
             [("ugc3", 2.0), ("ugc1", 32.0)]),
            (9.4, "2 DAKİKALIK SABAH RUTİNİ", "Sonra bu lenf drenaj fırçasıyla her sabah iki dakikalık masaj yapmaya başladım.",
             [("dl12", 0.0), ("ugc1", 4.0), ("ugc3", 12.0)]),
            (13.1, "DAHA DİNÇ GÖRÜNÜM", "Yüzüm daha dinç, çene hattım da çok daha belirgin görünüyor!",
             [("ugc4", 2.0), ("ugc4", 16.0)]),
            (17.45, "+ HEDİYE SIMPLE SPF30", "Şu an seti alana Simple SPF30 nemlendirici hediye!",
             [("dl12", 20.0), ("ugc3", 33.5)]),
            (None, "STOKLAR BİTMEDEN!", "699 TL, kargo bedava, kapıda ödeme. Stoklar bitmeden kap!", "END"),
        ],
    },
    "A-samimi": {
        "vo": "A-samimi.mp3",
        "sections": [
            (3.25, "SABAH ŞİŞKİNLİĞİ?", "Sabah uyanınca yüzüm hep böyle şiş görünüyordu...",
             [("ugc3", 2.0), ("ugc1", 32.0)]),
            (7.9, "2 DAKİKALIK SABAH RUTİNİ", "Sonra bu lenf drenaj fırçasıyla her sabah iki dakikalık masaj yapmaya başladım.",
             [("dl12", 0.0), ("ugc1", 4.0), ("ugc3", 12.0)]),
            (11.2, "DAHA DİNÇ GÖRÜNÜM", "Yüzüm daha dinç, çene hattım da çok daha belirgin görünüyor.",
             [("ugc4", 2.0), ("ugc4", 16.0)]),
            (14.8, "+ HEDİYE SIMPLE SPF30", "Şu an seti alana Simple SPF30 nemlendirici hediye.",
             [("dl12", 20.0), ("ugc3", 33.5)]),
            (None, "STOKLAR BİTMEDEN!", "699 TL, kargo bedava, kapıda ödeme. Stoklar bitmeden kap!", "END"),
        ],
    },
    "B-samimi": {
        "vo": "B-samimi.mp3",
        "sections": [
            (3.75, "ÇENE HATTI SIRRIM", "Kızlar, çene hattımı belirgin gösteren sabah rutinimi soruyorsunuz...",
             [("ugc1", 31.5)]),
            (6.4, "CILDOSS LENF DRENAJ FIRÇASI", "İşte bu! Cildoss lenf drenaj fırçası.",
             [("ugc3", 33.8), ("dl12", 20.0)]),
            (10.62, "AŞAĞIDAN YUKARI, İÇTEN DIŞA", "Aşağıdan yukarıya, içten dışa doğru hafifçe tarıyorum, iki dakika yetiyor.",
             [("dl12", 0.0), ("ugc3", 26.0), ("ugc4", 2.0)]),
            (13.85, "+ HEDİYE SIMPLE SPF30", "Üstelik şimdi yanında Simple SPF30 krem hediye.",
             [("ugc4", 16.0), ("ugc1", 8.0)]),
            (None, "LİNK PROFİLİMDE", "699 TL, ücretsiz kargo ve kapıda ödeme. Link profilimde!", "END"),
        ],
    },
    "C-heyecanli": {
        "vo": "C-heyecanli.mp3",
        "sections": [
            (3.77, "ÜCRETSİZ SIMPLE KREM\n(SINIRLI SAYIDA)", "Bu fırçayı alana Simple SPF30 krem bedava, ama sınırlı sayıda!",
             [("ugc3", 33.5), ("dl12", 20.0)]),
            (9.0, "SABAH ŞİŞKİNLİĞİNE KARŞI RUTİN", "Cildoss lenf drenaj fırçası, sabah şişkinliğine karşı en sevdiğim rutin.",
             [("dl12", 0.0), ("ugc3", 12.0), ("ugc1", 4.0)]),
            (12.28, "DAHA DİNÇ GÖRÜNÜM", "Yüzüm daha dinç, çene hattım daha belirgin görünüyor.",
             [("ugc4", 2.0), ("ugc4", 16.0)]),
            (None, "HEMEN SİPARİŞ VER", "699 TL, kargo bedava, kapıda ödeme. Hemen sipariş ver!", "END"),
        ],
    },
}


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def duration(path):
    r = subprocess.run([FFMPEG, "-i", path], capture_output=True, text=True)
    for line in r.stderr.splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(path)


def font(size):
    return ImageFont.truetype(BOLD, size)


def rounded_box(draw, xy, fill, radius=28):
    draw.rounded_rectangle(xy, radius=radius, fill=fill)


def headline_png(text, path):
    """Üst bölgede beyaz kutu içinde koyu kahve kalın başlık."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(66)
    lines = []
    for part in text.split("\n"):
        lines += textwrap.wrap(part, 20) or [""]
    lh = 82
    widths = [d.textlength(l, font=f) for l in lines]
    bw = max(widths) + 70
    bh = lh * len(lines) + 40
    x0, y0 = (W - bw) / 2, 300
    rounded_box(d, (x0, y0, x0 + bw, y0 + bh), (255, 255, 255, 240))
    for i, l in enumerate(lines):
        d.text(((W - widths[i]) / 2, y0 + 20 + i * lh), l, font=f, fill=BROWN)
    img.save(path)


def subtitle_png(text, path):
    """Alt-orta bölgede konturlu beyaz altyazı (sessiz izleyenler için)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(50)
    lines = textwrap.wrap(text, 30)
    lh = 64
    y0 = 1150  # Reels alt arayüzünün (açıklama/CTA) üstünde kalsın
    for i, l in enumerate(lines):
        w = d.textlength(l, font=f)
        d.text(((W - w) / 2, y0 + i * lh), l, font=f, fill="white", stroke_width=5, stroke_fill="black")
    img.save(path)


def endcard_png(path):
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    f_top = font(54)
    t = "CILDOSS STARTER SET"
    d.text(((W - d.textlength(t, font=f_top)) / 2, 200), t, font=f_top, fill=BROWN)
    prod = Image.open(PRODUCT_IMG).convert("RGB").resize((860, 860), Image.LANCZOS)
    img.paste(prod, ((W - 860) // 2, 280))
    # Fiyat bandı
    rounded_box(d, (140, 1160, W - 140, 1300), BROWN, radius=40)
    f_price = font(96)
    p = "699 TL"
    d.text(((W - d.textlength(p, font=f_price)) / 2, 1175), p, font=f_price, fill="white")
    f_sub = font(44)
    s = "ÜCRETSİZ KARGO · KAPIDA ÖDEME"
    d.text(((W - d.textlength(s, font=f_sub)) / 2, 1320), s, font=f_sub, fill=BROWN)
    img.save(path)


def cta_png(text, path):
    """Kapanış kartında fiyatın altında beyaz çerçeveli CTA hapı."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = font(52)
    tw = d.textlength(text, font=f)
    x0, y0 = (W - tw - 90) / 2, 1400
    d.rounded_rectangle((x0, y0, x0 + tw + 90, y0 + 96), radius=48, fill=(255, 255, 255), outline=BROWN, width=5)
    d.text((x0 + 45, y0 + 18), text, font=f, fill=BROWN)
    img.save(path)


def make_segment(src, start, dur, path):
    src_dur = duration(CLIPS[src])
    start = max(0.0, min(start, src_dur - dur - 0.05))
    run([FFMPEG, "-y", "-ss", f"{start:.3f}", "-i", CLIPS[src], "-t", f"{dur:.3f}",
         "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1",
         "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", path])


def make_endcard_segment(png, dur, path):
    frames = int(round(dur * FPS))
    run([FFMPEG, "-y", "-loop", "1", "-i", png, "-t", f"{dur:.3f}",
         "-vf", f"scale={W*2}:{H*2},zoompan=z='1+0.04*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},setsar=1",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", path])


def build(name, spec):
    work = os.path.join(TMP, name)
    os.makedirs(work, exist_ok=True)
    vo = os.path.join(VO, spec["vo"])
    total = duration(vo) + 0.6
    endcard = os.path.join(TMP, "endcard.png")
    if not os.path.exists(endcard):
        endcard_png(endcard)

    segs, overlays, t = [], [], 0.0
    for idx, (end, head, sub, clips) in enumerate(spec["sections"]):
        end = total if end is None else end
        sec_dur = end - t
        hp, sp = os.path.join(work, f"h{idx}.png"), os.path.join(work, f"s{idx}.png")
        headline_png(head, hp)
        subtitle_png(sub, sp)
        if clips == "END":
            seg = os.path.join(work, f"seg{idx}_end.mp4")
            make_endcard_segment(endcard, sec_dur, seg)
            segs.append(seg)
            cp = os.path.join(work, f"cta{idx}.png")
            cta_png(head, cp)
            overlays.append((cp, t, end))  # fiyat kartta; altyazı yerine CTA hapı
        else:
            each = sec_dur / len(clips)
            for j, (src, st) in enumerate(clips):
                seg = os.path.join(work, f"seg{idx}_{j}.mp4")
                make_segment(src, st, each, seg)
                segs.append(seg)
            overlays += [(hp, t, end), (sp, t, end)]
        t = end

    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as fh:
        fh.writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(work, "base.mp4")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])

    inputs = ["-i", base, "-i", vo]
    for png, _, _ in overlays:
        inputs += ["-i", png]
    chain, prev = [], "[0:v]"
    for k, (_, a, b) in enumerate(overlays):
        out = f"[v{k}]"
        chain.append(f"{prev}[{k+2}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'{out}")
        prev = out
    chain.append("[1:a]loudnorm=I=-14:TP=-1.5:LRA=11,apad[a]")
    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, f"cildoss-reels-{name}.mp4")
    run([FFMPEG, "-y", *inputs, "-filter_complex", ";".join(chain),
         "-map", prev, "-map", "[a]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", out_path])
    print(f"{out_path}  ({total:.1f} sn)")


if __name__ == "__main__":
    os.makedirs(TMP, exist_ok=True)
    for name, spec in VARIANTS.items():
        build(name, spec)
