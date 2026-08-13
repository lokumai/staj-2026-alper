# Week 4 – Mini-Project: TCDD Train Delay Prediction & Enterprise Data Pipeline

## 📖 Background & Context

In large national railway organizations like TCDD (*Türkiye Cumhuriyeti Devlet Demiryolları*), train arrival delays ripple across thousands of kilometers of track, impacting logistics, passenger satisfaction, and operating margins. Accurately predicting delays allows centralized dispatching teams to adjust schedules, optimize track bottlenecks, and notify passengers dynamically.

In previous weeks, you worked with clean, single-file educational datasets (like Iris or Diabetes) containing fewer than 500 rows and pre-selected features.

**In enterprise engineering projects, data is vastly larger, wider, and messier.** Data is stored across relational database dumps containing tens of thousands of records and dozens of administrative columns (staff IDs, equipment serial numbers, maintenance budget files) that have zero predictive value for ML. 

This week, you will take on the role of an ML Engineer at Intellica building a production-grade data processing and prediction pipeline on an enterprise dataset dump from TCDD.

---

## 🎯 Project Goal

Your goal is to build an **end-to-end machine learning pipeline** in a Jupyter Notebook ([`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb)) that:
1. Inspects and merges **3 large enterprise database tables** (~12,000 trip logs, 250 locomotives, 40 routes, 48 total columns) from [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data).
2. Performs a schema audit to drop administrative metadata noise and isolate true predictive signals.
3. Resolves real-world data quality issues (missing technical metrics, negative sensor values, corrupt error codes, mixed date strings, and station name variations).
4. Engineers domain features (temporal patterns, weather severity, technical wear factors).
5. Trains, tunes, and compares multiple ML models to predict arrival delays in minutes (`gecikme_suresi_dk`).

---

## 🗄️ Scenario & Data Overview

You are provided with 3 raw database dumps in [`projects/tcdd_data/`](file:///home/amirkia/Desktop/staj-2026-alper/projects/tcdd_data):

1. **`seferler_log.csv`** (12,000 trip records, 21 columns): Operational logs for train journeys across 2025–2026.
2. **`tren_bakim_gecmisi.csv`** (250 locomotives, 14 columns): Fleet specs, cumulative mileage, brake/wheel wear metrics, and maintenance logs.
3. **`hat_bilgileri.csv`** (40 railway routes, 13 columns): Infrastructure parameters, track types, elevation changes, bends, and speed limits.

### 💡 Hints for Your Data Investigation
* **Separate Signal from Administrative Noise:** Enterprise tables contain many non-predictive metadata fields (e.g., ticket scanner firmware versions, driver staff IDs, depot manager names, supplier codes, budget numbers). Audit all 48 columns and drop the noise.
* **Discover Relational Joins:** Find key identifier columns shared across `seferler_log`, `tren_bakim_gecmisi`, and `hat_bilgileri` to join them into a single consolidated dataset.
* **Audit Data Hygiene:** Scale creates more data anomalies. Look out for:
  * Missing (`NaN`) technical scores or environmental readings.
  * Invalid records or corrupt system error codes (e.g. negative values where impossible).
  * Inconsistent string casing and typos in weather and station names.
  * Mixed ISO (`YYYY-MM-DD`) and European (`DD.MM.YYYY`) date string formats.

---

## 🛠️ Project Phases & Workflow

### Phase 1: Schema Audit & Relational Joining (Day 1)
* Load all 3 CSV files into pandas DataFrames and inspect schemas (`info()`, `shape`, `head()`).
* Document which of the 48 columns are useful feature candidates vs. administrative noise.
* Discover primary/foreign keys and merge the 3 tables into a unified master DataFrame (12,000 rows).

### Phase 2: Data Cleaning & Preprocessing (Day 2)
* Check summary statistics (`describe()`, `isna().sum()`) across all numerical and categorical fields.
* Handle missing values (`NaN`) using appropriate imputation strategies.
* Clean corrupted system entries (e.g. invalid negative passenger counts or error codes).
* Parse date strings into datetime objects and resolve text/station string variations.

### Phase 3: Exploratory Data Analysis & Feature Engineering (Day 3)
* Engineer temporal features (departure hour, day of week, seasonal flags).
* Create physical domain ratios (e.g., estimated journey duration, wear-to-age ratios).
* Produce visualizations (correlation heatmaps, box plots, scatter plots) to uncover the top drivers of delay.

### Phase 4: Model Training, Selection & Fine-Tuning (Day 4)
* Split the dataset into 80% Training and 20% Testing sets.
* Train and compare **at least 3 different regression algorithms**:
  * **Linear Models:** e.g., `LinearRegression`, `Ridge`, or `Lasso`.
  * **Tree-Based Models:** e.g., `DecisionTreeRegressor`.
  * **Ensemble Models:** e.g., `RandomForestRegressor` or `GradientBoostingRegressor` / `HistGradientBoostingRegressor`.
* Tune key hyperparameters (`max_depth`, `n_estimators`, `learning_rate`) to prevent overfitting.
* Benchmark model performance using **MAE**, **RMSE**, and **$R^2$ Score**.

---

## 📋 Expected Deliverables

1. **Jupyter Notebook:** [`projects/w4_tcdd_delay_prediction.ipynb`](file:///home/amirkia/Desktop/staj-2026-alper/projects/w4_tcdd_delay_prediction.ipynb) with clean code, comments, and plots.
2. **Completed Internship Log:** Fill in your findings in the section below.

---

## 📝 Alper's Internship Log

### 1. Data Audit & Schema Joining

* **Out of 48 total columns across the 3 tables, which columns did you keep as
  features, which did you drop as administrative noise, and why?**
  * *Notes:* 48 sütunu üç kovaya ayırdım: anahtarlar, sinyal adayları ve idari
    gürültü. 18 sütunu attım:
    - **Yüksek kardinaliteli ID'ler:** `makinist_sicil_no` (6.590 benzersiz),
      `yardimci_makinist_sicil_no` (6.612), `sefer_id`, `depo_sorumlusu_adi`.
      Neredeyse her satırda farklı değer aldıkları için model bunları ezberler,
      test setinde hiç görmediği değerlerle karşılaşır.
    - **Tedarikçi/firma kodları ve firmware:** `temizlik_firmasi_kodu`,
      `yedek_parca_tedarikci_kodu`, `bilet_kontrol_cihaz_versiyonu`.
    - **Bütçe ve iletişim:** `son_bakim_maliyeti_tl`, `peron_yenileme_butcesi_tl`,
      `istasyon_muduru_telefon`.
    - **İkiz sütun:** `uretim_yili` ile `lokomotif_yasi` arasındaki korelasyon
      tam -1.0 çıktı; aynı bilginin iki hâli. `lokomotif_yasi`'nı tuttum çünkü
      doğrudan yorumlanabilir.
    - **Ölçülen ilişkisi olmayanlar:** `makinist_vardiya_saati`,
      `yemek_servisi_var_mi`, `vagon_klima_arizasi_bildirimi`, `hat_insaat_yili`,
      `garanti_durumu` — hepsinin hedefle korelasyonu |r| < 0.02.
    - **Gereksiz tekrar:** `kalkis_istasyonu`, `varis_istasyonu` — `hat_id` zaten
      aynı bilgiyi taşıyor (40 hat = 40 sabit rota).
    - **Temizlik sonrası elenenler:** `bolge_mudurlugu` ve `depo_kodu`'nu
      başlangıçta tutmuştum, ancak temiz veriyle grup ortalamaları yayılımı
      sırasıyla 0.6 ve 0.3 dakika çıkınca attım.

* **How did you join the 3 database tables?**
  * *Notes:* İki foreign key buldum: `tren_id` (seferler → tren_bakim_gecmisi)
    ve `hat_id` (seferler → hat_bilgileri). Anahtar adayını `nunique()` ile
    tespit ettim — bakım tablosunda 250, hat tablosunda 40 benzersiz değer,
    tablo satır sayılarıyla birebir örtüşüyor, yani ikisi de birer lookup tablosu.
    `seferler` sol tablo olacak şekilde iki kez `how='left'` merge yaptım.
    Merge öncesi üç doğrulama yaptım: (1) her iki sağ tabloda `duplicated()`
    kontrolü — duplike anahtar yok, (2) yetim kayıt kontrolü — `seferler`'deki
    tüm ID'lerin karşılığı mevcut, (3) merge sonrası satır sayısı kontrolü.
    Sonuç: 12.000 × 46, satır kaybı ve şişme yok.

---

### 2. Data Cleaning Discoveries

* **What data quality issues (outliers, formatting, missing data) did you
  discover in the 12,000 records, and how did you fix them?**
  * *Notes:*
    **1. Hedef değişkende sentinel değerler (en kritik bulgu).**
    `gecikme_suresi_dk` içinde 147 kayıt `-999` değerindeydi. Bunu
    `describe()` çıktısındaki üç anormallikten fark ettim: ortalama (13.6)
    medyandan (25.5) küçüktü, standart sapma (113.5) maksimum değeri (98.6)
    aşıyordu, min -999'du. Hedef değişkendeki bozuk kayıt doldurulamaz —
    modele uydurma cevap öğretmek olur — bu yüzden sildim (%1.2 kayıp,
    11.853 satır kaldı). Silmeden önce bozuk kayıtların kategorilere dağılımını
    kontrol ettim, rastgeleydi, yani bias yaratmıyor.

    **Bu bulgunun etkisi:** temizlik öncesi hesapladığım kategorik grup
    ortalamaları tamamen yanıltıcıymış. `hat_tipi` yayılımı kirli veride
    10.5 dakika görünüyordu, temiz veride 0.6 dakikaya düştü. 147 bozuk kayıt
    (%1.2) tüm EDA sonuçlarını tersine çevirmişti.

    **2. Karışık tarih formatları.** 1.382 kayıt DD.MM.YYYY, 10.471 kayıt
    ISO formatındaydı. `pd.to_datetime`'ı düz çağırmak yerine regex ile
    formatları ayırıp her birini kendi formatıyla parse ettim, çünkü
    `06.08.2025` hem 6 Ağustos hem 8 Haziran olarak okunabilir ve pandas bunu
    sessizce yanlış yapabilir. Parse sonrası üç doğrulama: tarih aralığı
    (2025-01-01 → 2026-08-07, gelecek tarih yok), varış < kalkış olan satır
    sayısı (0), yolculuk süresi dağılımı (60–510 dk, makul). Hiçbir kayıt
    parse edilemez kalmadı.

    **3. Geçersiz negatif değerler — ama hepsi değil.** `yolcu_sayisi`'nda 239
    negatif kayıt vardı (min -40); bunları 0 yerine NaN'a çevirdim, çünkü
    -40 "kimse binmedi" değil "sistem hatalı kaydetti" demek.
    `ortam_sicakligi_c`'de de 2.369 negatif değer vardı ama bunlar meşru —
    Türkiye'de kış sıcaklıkları eksiye düşer. Negatif değerleri körü körüne
    temizlemek 2.369 geçerli kaydı bozardı.

    **4. String tutarsızlıkları.** `hava_durumu`'nda `Sisli`/`sisli` ve
    `Yagmurlu`/`yagmurlu` ayrı kategoriler olarak sayılıyordu;
    `.str.strip().str.lower()` ile 7 kategori 5'e indi. İstasyon isimlerinde
    hem "Ek-N" son ekleri hem yazım varyasyonları vardı (`Ankara Gar`,
    `ANKARA`, `ank-gar`); regex + eşleme sözlüğüyle 40 ismi 17'ye indirdim.
    Bu temizliği 11.853 satırlık master tablo yerine 40 satırlık kaynak
    tabloda yaptım.

    **5. Eksik değerler — üç sütun, iki farklı strateji.** Doldurmadan önce
    her sütun için "eksik olanların ortalama gecikmesi" ile "dolu olanların
    ortalama gecikmesi"ni karşılaştırdım:
    - `yolcu_sayisi` (898 eksik) ve `motor_saglik_skoru` (1.493): fark 0.3 ve
      0.1 dakika, yani eksiklik rastgele. Medyanla doldurdum (ortalama yerine
      medyan, çünkü aykırı değerlerden etkilenmiyor) ve birer `_eksikti`
      bayrak sütunu ekledim.
    - `hava_durumu` (1.515 eksik): eksik olanların ortalaması 14.0 dk, dolu
      olanların 27.9 dk — **13.9 dakikalık fark.** Bu, eksikliğin kendisinin
      bilgi taşıdığı anlamına geliyor. Farkın hat tipinden kaynaklanıp
      kaynaklanmadığını test ettim; dört hat tipinin dördünde de fark ~14 dakika
      olarak sabit kaldı, yani bağımsız bir sinyal. Mod ile doldurmak yerine
      `"bilinmiyor"` adında ayrı bir kategori olarak bıraktım. Sonradan bu
      kategorinin ortalamasının (14.0) `acik` ile (14.1) neredeyse birebir aynı
      olduğunu gördüm — hava kaydı muhtemelen sadece olumsuz koşullarda
      giriliyor. Mod (`sisli`) ile doldursaydım 1.515 açık hava seferini yanlış
      etiketleyip modele 20 dakikalık hata öğretecektim.

    **6. Fiziksel olarak imkânsız türev değerler.** Türettiğim
    `ortalama_hiz_kmh` sütununda maksimum 534 km/s çıktı ve
    `hiz_kullanim_orani` 2.83'e (hat limitinin 2.8 katı) ulaştı. Bu,
    `mesafe_km` ile planlanan süre arasında tutarsızlık olduğunu gösteriyor.
    Bu özelliklerin hedefle korelasyonu sıfır olduğu için modele zarar
    vermediler, ancak veri kalitesi açısından not edilmesi gereken bir bulgu.

---

### 3. Feature Engineering & Key EDA Findings

* **What new features did you engineer?**
  * *Notes:* 15 yeni özellik türettim:
    - **Zamansal:** `kalkis_saati`, `haftanin_gunu`, `ay`, `mevsim`,
      `hafta_sonu_mu`, `zirve_saat_mi` (07–09 ve 17–19), `gece_seferi_mi`
    - **Hava şiddeti:** `hava_siddeti` — kategorik hava durumunu sıralı sayısal
      skora çevirdim (acik/bilinmiyor=0, yagmurlu=1, sisli/firtinali/karli=2).
      Bu gruplamayı box plot'a dayandırdım: sisli, fırtınalı ve karlı
      dağılımları birbirinden ayırt edilemiyordu (üçünün de medyanı ~33 dk),
      acik ile bilinmiyor da aynıydı. Yani veride 6 değil 3 seviye var.
    - **Fiziksel oranlar:** `planlanan_sure_dk`, `ortalama_hiz_kmh`,
      `hiz_kullanim_orani`, `km_basina_viraj`, `km_basina_gecit`, `yillik_km`,
      `asinma_yas_orani`

    **En değerli türetme `zirve_saat_mi` oldu.** Ham `kalkis_saati`'nin hedefle
    korelasyonu sadece 0.062'ydi ve bu sütunu elemeye meyilliydim. Ancak
    `qcut` ile binleyip grup ortalamalarına bakınca çift tepeli bir örüntü
    çıktı: 07–09 arası 30.3 dk, 17–19 arası 30.9 dk, diğer tüm saatler ~23 dk.
    İlişki doğrusal olmadığı için korelasyon bunu göremiyordu. İkili bayrağa
    çevirince korelasyon 0.062'den **0.401'e** çıktı — altı kat.

    Buradan çıkardığım ders: korelasyonun sıfır olması ilişki olmadığı anlamına
    gelmiyor, sadece doğrusal ilişki olmadığı anlamına geliyor.

    Fiziksel oran özelliklerinin hiçbiri sinyal vermedi (hepsi |r| < 0.02).

* **What are the top factors that cause train delays based on your EDA?**
  * *Notes:*
    | Özellik | Katsayı × std | RF önem | Etki |
    |---|---|---|---|
    | `hava_siddeti` | 8.63 | 62.7% | Kötü hava ~+20 dk |
    | `zirve_saat_mi` | 5.23 | 22.8% | Zirve saat ~+12 dk |
    | `fiili_kalkis_gecikmesi_dk` | 2.98 | 7.8% | Kalkış gecikmesinin %74'ü varışa taşınıyor |

    Bu üç özellik açıklanan varyansın %93'ünü taşıyor. Sıralamayı iki bağımsız
    yöntemle doğruladım: lineer modelin standartlaştırılmış katsayıları ve
    Random Forest özellik önemleri aynı sonucu verdi.

    **Etkiler toplamsal, çarpımsal değil.** Hava şiddeti × zirve saat
    etkileşim grafiğinde zirve saatin etkisi üç hava seviyesinde de sabit
    ~12 dakika çıktı (iyi havada 11→23, yağmurluda 19→31, kötüde 31→43).
    Yani gecikme yapısı kabaca: `taban + (hava_siddeti × 10) + (zirve × 12)`.
    Bu gözlem, hangi modelin kazanacağını önceden tahmin etmemi sağladı.

    **Beklediğim ama çıkmayan sinyaller:** Lokomotif yaşı, aşınma metrikleri
    (fren balatası, tekerlek profili), toplam kilometre, motor sağlık skoru,
    hat zorluk indeksi, viraj sayısı, mesafe — hiçbirinin hedefle anlamlı
    ilişkisi yok (|r| < 0.02). Binleme testiyle doğrusal olmayan ilişki
    ihtimalini de kontrol ettim, dilimler arası fark çıkmadı. Alan bilgisi
    eskimiş ve yıpranmış araçların daha çok gecikeceğini düşündürüyordu, ancak
    veri bunu desteklemedi.

    **Mevsim etkisiz (yayılım 0.7 dk).** Bu tuhaf: hava durumu en güçlü sürücü
    olduğuna göre karlı seferlerin kışta yoğunlaşması ve kış ortalamasının
    yükselmesi beklenirdi. Anlamı, veri setinde hava durumunun mevsimden
    bağımsız atanmış olması.

    Eklediğim `_eksikti` bayrakları modelde neredeyse hiç ağırlık almadı
    (RF önemi %0.4), bu da `yolcu_sayisi` ve `motor_saglik_skoru`'ndaki
    eksikliğin gerçekten rastgele olduğunu doğruladı.

---

### 4. Model Benchmark Comparison

| Model Name | Key Hyperparameters | Test MAE (min) | Test RMSE (min) | Test $R^2$ |
|---|---|---|---|---|
| Linear Regression | Default | 5.77 | 7.68 | 0.641 |
| Decision Tree | max_depth=4 | 5.88 | 7.81 | 0.629 |
| Decision Tree (ayarsız) | Default | 8.63 | 12.13 | 0.106 |
| Random Forest | n_estimators=200, max_depth=8, min_samples_leaf=20 | 5.79 | 7.70 | 0.639 |
| HistGradientBoosting | max_iter=200, learning_rate=0.1, max_depth=6 | 5.91 | 7.88 | 0.623 |

*Naif baseline (tüm tahminler = medyan): MAE 10.47 dk*

* **Which model performed best, and why?**
  * *Notes:* **Linear Regression** kazandı (MAE 5.77, R² 0.641), ancak ayarlı
    modellerin hepsi 5.8–5.9 MAE bandında yakınsadı. Tüm modeller baseline'ı
    yaklaşık %45 iyileştirdi.

    **Neden lineer model:** EDA'da etkilerin toplamsal olduğunu görmüştüm.
    Ensemble modellerin asıl avantajı doğrusal olmayan etkileşimleri
    yakalamaktır; bu veride yakalanacak etkileşim yok. Ağaç tabanlı modeller
    sürekli değişkenleri basamaklara böldüğü için hafif hassasiyet kaybediyor.
    Yani en karmaşık model değil, veri yapısına en uygun model kazandı.

    Lineer modelin katsayıları EDA'daki tahminimi doğruladı:
    `zirve_saat_mi` = 12.08, `hava_siddeti` = 10.31. Grafiklerden çıkardığım
    "taban + hava×10 + zirve×12" formülünü model bağımsız olarak onayladı.

    **Overfitting gözlemi:** Ayarsız karar ağacı eğitim setini birebir
    ezberledi — Train MAE 0.000, Train R² 1.000 — ama Test R² sadece 0.106.
    `max_depth` taraması klasik U eğrisi verdi: derinlik arttıkça train skoru
    sürekli yükseliyor (0.602 → 1.000) ama test skoru 4'te tepe yapıp düşüyor.
    `max_depth=4` ile Test R² 0.629'a çıktı, yani altı kat iyileşme.
    Random Forest'ta da benzer bir makas vardı (Train R² 0.945 vs Test 0.608);
    `max_depth=8` ve `min_samples_leaf=20` ile MAE 6.13'ten 5.79'a indi.

    **Modelin tavanı:** R² 0.641, yani varyansın %36'sı açıklanamıyor. Artık
    analizi bu kalıntının sistematik değil rastgele olduğunu gösterdi — model
    üç hava seviyesinde de neredeyse eşit hata yapıyor (5.61 / 6.04 / 5.71 dk).
    Artıkların sağa çarpık olması ise gecikmenin doğasından kaynaklanıyor:
    alt sınır 0 dakika, üst sınır yok. Bu tavan modelin yetersizliğinden değil,
    veride bulunmayan bilgiden kaynaklanıyor.
### 5. Final Reflection & Questions

* Bu hafta en çok öğrendiğim şey, temizlik yapmadan EDA'ya girmenin insanı
  yanlış sonuca götürdüğü oldu. 12.000 kayıtta sadece 147 tanesi bozuktu ama
  bütün grup ortalamalarımı tersine çevirmişti. Eğer describe() çıktısında
  ortalamanın medyandan küçük olmasını fark etmeseydim, tamamen yanlış
  bulgularla devam edecektim.

* Beklemediğim bir sonuç, en basit modelin kazanması oldu. Random Forest'ın
  daha iyi çıkacağını düşünüyordum ama veri yapısı toplamsal olduğu için
  lineer regresyon yeterli geldi. "Daha karmaşık model daha iyi sonuç verir"
  varsayımının her zaman geçerli olmadığını gördüm.

* Zaman olarak Faz 1 ve 2 tahmin ettiğimden çok daha uzun sürdü, Faz 4 ise
  beklediğimden kısa sürdü. Asıl iş modelde değil veriyi anlamakta geçiyormuş.

**Sorularım:**
* Gerçek bir projede R² 0.64 kabul edilebilir bir seviye mi, yoksa daha fazla
  veri kaynağı toplamaya mı gidilir?
* Bir sonraki adım olarak cross-validation ve daha geniş hiperparametre
  taraması yapmayı düşünüyorum küçük bir arayüz de işimi görebilir. Sizce öncelik vermem gereken başka bir şey var mı? 
