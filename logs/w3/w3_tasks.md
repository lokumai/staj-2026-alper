# Week 3 – Jupyter, Colab, and the ML Working Style

## Goal

Before touching real TCDD data next week, get comfortable with the *environment*
ML engineers and Data Scientists actually work in day-to-day, then **build one
notebook per Week 2 algorithm yourself**, from scratch, in Colab. Nobody is
handing you working code this week — you're given a task and a dataset, and you
write the notebook. Use your AI coding agent (Claude/Copilot) whenever you get
stuck on syntax or an error message — that's expected and encouraged, the same way
it was in Week 1. The goal is that *you* understand and can explain what the
notebook does and why the result looks the way it does, not that you memorize
scikit-learn syntax.

No exploratory data analysis, no data cleaning, no hyperparameter tuning this week
— that's deliberate, and saved for Week 4 on real data. Every dataset below is a
famous, education-ready one (Iris, Diabetes — both originally from the UCI Machine
Learning Repository — plus one synthetic dataset made for teaching clustering),
built directly into scikit-learn, so there's zero friction between "start a new
notebook" and "see the algorithm work."

## Schedule

| Session | Format | Focus |
|---|---|---|
| Day 1 | Self-study | What is Jupyter / Colab, and why ML work looks different from software engineering |
| Day 2 | Build | Classification tasks: Naive Bayes, KNN |
| Day 3 | Build | Regression tasks: Linear Regression, Decision Tree |
| Day 4 | Build | Clustering task: K-Means + write up observations |
| Day 5 | Meeting | Walk through all 5 notebooks together, preview Week 4 (real TCDD EDA) |

## Day 1 — Jupyter, Colab, and how ML work differs from software engineering

### What is a Jupyter Notebook, and why does ML use it?
A notebook is a document made of **cells** — some are code, some are text (markdown)
— that you run one at a time, in any order you like, and the output (a number, a
table, a plot) appears right below the cell that produced it.

That's the whole reason it exists: ML and data work is fundamentally **iterative and
exploratory**. You load some data, look at it, try something, look at the result,
change one thing, look again. A notebook lets you keep all your intermediate
results (data previews, charts, model scores) visible on the same page as the code
that made them, instead of re-running an entire program from scratch every time you
change one line — which is how you'd normally work as a software engineer.

### What is Google Colab?
Colab is Google's free, hosted Jupyter environment — it runs in your browser, needs
zero local setup (no Python install, no virtual environments), comes with the
common ML libraries (including scikit-learn and matplotlib) already installed, and
even gives free (limited) GPU access. To start, go to colab.new (or Google Drive →
New → More → Google Colaboratory) — that gives you a blank notebook you can start
writing in immediately.

### How does ML/DS working style differ from software engineering?
Worth internalizing this early, since it explains *why* the tools and habits differ:

- **Exploration vs. construction.** A software engineer usually starts from a fairly
  clear spec and builds toward it. An ML engineer / data scientist often starts by
  not knowing what the data even looks like, and the first hour of work is just
  looking — that's what notebooks are built for.
- **Cells vs. programs.** Notebook code runs cell-by-cell, out of order, with state
  hanging around in memory between runs. This is great for exploration and terrible
  for the reliability guarantees software engineering usually wants (reproducibility,
  "run this from a clean state and get the same result").
- **Evaluation by metric, not pass/fail.** A unit test either passes or fails. A
  model doesn't — you get an accuracy or an error number and have to judge whether
  it's *good enough*, which is a judgment call, not a boolean.
- **Notebooks are for prototyping, not production.** Once an approach is validated
  in a notebook, it usually gets rewritten into proper scripts/pipelines (real
  functions, tests, version control that actually diffs cleanly) before it runs in
  production. Notebooks themselves diff terribly in git — that's a real, known pain
  point, not a limitation you're missing something about.

### Self-check (write in your log)
- In your own words: why does a notebook fit exploratory data work better than a
  regular script would?
- What's one thing about the notebook workflow that would worry you if this code
  were going straight to production?

## Day 2 — Classification tasks

Make one notebook per algorithm. For both, use the **Iris dataset** — a famous
flower-measurement dataset built into scikit-learn (`sklearn.datasets.load_iris`),
where the goal is predicting the species from 4 measurements. Use the same dataset
for both so you can compare your two results directly.

**Before you train anything, play with the raw data first.** Try a few different
plots: a scatter plot of two features colored by species, a histogram of a single
feature, a scatter plot of a *different* pair of features. Do the species look
visually separable before you've trained anything? This habit — looking at the
data from a few angles before modeling — is worth building now, and it also gives
you something to sanity-check your model's results against later.

