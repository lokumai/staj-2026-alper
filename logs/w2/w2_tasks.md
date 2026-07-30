# Week 2 – Machine Learning Fundamentals (Supervised & Unsupervised)

## Goal

This week is about **intuition, not implementation**. You do not need to write any
ML code, study the math, or learn a framework (scikit-learn, etc.) this week.

As an AI Engineer working in an agent-first world, the day-to-day skill is knowing
*which kind of algorithm fits a problem* and *how to judge whether a result makes
sense* — not deriving the math or hand-coding the algorithm. So for every algorithm
below, the goal is to be able to answer: what is it doing, when would I reach for
it, and when would it fail me?

## Schedule

| Session | Format | Focus |
|---|---|---|
| Day 1 | Self-study | Foundations: what is supervised vs. unsupervised learning |
| Day 2 | Self-study | Classification: Naive Bayes, KNN |
| Day 3 | Self-study | Regression: Linear Regression, Decision Trees |
| Day 4 | Self-study | Clustering: K-Means + comparison exercise + AI agent self-quiz |
| Day 5 | Meeting | Discuss answers, clarify confusion, preview Week 3 |

## Day 1 — Foundations: Supervised vs. Unsupervised Learning

Before any algorithm names, get this distinction rock solid — everything else this
week is just "which flavor of supervised or unsupervised is this."

### What is Machine Learning, in one line
Teaching a computer to find patterns in data instead of writing explicit rules by hand.

### Supervised Learning
- **Definition:** you have *labeled* data — every example comes with the "correct answer" (a label/target), and the algorithm learns to map inputs to that answer.
- **Two flavors, both covered this week:**
  - **Classification** — the answer is a category (e.g. spam / not spam)
  - **Regression** — the answer is a number (e.g. a price)
- **Example:** given past emails already marked spam / not spam, predict whether a new email is spam.

### Unsupervised Learning
- **Definition:** you have *unlabeled* data — no "correct answer" is given. The algorithm has to find structure or patterns in the data on its own.
- **The flavor covered this week: Clustering** — grouping data points together by similarity, with no predefined groups.
- **Example:** given customer purchase histories with no labels at all, group customers into segments that behave similarly.

### The core difference, in one sentence
**Supervised** = you're given the answers and want to predict new ones. **Unsupervised** = you're given no answers and want to discover structure.

### Resource
Google's Machine Learning Crash Course — the "Introduction to ML" section (developers.google.com/machine-learning) covers exactly this distinction in plain language with visuals. If you'd rather watch something, search "supervised vs unsupervised learning" — it's such a fundamental split that most well-rated explainer videos cover it well.

### Self-check (write your answers in your log)
- Is "predicting whether a transaction is fraud, using past examples already labeled fraud / not-fraud" supervised or unsupervised? Why?
- Is "grouping news articles by topic, when no topics are defined ahead of time" supervised or unsupervised? Why?
- Come up with one more real-world example of each, in your own words.

## Day 2 — Classification (Supervised)

### Naive Bayes
- **Intuition:** uses Bayes' theorem to estimate the probability of each class given the input features, assuming the features don't influence each other ("naive").
- **Reach for it when:** text/spam-style classification, you need a fast, cheap baseline, or you have limited data.
- **Watch out for:** the independence assumption is almost never really true — it still often works fine anyway, but it struggles when features are strongly correlated.
- **Resource:** StatQuest (Josh Starmer) — search "StatQuest Naive Bayes" on YouTube. Very clear, no heavy math, ~15 min.

### K-Nearest Neighbors (KNN)
- **Intuition:** to classify a new point, look at its `k` closest neighbors in the training data and take a majority vote. There's no real "training" step.
- **Reach for it when:** the decision boundary is irregular/non-linear and you want something simple and interpretable on small-to-medium datasets.
- **Watch out for:** gets slow and unreliable as data size and number of features grow (curse of dimensionality); sensitive to feature scaling.
- **Interactive:** Stanford's CS231n kNN demo — search "cs231n knn demo". You place points on a 2D plane, change `k`, and watch the decision regions change live. Best way to build real intuition for this one.

## Day 3 — Regression (Supervised)

### Linear Regression
- **Intuition:** fits the straight line (or plane) through the data that minimizes prediction error.
- **Reach for it when:** you need a fast, interpretable baseline for predicting a number, and the relationship looks roughly linear. The coefficients directly tell you "how much does the prediction change per unit of this feature."
- **Watch out for:** can't capture curved/non-linear relationships, and is sensitive to outliers.
- **Resource:** StatQuest — search "StatQuest Linear Regression".

