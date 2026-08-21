"""
TCDD Sefer Gecikme Tahmini — Demo Arayüzü
Intellica Yaz Stajı 2026 / Mehmet Alper

Calistirmak icin:  python app.py
"""

from pathlib import Path

import gradio as gr
import joblib
import pandas as pd

# --- Model yukleme -----------------------------------------------------------
# Model dosyasini bu betigin bulundugu klasorde arar; boylece uygulamayi
# hangi dizinden calistirdigin fark etmez.
MODEL_PATH = Path(__file__).parent / "tcdd_demo_model.pkl"

bundle = joblib.load(MODEL_PATH)
model = bundle["model"]
FEATURES = bundle["features"]

MAE = 5.75  # test setindeki ortalama mutlak hata (dk)

# --- Alan bilgisi ------------------------------------------------------------
# Hava durumu kategorileri EDA sonucunda 3 siddet seviyesine indirgendi:
# kutu grafikleri sisli / firtinali / karli arasinda anlamli fark gostermedi,
# "bilinmiyor" ise "acik" ile ayni davrandi.
HAVA_SIDDETI = {
    "Açık": 0,
    "Bilinmiyor": 0,
    "Yağmurlu": 1,
    "Sisli": 2,
    "Fırtınalı": 2,
    "Karlı": 2,
}

ZIRVE_SAATLER = "07:00-09:00 ve 17:00-19:00"


def tahmin_et(hava, saat, kalkis_gecikmesi):
    """Kullanici girdilerini model ozelliklerine cevirip tahmin uretir."""
    saat = int(saat)
    kalkis_gecikmesi = float(kalkis_gecikmesi or 0)

    hava_siddeti = HAVA_SIDDETI[hava]
    zirve_saat_mi = int(7 <= saat <= 9 or 17 <= saat <= 19)

    X = pd.DataFrame(
        [[hava_siddeti, zirve_saat_mi, kalkis_gecikmesi]],
        columns=FEATURES,
    )
    tahmin = float(model.predict(X)[0])

    return f"""
### Tahmini varış gecikmesi: **{tahmin:.1f} dakika**

Beklenen aralık: {max(0, tahmin - MAE):.1f} – {tahmin + MAE:.1f} dk
*(± ortalama mutlak hata)*

**Tahmin nasıl oluştu**

| Bileşen | Katkı |
|---|---|
| Taban gecikme | {model.intercept_:.1f} dk |
| Hava şiddeti ({hava}, seviye {hava_siddeti}) | {hava_siddeti * model.coef_[0]:+.1f} dk |
| Zirve saat ({'evet' if zirve_saat_mi else 'hayır'}) | {zirve_saat_mi * model.coef_[1]:+.1f} dk |
| Kalkış gecikmesi ({kalkis_gecikmesi:.0f} dk) | {kalkis_gecikmesi * model.coef_[2]:+.1f} dk |
"""


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
        "Model üç özellik kullanır: hava şiddeti, zirve saat bayrağı ve "
        "kalkış gecikmesi. Ham veri setindeki 44 özellikle eğitilen model "
        "ile aynı doğruluğu verir (MAE 5.77 → 5.75)."
    )

    btn.click(
        fn=tahmin_et,
        inputs=[hava_input, saat_input, gecikme_input],
        outputs=cikti,
    )


if __name__ == "__main__":
    demo.launch(inbrowser=True)