**Task A — Naive Bayes**
1. Load the Iris dataset and split it into training and test sets.
2. Train a Naive Bayes classifier (`sklearn.naive_bayes.GaussianNB`) on the training set.
3. Predict on the test set and report accuracy.
4. Look at `predict_proba` for a few test examples — what do the actual probabilities behind a prediction look like?

**Task B — KNN**
1. Same dataset, same train/test split approach.
2. Train a KNN classifier (`sklearn.neighbors.KNeighborsClassifier`).
3. Try at least 3 different values of `k` and report accuracy for each.
4. Write down: which `k` did best, and what's your theory for why?

## Day 3 — Regression tasks

Make one notebook per algorithm. For both, use the **Diabetes dataset**
(`sklearn.datasets.load_diabetes`) and, to keep things plottable, pick just **one**
feature (e.g. BMI) as your input rather than all of them.

**Before you train anything, play with the raw data first.** Try plotting your
chosen feature against the target as a plain scatter plot, then try a different
feature and see if the relationship looks tighter or looser. A histogram of the
target itself is also worth a look — is it roughly symmetric, skewed, anything
unexpected? Whichever feature ends up looking most related to the target is a
reasonable one to model with.

**Task C — Linear Regression**
1. Load the data, pick one feature, split into train/test.
2. Train a `LinearRegression` model.
3. Report R² and plot your predictions against the actual test points (a scatter plot of the real points plus your fitted line).

**Task D — Decision Tree**
1. Same feature, same dataset, same split.
2. Train a `DecisionTreeRegressor` — try capping `max_depth` at a small number first.
3. Plot your predictions the same way you did for linear regression.
4. Compare the *shape* of your two plots — what's different about how the tree fits the data versus the straight line? What happens to the shape if you remove the `max_depth` cap?

## Day 4 — Clustering task + wrap-up

**Task E — K-Means**
1. Generate a synthetic dataset with `sklearn.datasets.make_blobs` (this is a well-known synthetic dataset made specifically for teaching clustering — pick however many centers you like).
2. Plot the raw points *before* running anything — with no labels, no colors, just the points. What do you see with your own eyes? How many groups would you guess, just by looking?
3. Run `KMeans` on it and plot the result, coloring points by their assigned cluster, with the cluster centers marked. Compare this to your guess in step 2.
4. Now deliberately set `n_clusters` in `KMeans` to the *wrong* number (not matching how many blobs you generated) and re-run, plotting the result again. What does it do? Is there a "right" way for K-Means to tell you it got the wrong number?

## General note: play with it beyond what's asked

Every task above lists a minimum. Beyond that, experiment freely — try other plot
types (box plots, pair plots of multiple features at once, 3D scatter plots), swap
in a different feature than the one suggested, change `test_size`, try more values
of `k` or `max_depth` than asked. None of this needs to make it into your final
notebook — the point is building a feel for how these things behave by poking at
them, not just completing a checklist.

In your log, write a few sentences per task: what you built, what you had to ask
your AI agent for help with, what you noticed in the comparisons above, and
anything interesting you found while experimenting beyond the minimum ask.

## Day 5 — Wrap-up meeting

Walk through observations from all 5 notebooks together, answer open questions, and
preview Week 4 — his first real task on the actual TCDD project (EDA on real data).

---

## Alper's Log
## Alper's Log

### Day 1 — Jupyter, Colab ve ML çalışma tarzı

**Self-check 1: Notebook neden keşifsel veri işine script'ten daha uygun?**
Kodu hücrelere bölüp adım adım çalıştırabildiğim için veriyi parça parça
inceleyip her adımda çıktıyı görebiliyorum. Grafikler ve tablolar anında
hücrenin altında göründüğü için gözlem–yorum–deneme döngüsü çok hızlı
ilerliyor. Markdown hücreleriyle kod ve açıklamayı aynı yerde tutabiliyorum.
Script'te tek bir satırı değiştirmek için her şeyi baştan çalıştırmak gerekirdi.

**Self-check 2: Bu kod üretime gitse ne endişelendirirdi?**
Gizli durum (hidden state) ve tekrarlanabilirlik. Hücreleri istediğim sırada
çalıştırabildiğim için ekranda okuduğum kod ile gerçekte çalışmış olan sıra
farklı olabiliyor. Değişkenler bellekte asılı kaldığından, bende çalışan bir
notebook sıfırdan çalıştırıldığında aynı sonucu vermeyebilir. Üretimde en
temel beklenti "temiz başlangıçtan çalıştır, aynı sonucu al" — notebook bunu
yapısı gereği garanti etmiyor. Bu yüzden her notebook'u paylaşmadan önce
Restart & Run All yaptım.