### Decision Trees
- **Intuition:** repeatedly splits the data with yes/no questions on features, aiming for purer and purer groups at each split.
- **Reach for it when:** you want something interpretable (you can literally read the tree as a set of rules), and your data mixes feature types or has non-linear relationships.
- **Watch out for:** left to grow freely, they overfit — memorize the training data instead of generalizing.
- **Interactive:** r2d3.us — "A Visual Introduction to Machine Learning" (Part 1 and Part 2). A scroll-through visual explainer that builds a decision tree in front of you and shows overfitting happening. One of the best ML-intuition resources on the web, genuinely worth the full read for both parts.

## Day 4 — Clustering (Unsupervised) + Comparison Exercise

### K-Means
- **Intuition:** given a chosen number of groups `k`, repeatedly (1) assign each point to its nearest center, (2) recompute each center as the average of its assigned points, until things stop changing.
- **Reach for it when:** you don't have labels and want to discover natural groupings — e.g. customer segmentation, grouping similar log entries.
- **Watch out for:** you have to choose `k` yourself, it assumes roughly round/blob-shaped clusters, and the result depends on where the centers start out.
- **Interactive:** naftaliharris.com/blog/visualizing-k-means-clustering — drop your own points on a canvas and step through the algorithm one iteration at a time. Excellent for seeing exactly why initialization matters.

### Comparison exercise + use your AI agent

Use the AI agent skills from Week 1 here — this *is* the exercise, not a shortcut around it.
Ask Claude/Copilot things like:
- "Explain [algorithm] to me like I'm new to ML, with a real-world example."
- "Give me 3 situations where you'd pick KNN over Naive Bayes, and 3 where you'd pick the opposite."
- "Quiz me with 3 questions on the difference between linear regression and decision trees."

Then, in your own words (no need for code, a few sentences is enough), answer in your log:
1. KNN vs. Naive Bayes for classification — when would you pick one over the other?
2. Linear Regression vs. Decision Tree for regression — when does each one fail?
3. Given a brand-new dataset with no labels, how would you decide whether clustering is even the right approach?

## Day 5 — Wrap-up meeting

Walk through your answers together, clear up anything confusing, and preview Week 3
(a small project that puts these ideas into practice).

---

## Alper's Log

**Day 1 — Supervised vs Unsupervised**
Temel ayrımı oturttum: supervised'da veri etiketli, cevapları biliyorum ve
yenilerini tahmin ediyorum; unsupervised'da etiket yok, yapıyı keşfediyorum.
Google ML Crash Course'un "Introduction to ML" bölümünü çalıştım ve konuyla
ilgili video izledim.

Kendi örneklerim:
- Supervised: Futbol antrenmanlarımdaki hız kayıtları + "sakatlandım /
  sakatlanmadım" bilgisi → yeni bir antrenman için sakatlanma tahmini.
- Unsupervised: Bir sürü futbolcunun istatistikleri var ama hiçbiri "şu tip
  oyuncu" diye etiketlenmemiş → istatistiklerine göre benzer gruplara ayır.

Öğrendiğim ince nokta: aynı veriden hem classification hem regression problemi
çıkabiliyor. "Sakatlandım mı" bir kategori (classification), "kaç gün oyun
dışı kaldım" bir sayı (regression).

**Day 2 — Classification: Naive Bayes ve KNN**
- KNN: en yakın k komşuya bakıp çoğunluğun sınıfını verir. Eğitim aşaması yok,
  tüm veriyi hafızada tutar ("lazy learner"). Bedelini tahmin anında öder.
- Naive Bayes: olasılıkları çarpar, en olası sınıfı seçer. "Naive" olması,
  özellikleri birbirinden bağımsız varsaymasından geliyor.

En çok kafama yatan şey ölçekleme meselesi oldu. KNN mesafeye göre çalıştığı
için, aralığı geniş olan özellik (ör. kolesterol 100-300 vs yaş 20-90) kararı
domine ediyor. Claude Code'a sorduğum meyve örneğinde bunu sayılarla test
ettim: ölçeklemeden 2-1 oylama çıkıyordu, ölçekledikten sonra 3-0 oldu ve
"komşu" sanılan bir nokta listeden düştü. Yani ölçekleme opsiyonel bir
iyileştirme değil, doğru komşuyu bulmanın ön şartı.

