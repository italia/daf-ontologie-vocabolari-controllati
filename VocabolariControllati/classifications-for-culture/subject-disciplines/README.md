# Vocabolario controllato Ambiti Disciplinari

Lo schema serve ad individuare delle categorie generali sotto cui indicizzare ambiti disciplinari, utilizzati anche per i luoghi e gli eventi della cultura (DB Unico del MIBACT). Lo scopo è quello di facilitare la ricerca e la navigazione delle informazioni da parte degli utenti.
Le fonti alla base dell’individuazione delle categorie sono l’elenco dei settori scientifico-disciplinari individuati dal [D. M. 4 ottobre 2000](http://www.miur.it/UserFiles/115.htm), il [Thesaurus Pico](http://www.culturaitalia.it/pico/thesaurus/4.3/thesaurus_4.3.0.skos.xml) e il [Nuovo Soggettario di Firenze](http://thes.bncf.firenze.sbn.it/ricerca.php).
Generalmente si è deciso di utilizzare come fonte della categorizzazione l’elenco del Ministero dell'Istruzione Università e Ricerca (MIUR) dei settori scientifico-disciplinari (con alcune integrazioni provenienti dagli altri Thesauri), ad eccezione dell’ambito Arte, per il quale si è ripresa la suddivisione proposta da [Pico](http://culturaitalia.it/pico/thesaurus/4.1#arte) (cfr. Thesaurus Pico - cosa - aree disciplinari – arte, con le relative suddivisioni in arti applicate, arti visive, arti dello spettacolo), che permette di rappresentare la complessità dei beni artistici con maggiore precisione.

Il vocabolario è stato creato nell'ambito di una collaborazione tra AgID e MIBACT (Ministero dei Beni e delle Attività Culturali e del Turismo) ed è realizzato mediante l'uso di SKOS (Simple Knowledge Organization System) un'ontologia standard per condividere e collegare sistemi organizzati di conoscenza via Web.

Le categorie sono state strutturate su tre livelli di specializzazione progressiva, a partire da un primo livello che racchiude 25 macroaree, per arrivare al terzo livello che prevede una specializzazione disciplinare più capillare.
Ogni categoria individuata a partire dalla denominazione del MIUR dei settori scientifico-disciplinari è allineata, dove possibile, con gli URI (Uniform Resource Identifier) dei termini corrispondenti in PICO (in questo caso tutti gli URI sono sottolivelli di aree disciplinari) e nel Nuovo Soggettario di Firenze (in questo caso gli URI sono sottolivelli non solo di discipline, ma anche di altre categorie – cfr. Appendice 3). Tali allineamenti:

+ sono relativi al nome della categoria, non alle sue relazioni con i livelli superiori o inferiori individuate dai rispettivi thesauri (cfr appendice 1). Per questo il tipo di legame tra i termini deve essere debole (skos:relatedMatch), ovvero tale che i termini non ereditino le relazioni gerarchiche e associative stabilite nei diversi sistemi di organizzazione della conoscenza;
+	non sempre presentano una corrispondenza letterale con i termini individuati nel Nuovo Soggettario (cfr. appendice 4);
+ in alcuni casi denominazioni nell’elenco MIUR sono rappresentate da URI separati nei thesauri (cfr Appendice 2), o viceversa. In questi casi è stata presa a riferimento la denominazione proposta nell’elenco MIUR.

## I livello

### Criterio utilizzato per l’individuazione delle categorie
Le categorie appartenenti al primo livello sono state individuate a partire dalla suddivisione in aree disciplinari proposta nel D. M. 4 ottobre 2000. A queste è stata aggiunta la categoria arte, basata principalmente sulla categorizzazione proposta da Pico.

### Osservazioni
Per facilitare la navigazione da parte degli utenti tra le diverse macrocategorie, le discipline che nel D.M. risultano unite in un’unica denominazione sono state divise in categorie separate.

Di seguito l’elenco delle aree del D.M. modificate:

1.	scienze matematiche e informatiche (D.M. 4 ottobre 2000 – Area 01) diviso in: scienze matematiche; scienze informatiche
2.	scienze agrarie e veterinarie (D.M. 4 ottobre 2000 – Area 07) diviso in: scienze agrarie; scienze veterinarie
3.	ingegneria industriale e dell'informazione (D.M. 4 ottobre 2000 – Area 09) diviso in: ingegneria industriale; ingegneria dell’informazione
4.	scienze dell'antichità, filologico letterarie e storico-artistiche (D.M. 4 ottobre 2000 – Area 10) diviso in: scienze dell’antichità; scienze filologico-letterarie; scienze storico-artistiche, linguistica; studi orientali
5.	scienze storiche, filosofiche, pedagogiche, psicologiche (D.M. 4 ottobre 2000 – Area 11) diviso in: storia; filosofia; pedagogia; psicologia


## II livello

### Criterio utilizzato per l’individuazione delle categorie
Le categorie sono state individuare a partire dai settori scientifico-disciplinari delle rispettive aree, individuati dal D. M. 4 ottobre 2000 (e modificati dal D.M. 18 marzo 2005)
Per quanto riguarda le categorie riferite al macrolivello arte, non avendo alcun corrispettivo all’interno dell’elenco MIUR, sono state riprese dal Thesaurus PICO e, dove possibile, allineate ai termini del Nuovo Soggettario. A tali categorie di PICO è stata aggiunta una nuova categoria, design, per permettere di raggruppare meglio i sottolivelli relativi a tale ambito.

### Osservazioni
Di seguito la lista delle modifiche rispetto alla lista dei settori scientifico-disciplinari  del MIUR (non sono riportate le modifiche relativa alla separazione della disciplina MIUR in due categorie distinte, perché elencate in Appendice 2).
Nell’area delle scienze fisiche (Area 02 del D.M.) sono state aggiunte le categorie:
+	acustica,
+	fisica molecolare,
+	fisica atomica,
+	meccanica (sono presenti altre meccaniche in MIUR che però sono più specifiche e non appartengono a fisica),
+	ottica,
+	fisica (categoria generica che in MIUR non c’è).

Nell’area scienze della terra (Area 04 del D.M.) sono state aggiunte le categorie:
+	climatologia,
+	geofisica (il MIUR ci sono due tipi di geofisica specifici, ma non questo generale),
+	idrologia.

Nell’area scienze biologiche (Area 05 del D.M.) sono state aggiunte le categorie:
+	biofisica,
+	biologia, (il MIUR ha diversi tipi specifici di biologia, ma non questo generale).

Nell’area scienze mediche (Area 06 del D.M.) è stata eliminata la categoria microbiologia (è rimasta la sola categoria microbiologia clinica), perché ripete lo stesso campo di microbiologia generale nell’area scienze biologiche (Area 05 del D.M.).
Nell’area ingegneria civile e architettura (Area 08 del D.M.) è stata aggiunta la categoria architettura ed eliminata la categoria disegno industriale (inserita invece come sottolivello di design).
Nell’area scienze dell'antichità è stata aggiunta la categoria archeologia (come categoria generica).

Nell’area scienze filologico letterarie sono state aggiunte le categorie:
+	filologia moderna,
+	lingua e letteratura straniera (come categoria generica),
+	storia della letteratura,
+	letteratura (come categoria generica).

Nell’area scienze storico-artistiche è stata eliminata la categoria etnomusicologia (compresa dentro la categoria musicologia e storia della musica) e aggiunta la categoria generica storia dell’arte.
Nell’area linguistica tutte le denominazioni, ad eccezione di  glottologia e linguistica e di didattica delle lingue moderne, sono state eliminate, perché ricomprese nella categoria lingua e letteratura straniera.

Nell’area storia (Area 11 del D.M.) sono state aggiunte le categorie:
+	storia locael,
+	storia orale,
+	storia politica,
+	storia sociale.

Nell’area filosofia (Area 11 del D.M.) sono state aggiunte le categorie:
+	epistemologia,
+	metafisica.

Infine, alcuni sotto-sottolivelli della macrocategoria storia dell’arte individuati dall’elenco MIUR (quali: discipline dello spettacolo, cinema, fotografia e televisione musicologia e storia della musica, etnomusicologia) sono stati eliminati perché duplicati dalle categorie Pico: cinema, fotografia; danza, musica, teatro (appartenenti alla macrocategoria arte).

## III livello

### Criterio utilizzato per l’individuazione delle categorie
Le categorie del III livello sono state individuate a partire dal Thesaurus Pico (e, dove necessario, integrate con termini del Nuovo Soggettario) e riguardano esclusivamente i beni storico-artistici e archeologici (in particolare solo le categorie: *archeologia classica, arti applicate, arti visive e arti dello spettacolo*)

### Osservazioni
I termini mutuati da Pico e collegati gerarchicamente al sopra-livello arti applicate sono stati integrati con altri termini ripresi dal Nuovo Soggettario, collegati gerarchicamente al termine arti decorative, in quanto categorie affini.


## Appendice 1 - Discrepanze tra elenco MIUR e Thesaurus Pico

Lista URI Pico che non appartengono alle stesse macrocategorie di MIUR:
1.	http://culturaitalia.it/pico/thesaurus/4.1#biblioteconomia_e_archivistica: in Pico è sottolivello di aree disciplinari; in MIUR è sottolivello di storia (a cui è affiancata anche bibliologia);
2.	http://culturaitalia.it/pico/thesaurus/4.1#numismatica: in Pico è sottocategoria di discipline storico-artistiche, nel MIUR è sottolivello di scienze dell'antichità, filologico-letterarie e storico-artistiche;proporre come macroarea a sé?
3.	http://culturaitalia.it/pico/thesaurus/4.1#egittologia: in Pico è sottolivello di archeologia, in MIUR di scienze dell'antichità, filologico-letterarie e storico-artistiche;
4.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_economiche: in Pico è sottolivello di scienze del comportamento, in MIUR è area disciplinare;
5.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_giuridiche: in Pico è sottolivello di scienze del comportamento, in MIUR è area disciplinare
6.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_politiche: in Pico è sottolivello di scienze del comportamento, in MIUR è area disciplinare
7.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_biologiche: in Pico sottolivello di scienze naturali, in MIUR area disciplinare
8.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_della_terra: in Pico sottolivello di scienze fisiche, in MIUR è area disciplinare
9.	http://culturaitalia.it/pico/thesaurus/4.1#geotecnica: in Pico sottolivello di scienze tecnologiche, in MIUR di ingegneria civile
10.	http://culturaitalia.it/pico/thesaurus/4.1#ingegneria_civile_e_architettura: in Pico sottolivello di scienze tecnologiche, in MIUR è area disciplinare
11.	http://culturaitalia.it/pico/thesaurus/4.1#ingegneria_industriale: in Pico sottolivello di scienze tecnologiche, in MIUR è area disciplinare (MIUR lo lega a ingegneria dell’informazione)
12.	http://culturaitalia.it/pico/thesaurus/4.1#ingegneria_dell_informazione: in Pico sottolivello di scienze tecnologiche, in MIUR è area disciplinare (MIUR lo lega a ingegneria industriale)
13.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_agrarie_e_veterinarie: in Pico sottolivello di scienze tecnologiche, in MIUR è area disciplinare
14.	http://culturaitalia.it/pico/thesaurus/4.1#progettazione_di_interni: allineata a MIUR architettura degli interni e allestimento, ma in Pico è sottolivello di arti applicate, in MIUR è sottolivello di ingegneria civile
15.	http://culturaitalia.it/pico/thesaurus/4.1#archeologia_dell_italia_antica e http://culturaitalia.it/pico/thesaurus/4.1#etruscologia: in Pico sottolivello di archeologia classica, in MIUR sottolivello di s scienze dell'antichità, filologico-letterarie e storico-artistiche
16.	http://culturaitalia.it/pico/thesaurus/4.1#archeologia_del_vicino_oriente: in MIUR sottolivello di studi orientali; in Pico sottolivello di archeologia classica
17.	http://culturaitalia.it/pico/thesaurus/4.1#letteratura_greca: in Pico sottolivello di letteratura, in MIUR sottolivello di scienze dell'antichità, filologico-letterarie e storico-artistiche raggruppare le letterature sotto letteratura
18.	http://culturaitalia.it/pico/thesaurus/4.1#letteratura_italiana: in Pico sottolivello di letteratura, in MIUR sottolivello di scienze dell'antichità, filologico-letterarie e storico-artistiche
19.	http://culturaitalia.it/pico/thesaurus/4.1#letteratura_latina: in Pico sottolivello di letteratura, in MIUR sottolivello di scienze dell'antichità, filologico-letterarie e storico-artistiche
20.	http://culturaitalia.it/pico/thesaurus/4.1#scienze_mediche: in Pico è sottolivello di scienze biologiche che è sottolivello di scienze naturali, in MIUR è area disciplinare
21.	http://culturaitalia.it/pico/thesaurus/4.1#pedologia: in Pico è sottolivello di scienze della terra, in MIUR è sottolivello di scienze agrarie;
22.	http://culturaitalia.it/pico/thesaurus/4.1#restauro: in Pico è  sottolivello di Scienze e tecnologia dei Beni Culturali, in MIUR è sottolivello di ingegneria civile o sottolivello di scienze dell'antichità, filologico-letterarie e storico-artistiche (denominazione: museologia e critica artistica e del restauro).

## Appendice 2

Denominazioni MIUR considerate come un'unica categoria, rappresentate da URI separati in Pico o nel Nuovo Soggettario (o viceversa)

1.	museologia e critica artistica e del restauro (2 URI in Pico e nel Nuovo Soggettario)
2.	etruscologia e antichità italiche (2 URI in Pico)
3.	geochimica e vulcanologia (2 URI in Pico e nel Nuovo Soggettario)
4.	logica e filosofia della scienza (2 URI PICO; nel Nuovo Soggettario non esiste il termine filosofia della scienza)
5.	astronomia e astrofisica (2 URI nel Nuovo Soggettario, 1 in Pico)
6.	scienze agrarie e veterinarie (2 URI nel Nuovo Soggettario, 1 in Pico)
7.	paleontologia e paleoecologia (2 URI nel Nuovo Soggettario, 1 in Pico)
8.	geografia fisica e geomorfologia (2 URI nel Nuovo Soggettario)
9.	petrologia e petrografia (2 URI nel Nuovo Soggettario)
10.	anatomia comparata e citologia (2 URI nel Nuovo Soggettario)
11.	microbiologia e microbiologia clinica (2 URI nel Nuovo Soggettario)
12.	diagnostica per immagini e radioterapia (2 URI nel Nuovo Soggettario)
13.	ginecologia e ostetricia (2 URI nel Nuovo Soggettario)
14.	orticoltura e floricoltura (2 URI nel Nuovo Soggettario)
15.	farmacologia e tossicologia veterinaria (2 URI nel Nuovo Soggettario)
16.	costruzioni idrauliche e marittime e idrologia (3 URI nel Nuovo Soggettario)
17.	topografia e cartografia (2 URI nel Nuovo Soggettario)
18.	misure elettriche e elettroniche (2 URI nel Nuovo Soggettario)
19.	archeologia cristiana e medievale (2 URI nel Nuovo Soggettario)
20.	lingua e letteratura greca (2 URI nel Nuovo Soggettario)
21.	filologia e linguistica romanza (2 URI nel Nuovo Soggettario)
22.	lingua e letteratura latina (2 URI nel Nuovo Soggettario)
23.	letteratura latina medievale e umanistica (2 URI nel Nuovo Soggettario)
24.	critica letteraria e letterature comparate (2 URI nel Nuovo Soggettario)
25.	archivistica, bibliografia e biblioteconomia (3 URI nel Nuovo Soggettario)
26.	geografia economico-politica (2 URI nel Nuovo Soggettario)
27.	psicologia dello sviluppo e psicologia dell'educazione (2 URI nel Nuovo Soggettario)
28.	psicologia del lavoro e delle organizzazioni  (2 URI nel Nuovo Soggettario)
29.	psicobiologia e psicologia fisiologica  (2 URI nel Nuovo Soggettario)
30.	diritto canonico e diritto ecclesiastico  (2 URI nel Nuovo Soggettario)
31.	Stampe, incisioni, matrici (3 URI diversi nel Nuovo Soggettario)
32.	scienze delle costruzioni e tecnica delle costruzioni (denominazioni separate in MIUR) fanno capo allo stesso URI Pico *scienze e tecnologie della costruzione*

## Appendice 3
Termini del Nuovo Soggettario che non appartengono alla categoria *discipline*:

| Categoria | Termini |
| --------- | ------- |
| Attività | architettura, arte, calcolo delle probabilità, chirurgia, chirurgia plastica, chirurgia pediatrica, chirurgia cardiovascolare, medicina riabilitativa, diagnosi per immagini, radioterapia, estimo rurale, arboricoltura, orticoltura, floricoltura, selvicoltura, alimentazione (tecnologia), disegno architettonico, restauro, pianificazione urbanistica, estimo, metallurgia, letteratura (greca, latina, cristiana antica, latina medievale, umanistica, italiana, italiana contemporanea, comparata, francese, spagnola, ispano-americana,portoghese, brasiliana, inglese, anglo-americana, tedesca, nordiche, nederlandese, romena, albanese neogreca, africane, araba, persiana, cinese, giapponese) critica letteraria, critica artistica, arti applicate, attività relative allo spettacolo, politica economica, finanza aziendale, agemina, arte vetraria, bricolage, calligrafia, ceramica, ceroplastica, conio, decorazione, doratura, ebanisteria, glittica, illustrazione, intaglio, niello, oreficeria, stencil, toreutica, culinaria, miniatura, design, cinema, fotografia, pittura, scultura, disegno, video art, danza, teatro, musica |
| Processi | Malattie dell’apparato respiratorio, malattie dell’apparato circolatorio, emopatie, malattie infettive, malattie degli occhi, malattie dell’apparato locomotore, malattie veneree, campi elettromagnetici, civiltà bizantina |
| Strutture | costruzioni rurali, costruzioni idrauliche, costruzioni marittime, impianti nucleari, impianti chimici |
| Forme | composizione architettonica, lingua (greca, latina, francese, spagnola, portoghese, inglese, tedesca, nordiche, nederlandese, romena, albanese, neogreca, africane, araba, persiana, cinese, giapponese), performance |
| Oggetti | costruzioni navali, macchine a fluido, azionamenti elettrici |
| Strumenti | misure meccaniche, telecomunicazioni, misure elettriche, misure elettroniche |
| Materia | idrocarburi |


## Appendice 4 - Nomi diversi tra MIUR e Nuovo Soggettario

| MIUR | Nuovo Soggettario |
| ---- | ----------------- |
| scienze veterinarie	| veterinaria |
| scienze economiche e statistiche | scienze economiche |
| probabilità e statistica | calcolo delle probabilità |
| fisica teorica, modelli e metodi matematici	| fisica teorica |
| fisica nucleare e subnucleare |	fisica nucleare |
| fisica applicata (a beni culturali, ambientali, biologia e medicina) | fisica applicata |
| chimica generale e inorganica	| chimica inorganica |
| chimica degli alimenti | chimica bromatologica |
| chimica dell'ambiente e dei beni culturali	| chimica ambientale (manca dicitura dei beni culturali) |
| geologia stratigrafica e sedimentologica	| stratigrafia |
| geologia strutturale	| tettonica |
| oceanografia e fisica dell'atmosfera	| oceanografia (manca dicitura *fisica dell'atmosfera*) |
| botanica generale |	botanica |
| microbiologia generale | microbiologia |
| statistica medica |	statistica sanitaria |
| patologia generale |patologia medica |
| oncologia medica | oncologia |
| microbiologia clinica | microbiologia medica |
| malattie del sangue |	emopatie |
| chirurgia generale | chirurgia |
| chirurgia pediatrica e infantile | chirurgia pediatrica |
| chirurgia cardiaca | chirurgia cardiovascolare |
| malattie apparato visivo | malattie degli occhi |
| medicina fisica e riabilitativa |	medicina riabilitativa |
| malattie cutanee e veneree | malattie veneree |
| diagnostica per immagini | diagnosi per immagini |
| pediatria generale e specialistica | pediatria |
| economia ed estimo rurale	| estimo rurale |
| agronomia e coltivazioni erbacee | agraria |
| arboricoltura generale e coltivazioni arboree	| arboricoltura |
| assestamento forestale e selvicoltura |	selvicoltura |
| genetica agraria | genetica vegetale |
| idraulica agraria e sistemazioni idraulico-forestali | idraulica agraria |
| costruzioni rurali e territorio agroforestale	| costruzioni rurali |
| entomologia generale e applicata | entomologia agraria |
| scienze e tecnologie alimentari	| alimentazione <tecnologie> |
| zootecnica generale e miglioramento genetico | zootecnia |
| patologia generale e anatomia patologica veterinaria | patologia veterinaria |
| parassitologia e malattie parassitarie degli animali | parassitologia veterinaria |
| costruzioni idrauliche e marittime | costruzioni idrauliche |
| trasporti	| ingegneria dei trasporti |
| composizione architettonica e urbana | composizione architettonica |
| tecnica e pianificazione urbanistica | pianificazione urbanistica |
| costruzioni e impianti navali e marini | costruzioni navali |
| misure meccaniche e termiche | misure meccaniche |
| chimica industriale e tecnologica	| chimica industriale |
| idrocarburi e fluidi del sottosuolo	| idrocarburi |
| convertitori, macchine e azionamenti elettrici | azionamenti elettrici |
| preistoria e protostoria | preistoria |
| etruscologia e antichità italiche	| etruscologia |
| critica artistica e del restauro | critica artistica |
| musicologia e storia della musica | musicologia |
| arti applicate | arti decorative |
| arti dello spettacolo	| attività relative allo spettacolo |
| egittologia e civiltà copta	| egittologia |
| lingue e letterature dell'africa | lingue africane, letterature africane |
| lingue e letterature della cina e dell'asia sud-orientale | lingua cinese, letteratura cinese |
| lingue e letterature del giappone e della corea	| lingua giapponese, letteratura giapponese |
| filosofia e teoria dei linguaggi | filosofia del linguaggio |
| psicologia fisiologica | psicofisiologia |
| istituzioni di diritto pubblico | diritto pubblico |
| diritto dell'unione europea | diritto comunitario |
| diritto romano e diritti dell'antichità | diritto romano |
| scienza politica | scienza della politica |
| sociologia generale |	sociologia |
| sociologia dei fenomeni politici | sociologia politica |
| sociologia giuridica, della devianza e mutamento sociale | sociologia del diritto |

| Pico | Nuovo Soggettario |
| ---- | ----------------- |
| performance art	| performance |
| arte del legno | ebanisteria |
| videoarte	| videoart |