### Task A — Naive Bayes (Iris)

Modellemeden önce scatter plot ve histogram çizdim. Petal ölçümleri türleri
sepal ölçümlerinden çok daha net ayırıyor: setosa tamamen kopuk bir küme,
versicolor ve virginica ise sınırda birbirine değiyor.

GaussianNB ile accuracy %97.8 çıktı (45 test örneğinden 44 doğru). Confusion
matrix, tek hatanın tam da grafikte beklediğim yerde olduğunu gösterdi: bir
versicolor, virginica sanılmış. Setosa'da hiç hata yok.

En çok predict_proba çıktısı ilgimi çekti. Model her tahminde aynı derecede
emin değil: setosa tahminlerinde olasılık tam 1.0 iken, sınıra yakın bir
versicolor örneğinde 0.83'e karşı 0.17 çıktı. Accuracy bu farkı gizliyor —
doğru/yanlış diyor ama modelin ne kadar emin olduğunu söylemiyor.

### Task B — KNN (Iris)

Task A ile aynı split'i (random_state=42) bilerek kullandım ki iki model
doğrudan karşılaştırılabilsin.

k = 1, 3, 5, 11, 25 için accuracy %100; k = 51'de %95.6'ya düştü. Sebebi:
eğitim setinde her türden yaklaşık 35 örnek var, dolayısıyla k=51 dediğimde
en yakın 35'i doğru türden gelse bile kalan 16'sı zorunlu olarak başka
türlerden geliyor. Oylama hiçbir zaman saf olamıyor.

Asgari ödevin ötesine geçip k'ya karşı accuracy grafiği çizdim. Grafikteki
basamakların tek tek çiçeklere denk geldiğini fark ettim: test setinde 45
örnek var, yani bir çiçek = 1/45 = 0.0222 ve tüm değerler bunun katı. Bu da
KNN ile Naive Bayes arasındaki 0.02'lik farkın aslında "bir çiçek" demek
olduğunu gösteriyor — bu kadar küçük bir test setinde o farka anlam
yüklememek gerekiyor.