**Day 3 — Regression: Linear Regression ve Decision Trees**
- Linear regression veriye en uygun düz çizgiyi geçirir. Katsayılar okunabilir
  olduğu için iyi bir baseline. Ama doğrusal olmayan ilişkileri yakalayamıyor
  ve aykırı değere çok duyarlı — çünkü hataların KARESİNİ minimize ediyor,
  uzak nokta orantısız ceza yazdırıp çizgiyi kendine çekiyor.
- Decision tree evet/hayır sorularıyla veriyi böler. Doğrusal olmayan
  ilişkileri kendiliğinden yakalıyor, ölçekleme istemiyor, kurallar olarak
  okunabiliyor. Ama serbest bırakılırsa ezberliyor (overfitting).

Overfitting'i nasıl yakaladığımızı öğrendim: train/test split. Veriyi böl,
bir kısmını modele hiç gösterme, sonra o kısımda test et. Eğitimde %100 test
te %60 ise model öğrenmemiş, ezberlemiş demektir.

**Day 4 — Clustering: K-Means + karşılaştırma egzersizi**
K-Means iki adımı tekrarlıyor: her noktayı en yakın merkeze ata, sonra
merkezleri kendi noktalarının ortalamasına taşı. Merkezler kımıldamayı
bırakınca duruyor.

Tuzakları: k'yı ben seçiyorum, kümelerin yuvarlak olduğunu varsayıyor ve
başlangıç merkezlerine bağımlı. k seçimi için elbow yöntemini ve silhouette
skorunu öğrendim.

Claude Code'u egzersiz için kullandım — her algoritmayı gerçek dünya örneğiyle
açıklattım ve KNN vs Naive Bayes karşılaştırması yaptırdım.

**Karşılaştırma soruları — kendi cevaplarım**

1. KNN vs Naive Bayes: Metin verisi, hız gereksinimi veya az eğitim verisi
   varsa Naive Bayes. Özellikler birbiriyle güçlü ilişkiliyse (NB'nin
   bağımsızlık varsayımı bozulur), karar sınırı düzensizse veya verinin
   dağılımı hakkında varsayım yapmak istemiyorsam KNN. Kısaca: KNN'in düşmanı
   boyut ve hacim, Naive Bayes'in düşmanı korelasyon.

2. Linear Regression vs Decision Tree: Zıt yönlerde başarısız oluyorlar. LR
   ilişkinin şeklini baştan varsayıyor — doğru varsayarsa az veriyle çok iş
   çıkarır, yanlış varsayarsa hiçbir veri kurtarmaz; ayrıca tek bir aykırı
   değer tüm çizgiyi bozar. Decision tree hiçbir şey varsaymıyor ama savurgan
   ve gördüğü aralığın dışına çıkamıyor: eğitimde 300 m²'ye kadar ev gördüyse
   500 m²'lik eve de aynı fiyatı biçer, çünkü tahminleri yaprak ortalamaları.

3. Etiketsiz yeni veri setinde clustering doğru mu: Önce veride gerçekten
   yapı var mı diye kontrol etmek gerekiyor, çünkü algoritma her zaman küme
   döndürüyor — tamamen rastgele veriye bile. Kontrol yolları: 2 boyuta
   indirip gözle bakmak, silhouette skoruna bakmak, veriyi ikiye bölüp
   sonuçların tekrarlanıp tekrarlanmadığını görmek. Ayrıca "etiket yok" ile
   "etiket alınamaz" aynı şey değil — birkaç yüz örneği elle etiketleyip
   problemi supervised'a çevirebiliyorsam bu genelde daha güçlü olur.

**önemli bulduklarım**
- KNN ile K-Means'in ikisinde de "k" olması başta kafa karıştırıcıydı. KNN
  supervised ve k = kaç komşuya bakılacağı; K-Means unsupervised ve k = kaç
  küme oluşturulacağı.
- Doğrusal olmayan bir ilişkide "parçalı linear regression yapsak" diye
  düşünmüştüm, meğer bunun adı varmış (piecewise regression) ama kırılma
  noktalarını elle seçmek gerekiyor. Decision tree bunu otomatik yapıyor.
- Naive Bayes'in iki varsayımı olduğunu sonradan öğrendim: bağımsızlık
  (adındaki "naive" bu) ve her özelliğin belirli bir dağılıma uyduğu. İkincisi
  hiç aklıma gelmemişti.
