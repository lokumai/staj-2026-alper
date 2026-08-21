# TCDD Sefer Gecikme Tahmini — Demo Arayüzü

Intellica yaz stajı (2026) kapsamında geliştirilen tren gecikme tahmin modelinin
canlı demo arayüzü. Model, TCDD sefer loglarıyla eğitilmiş bir doğrusal
regresyon modelidir; arayüz Gradio ile yazılmıştır.

## Çalıştırma

```bash
pip install -r requirements.txt
python app.py
```

Uygulama `http://127.0.0.1:7860` adresinde açılır.

## Model

11.853 temizlenmiş sefer kaydı üzerinde eğitildi. Hedef değişken varış
gecikmesidir (`gecikme_suresi_dk`, dakika cinsinden).

| Model | Test MAE | Test RMSE | Test R² |
|---|---|---|---|
| Naif baseline (medyan) | 10.47 | — | — |
| **Doğrusal regresyon (3 özellik)** | **5.75** | 7.68 | **0.643** |
| Doğrusal regresyon (44 özellik) | 5.77 | 7.68 | 0.641 |
| Random Forest (ayarlı) | 5.79 | 7.70 | 0.639 |
| HistGradientBoosting | 5.91 | 7.88 | 0.623 |

## Öğrenilen ilişki

Model, gecikmeyi toplamsal bir yapı olarak öğrendi:

```
gecikme ≈ 7.4 + 10.3 × hava_şiddeti + 12.1 × zirve_saat + 0.74 × kalkış_gecikmesi
```

| Özellik | Tanım |
|---|---|
| `hava_siddeti` | 0 = açık/bilinmiyor, 1 = yağmurlu, 2 = sisli/fırtınalı/karlı |
| `zirve_saat_mi` | Kalkış 07:00–09:00 veya 17:00–19:00 aralığındaysa 1 |
| `fiili_kalkis_gecikmesi_dk` | Kalkış anında ölçülen gecikme |

## Bulgular

**Üç özellik 44 özellik kadar iyi.** Ham veri setindeki 44 özelliğin taşıdığı
sinyalin tamamı üç özellikte toplanmış durumda; gereksiz sütunlar atılınca test
performansı düşmedi, hatta hafifçe iyileşti.

**Doğrusal model ensemble'ı geçti.** EDA aşamasında hava durumu ile zirve saat
etkilerinin çarpımsal değil toplamsal olduğu görülmüştü — yakalanacak doğrusal
olmayan etkileşim bulunmadığı için ağaç tabanlı modellerin avantajı oluşmadı.

**Korelasyon tek başına yanıltıcı.** `gece_seferi_mi` özelliğinin hedefle
korelasyonu −0.177 iken, modele `zirve_saat_mi` eklendiğinde katsayısı −0.09'a
düştü. Gece seferleri tanımı gereği zirve saat dışında olduğundan, iki özellik
aynı bilgiyi taşıyordu.

**Eksik veri de bilgidir.** `hava_durumu` sütunu boş olan seferlerin ortalama
gecikmesi 14.0 dk, dolu olanların 27.9 dk. Hava kaydı anlaşılan yalnızca
olumsuz koşullarda giriliyor. Bu yüzden eksik değerler mod ile değil, ayrı bir
"bilinmiyor" kategorisi olarak dolduruldu.

## Kapsam ve sınırlar

Model **kalkış anında** çalışacak şekilde tasarlandı: üç girdinin de tren
perondan ayrılırken bilinmesi gerekir. Sefer öncesi tahmin için
`fiili_kalkis_gecikmesi_dk` özelliği kullanılamaz.

R² 0.643, varyansın yaklaşık üçte birinin açıklanamadığı anlamına gelir. Artık
analizi bu kalıntının sistematik değil rastgele olduğunu gösterdi; hata tüm hava
koşullarında benzer düzeydedir (5.6–6.0 dk).

## Dosyalar

| Dosya | İçerik |
|---|---|
| `app.py` | Gradio arayüzü |
| `tcdd_demo_model.pkl` | Eğitilmiş model ve özellik listesi |
| `w4_tcdd_delay_prediction.ipynb` | Veri temizleme, EDA ve model eğitimi |