Bir de ölçekleme deneyi yaptım ve beklediğimin TERSİ çıktı: StandardScaler
sonrası accuracy düştü (k=51'de 0.9556'dan 0.8444'e). Sebebini araştırınca
anladım — Iris'te özellikler eşit derecede faydalı değil. Petal ölçümleri
türleri net ayırıyor, sepal ölçümleri karışık. Ham veride petal'in aralığı
daha geniş olduğu için mesafe hesabında zaten ağır basıyordu ve bu tesadüfen
doğru olanı yapıyordu. Ölçekleyince gürültülü olan sepal'i petal ile eşitlemiş
oldum. Çıkarım: ölçekleme özelliklerin ÖLÇEK farkını kaldırır, ÖNEM farkını
değil. Farklı birimlerdeki özelliklerde zorunlu, ama Iris'te dördü de aynı
birimde olduğu için düzeltilecek bir bozukluk yoktu.

### Task C — Linear Regression (Diabetes, bmi)

Hedefin histogramı sağa çarpık: yığılma 50-150 arasında, 350'ye kadar uzanan
bir kuyruk var. Üç özelliği (bmi, s5, age) hedefe karşı çizdim; age'de
noktalar tamamen bulut gibiydi, bmi'da yukarı yönlü bir eğilim vardı. bmi ile
modelledim.

R² = 0.2803. BMI tek başına hedefteki değişkenliğin yaklaşık dörtte birini
açıklıyor. Grafikte de eğilim gevşekti — aynı bmi değerinde target 50 de
olabiliyordu 300 de — yani sayı gözümün gördüğünü doğruladı.

İki katsayı da öğreticiydi. Kesişim 151.04, neredeyse hedefin ortalaması
(152.1); sebebi özelliklerin ortalaması 0 olacak şekilde normalize edilmiş
olması. Eğim 988 devasa görünüyor ama bmi normalize edilmiş, tüm aralığı
-0.09 ile 0.17 arası; gerçek anlamı en düşük bmi'dan en yükseğine giderken
tahminin ~257 puan artması. Katsayıyı yorumlayabilmek özelliğin biriminin
anlamlı olmasına bağlıymış.

### Task D — Decision Tree (Diabetes, bmi)

Aynı veri, aynı özellik, aynı split. max_depth=3 ile R² = 0.2781 çıktı —
Task C'deki 0.2803 ile pratikte aynı. İki tamamen farklı algoritma aynı
sonucu verdi çünkü bmi ile target arasındaki ilişki zaten kabaca doğrusal;
ağacın esnekliği burada fazladan bir şey kazandırmıyor.

Skorlar aynı ama şekil çok farklı: linear regression düz bir çizgi, ağaç ise
merdiven şeklinde basamaklar üretiyor. Ağaç bmi aralığını bölgelere ayırıp her
bölgedeki tüm hastalara tek bir sayı (o yaprağın ortalaması) veriyor. Bölge
içinde tahmin sabit, sınırı geçince aniden zıplıyor. İki uçtaki basamaklar da
yatay uzuyor — ağaç gördüğü aralığın dışına çıkamıyor.

max_depth'i artırdıkça train ve test R² ters yönlere gitti:
- depth=2 → train 0.3926 / test 0.2748
- depth=3 → train 0.4116 / test 0.2781
- depth=5 → train 0.4659 / test 0.2427
- sınırsız → train 0.6300 / test 0.1187

Bu tam olarak overfitting. Sınırsız ağaç eğitim verisini iki kat daha iyi
"biliyor" ama yeni veride linear regression'ın yarısı kadar işe yarıyor.
Grafiği de dişli ve titrek bir çizgi — bir örüntü değil, gürültünün
ezberlenmiş hali. En çarpıcı bulgu: modeli frenlemek onu güçlendirdi,
max_depth=2 bile sınırsız ağacın iki katından iyi test skoru verdi.

### Task E — K-Means (make_blobs)

Ham noktalara renksiz baktığımda 4 grup net şekilde ayırt ediliyordu. K-Means
k=4 ile çalıştığında bulduğu gruplar ve merkezler gözle gördüğümle örtüştü.

Yanlış k verdiğimde algoritma hiç şikayet etmedi, hata vermedi, uyarmadı — ne
istediysem onu üretti. İki farklı bozulma şekli gördüm: k=2 ve 3'te aralarında
kocaman boşluk olan ayrı blob'ları birleştirdi; k=6 ve 8'de iki merkezi AYNI
blob'un içine yerleştirip homojen bir grubu keyfi olarak ortasından böldü.

Elbow grafiğinde ilk bakışta dirseği k=3 sandım. Sayılara bakınca yanıldığımı
gördüm: 3→4 geçişi hâlâ 1541 puan kazandırıyor ama 4'ten sonraki her adım
sadece ~72. 2→3 düşüşü çok büyük olduğu için (7320) grafiği eziyor ve sonraki
gerçek düşüşü görsel olarak küçük gösteriyor. Elbow'un zayıflığı tam da bu:
"dirsek nerede" gözle verilen öznel bir karar. Silhouette daha net konuştu,
tepe k=4'te (0.752), ama k=3 de çok yakın (0.735).

Sonuç: K-Means'in içeriden "yanlış sayı verdin" deme yolu yok. Elbow ve
silhouette dışarıdan bakan teşhis araçları ve ikisi de kesin cevap vermiyor.
Burada doğru cevabı biliyorum çünkü veriyi ben centers=4 ile ürettim — gerçek
bir projede o bilgi olmayacak.

### AI ajanı kullanımı

matplotlib subplots sözdizimi, np.linspace ile grid oluşturup ağacın
basamaklarını çizme, StandardScaler'da neden fit_transform sadece eğitim
setine uygulanır (data leakage), R² nasıl okunur, predict_proba çıktısını
yorumlama, feature names uyarısının sebebi.]

### Kafamı karıştıran 

- Ölçekleme deneyinin sonucu beklediğimin tersi çıktı. "KNN'de ölçekleme
  zorunludur" diye öğrenmiştim ama burada zarar verdi. Ölçek farkı ile önem
  farkı ayrımını doğru anladığımdan emin olmak isterim.
- Elbow grafiğini gözle yanlış okudum. Bu tür grafiklerde log ölçek kullanmak
  ya da düşüş farklarını ayrıca hesaplamak standart bir pratik mi?
- Notebook'ları git'e koyunca diff'lerin okunamaz olduğunu gördüm. Ekipte
  bunun için kullanılan bir araç var mı (nbstripout, jupytext gibi)?

### Not

Colab'ın GitHub entegrasyonunu kullanamadım: lokumai organizasyonu için
üçüncü taraf uygulama erişimi gerekiyor. Notebook'ları Colab'dan indirip
repoya elle ekledim.
