"""
TCDD Sefer Gecikme Tahmini — Demo Arayüzü
Intellica Yaz Stajı 2026 / Mehmet Alper

Calistirmak icin:  python app.py
"""

from pathlib import Path

import gradio as gr
import joblib
import matplotlib

matplotlib.use("Agg")  # penceresiz (sunucu) cizim arka ucu
import matplotlib.pyplot as plt
import pandas as pd

# --- Model yukleme -----------------------------------------------------------
MODEL_PATH = Path(__file__).parent / "tcdd_demo_model.pkl"

bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
FEATURES = bundle["features"]

MAE = 5.75  # test setindeki ortalama mutlak hata (dk)

# --- Alan bilgisi ------------------------------------------------------------
HAVA_SIDDETI = {
    "Açık": 0,
    "Bilinmiyor": 0,
    "Yağmurlu": 1,
    "Sisli": 2,
    "Fırtınalı": 2,
    "Karlı": 2,
}

SEVIYE_ETIKET = {
    0: "Açık / bilinmiyor",
    1: "Yağmurlu",
    2: "Sisli / fırtınalı / karlı",
}

SEVIYE_RENK = {0: "#2e8b57", 1: "#d99423", 2: "#c0392b"}

ZIRVE_SAATLER = "07:00-09:00 ve 17:00-19:00"


def zirve_mi(saat):
    """Kalkis saati zirve araliginda mi?"""
    return int(7 <= saat <= 9 or 17 <= saat <= 19)


def tahmin_uret(hava_siddeti, saat, kalkis_gecikmesi):
    """Tek bir sefer icin tahmin dondurur."""
    X = pd.DataFrame(
        [[hava_siddeti, zirve_mi(saat), kalkis_gecikmesi]],
        columns=FEATURES,
    )
    return float(model.predict(X)[0])


def gecikme_grafigi(secili_siddet, secili_saat, kalkis_gecikmesi):
    """Saate gore gecikme egrilerini cizer, secili seferi isaretler."""
    plt.close("all")  # onceki cizimleri bellekte biriktirme

    saatler = list(range(24))
    zirve_bayraklari = [zirve_mi(s) for s in saatler]

    fig, ax = plt.subplots(figsize=(7.5, 4))

    for seviye in (0, 1, 2):
        # 24 saatin tahminini tek seferde uret (dongu yerine vektorel)
        X = pd.DataFrame(
            {
                FEATURES[0]: seviye,
                FEATURES[1]: zirve_bayraklari,
                FEATURES[2]: kalkis_gecikmesi,
            },
            index=saatler,
        )
        y = model.predict(X)

        vurgu = seviye == secili_siddet
        ax.step(
            saatler,
            y,
            where="mid",
            label=SEVIYE_ETIKET[seviye],
            color=SEVIYE_RENK[seviye],
            linewidth=2.8 if vurgu else 1.4,
            alpha=1.0 if vurgu else 0.45,
        )

    # Zirve saat bantlarini golgele
    for baslangic, bitis in [(6.5, 9.5), (16.5, 19.5)]:
        ax.axvspan(baslangic, bitis, color="#000000", alpha=0.05)

    # Kullanicinin sectigi sefer
    secili_tahmin = tahmin_uret(secili_siddet, secili_saat, kalkis_gecikmesi)
    ax.scatter(
        [secili_saat],
        [secili_tahmin],
        s=110,
        color="#111111",
        zorder=5,
        label="Seçilen sefer",
    )
    ax.annotate(
        f"{secili_tahmin:.1f} dk",
        xy=(secili_saat, secili_tahmin),
        xytext=(6, 8),
        textcoords="offset points",
        fontsize=10,
        fontweight="bold",
    )

    ax.set_xlabel("Kalkış saati")
    ax.set_ylabel("Tahmini gecikme (dk)")
    ax.set_title("Saate ve hava koşuluna göre tahmini gecikme")
    ax.set_xticks(range(0, 24, 2))
    ax.set_xlim(-0.5, 23.5)
    ax.set_ylim(bottom=0)
    ax.grid(axis="y", alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()

    return fig


def tahmin_et(hava, saat, kalkis_gecikmesi):
    """Arayuzun cagirdigi ana fonksiyon: metin ozeti ve grafik dondurur."""
    saat = int(saat)
    kalkis_gecikmesi = float(kalkis_gecikmesi or 0)
    hava_siddeti = HAVA_SIDDETI[hava]

    tahmin = tahmin_uret(hava_siddeti, saat, kalkis_gecikmesi)
    zirve = zirve_mi(saat)

    ozet = f"""
### Tahmini varış gecikmesi: **{tahmin:.1f} dakika**

Beklenen aralık: {max(0, tahmin - MAE):.1f} – {tahmin + MAE:.1f} dk
*(± ortalama mutlak hata)*

**Tahmin nasıl oluştu**

| Bileşen | Katkı |
|---|---|
| Taban gecikme | {model.intercept_:.1f} dk |
| Hava şiddeti ({hava}, seviye {hava_siddeti}) | {hava_siddeti * model.coef_[0]:+.1f} dk |
| Zirve saat ({'evet' if zirve else 'hayır'}) | {zirve * model.coef_[1]:+.1f} dk |
| Kalkış gecikmesi ({kalkis_gecikmesi:.0f} dk) | {kalkis_gecikmesi * model.coef_[2]:+.1f} dk |
"""

    return ozet, gecikme_grafigi(hava_siddeti, saat, kalkis_gecikmesi)


# --- Arayuz ------------------------------------------------------------------
with gr.Blocks(title="TCDD Gecikme Tahmini") as demo:
    gr.Markdown("# TCDD Sefer Gecikme Tahmini")
    gr.Markdown(
        "Intellica yaz stajı — 11.853 gerçek sefer kaydıyla eğitilmiş "
        "doğrusal regresyon modeli. Test MAE: 5.75 dk, R²: 0.643."
    )

    with gr.Row():
        with gr.Column():
            hava_input = gr.Dropdown(
                choices=list(HAVA_SIDDETI.keys()),
                value="Açık",
                label="Hava durumu",
            )
            saat_input = gr.Slider(
                minimum=0,
                maximum=23,
                step=1,
                value=8,
                label="Kalkış saati",
                info=f"Zirve saatler: {ZIRVE_SAATLER}",
            )
            gecikme_input = gr.Number(
                value=0,
                label="Kalkışta oluşan gecikme (dk)",
                info="Tren perondan ayrılırken bilinen gecikme",
            )
            btn = gr.Button("Tahmin Et", variant="primary")

        with gr.Column():
            cikti = gr.Markdown("Değerleri seçip **Tahmin Et**'e bas.")

    grafik = gr.Plot(label="Gecikme profili")

    gr.Examples(
        examples=[
            ["Açık", 3, 0],
            ["Açık", 8, 0],
            ["Karlı", 8, 0],
            ["Karlı", 8, 15],
        ],
        inputs=[hava_input, saat_input, gecikme_input],
        label="Hazır senaryolar",
    )

    gr.Markdown(
        "---\n"
        "Üç eğrinin paralel olması, hava koşulu ile zirve saat etkilerinin "
        "toplamsal olduğunu gösterir: her hava koşulunda zirve saat aynı "
        "miktarda gecikme ekler. Eğrilerin basamaklı olması ise saat etkisinin "
        "kademeli değil keskin olduğunu gösterir."
    )

    btn.click(
        fn=tahmin_et,
        inputs=[hava_input, saat_input, gecikme_input],
        outputs=[cikti, grafik],
    )


if __name__ == "__main__":
    demo.launch(inbrowser=True)
