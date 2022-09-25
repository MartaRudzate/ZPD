Šaha dāmu uzdevumi
====================

**Vispārīgais noteikums:** Uz galdiņa N*N rūtiņas novietotas N šaha dāmas
saucam par *derīgu izvietojumu*, ja
tās viena otru neapdraud (neatrastos uz tās pašas horizontāles,
vertikāles vai diagonāles).

Šis uzdevums ir daudz pētīts jau kopš 19.gadsimta;
par optimālu algoritmisku risinājumu publicēti dažādi raksti.
Sk. https://liacs.leidenuniv.nl/~kosterswa/nqueens/  (336 atsauces).
Šo to varētu atrast Sci Hub portālā; citas lietas ir tikai bibliotēkās.
Tur varbūt var atrast idejas arī priekš polimondu uzdevuma - ko un kā ir vērts meklēt.

Vairākas līdzības ar polimondu uzdevumu: Diezgan daudz atrisinājumu jebkuram N,  
bet nav zināma vienkārša induktīva pāreja, kura ļautu no derīga dāmu
izvietojuma NxN pāriet uz izvietojumu (N+1)x(N+1) vai, teiksim, (N+2)x(N+2).
Šaha dāmu uzdevuma varianti:

1. Atrast kaut kādu vienu derīgu šaha dāmu izvietojumu.
2. Dotajai N vērtībai atrast vai saskaitīt tos šaha dāmu izvietojumus,
   kuri ir centrāli simetriski (vai simetriski pret 90 grādu pagriezieniem).
   Dažām N vērtībām tādi izvietojumi neeksistē.
3. Dotajai N vērtībai saskaitīt visus šaha dāmu izvietojumus.
4. Dažādas definīcijas tam, kā derīgu šaha dāmu izvietojumu uz galdiņa NxN var
   "turpināt" uz lielāka galdiņa (N+k)x(N+k). Un eksperimenti, kuri ļautu
   pārbaudīt, kuras no šīm turpinājumu definīcijām var sastapt dzīvē.

   a. Viens turpināšanas veids: NxN galdiņa izvietojums vienkārši
      ir novietots (N+k)x(N+k) kreisajā augšējā stūrī; bet atlikušo kvadrātiņu kxk
      kaut kā aizpilda no jauna.
   b. Cits turpināšanas veids: NxN galdiņam jebkurās vietās ievieto k jaunas
      kolonnas un tās kaut kā aizpilda.
   c. Galdiņu (kN)x(kN) sadala vairākos "apakšgaldiņos" NxN, kurus katru atsevišķi aizpilda
      tāpat kā induktīvajā pieņēmumā; pēc tam kaut kā kombinē kopā.

Ja ir dažādi veidi, kā definēt derīgo šaha dāmu izvietojumu "turpināšanu",
tad var gadīties, ka polimondiem arī ir līdzīgi. Atbilstoši "turpināšanas" definīcijai
var konstruēt arī neiespējamības pierādījumu.



Risinājuma uzlabošanas soļi
------------------------------

Pašreizējais algoritms (queens.py - pielāgots no https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/ )
ir vienkāršs, bet stipri neefektīvs.
Ir vairāki veidi, kā varētu paātrināt algoritmu (daži no tiem var arī neko nedot - nezinām, kamēr neesam izmēģinājuši).
Katrs nākamais solis šajā virknītē ir grūtāks nekā iepriekšējie.
Var gadīties, ka algoritma optimizēšanā nemaz nepildīt tos pēdējos soļus.

1. Izmantojam numpy veselos skaitļus un līdzīgas C-stila
   datu struktūras, nevis Python integer tipu.
2. Atbrīvojamies no rekursīviem izsaukumiem - aizstājam tos ar cikliem
   pa masīvu veida datu struktūrām (nedaudz piņķerīgāks kods, bet cikli pa masīviem
   parasti strādā ātrāk nekā funkciju izsaukumu/aktivāciju steks).
3. Sadalām meklēšanas uzdevumu vairākiem procesiem vai vairākiem
   pavedieniem (ņemot vērā to, cik mūsu datoram ir procesora kodolu).
   Sk. https://b-ok.xyz/book/5291163/9e0fcf
   (Python Parallel Programming Cookbook: Over 70 recipes to solve challenges in multithreading
   and distributed system with Python 3 Giancarlo Zaccone)
   https://github.com/PacktPublishing/Python-Parallel-Programming-Cookbook-Second-Edition
4. Ieviešam "balansētu" meklēšanas koka augšanu, lai lavīnveidīgajā
   variantu skaita pieaugumā visos algoritma paralelizācijas soļos uzturētu variantu skaitu ierobežotu.
   Sk. L. De Giusti et al. "Parallelization of the N-queens problem. Load unbalance analysis."
   https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.926.6637&rep=rep1&type=pdf
5. Izdomāt SIMD (Single Instructions Multiple Data) algoritmu un pildīt to uz datora grafikas kartes.
   Šāds algoritms var sasniegt paātrinājumu, ja tas paralēli rēķina visās vietās vienu un to pašu -
   nebūs labi, ja tam būs zarošanās (atkarībā no datos atrastajām vērtībām).
   Tas ir līdzīgi kā manevrējama motocikla vietā savos aprēķinos
   ieviest traktora vilktas ecēšas - kas uzreiz noklāj lielu platību.
   Sk. Hands-On GPU Programming in Python.
   https://b-ok.xyz/book/5002329/09ed36
   GPU ir derīgi zināt, jo ar to bieži reizina matricas; taisa Neironu Tīklus un Mašīnmācīšanos.
6. Pārrakstām (jau paralelizētu?) algoritmu no Python kādā ātrākā valodā - teiksim, C++ vai Rust.


Veiktspējas mērījumi
-----------------------

Sk. https://www.quora.com/How-big-of-a-deal-would-it-be-to-find-an-explicit-formula-for-the-n-Queens-problem -
tur minēta skaitļu virknīte: cik ir derīgu izvietojumu katrai N vērtībai.
Šaha dāmu izvietojumu skaits dažādiem galdiņa izmēriem:

```
4 -> 2
5 -> 10
6 -> 4
7 -> 40
8 -> 92
9 -> 352
10 -> 724
11 -> 2680
12 -> 14200
13 -> 73712
14 -> 365596
```

14 dāmām variantu saskaitīšana (ar galīgi neoptimālu algoritmu queens.py) ilgst apmēram 6 minūtes.