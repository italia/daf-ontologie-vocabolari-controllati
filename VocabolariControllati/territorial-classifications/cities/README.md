# Vocabolario Controllato Archivio Storico dei Comuni d'Italia

### Contesto
Il vocabolario è stato creato all'interno della Piattaforma Digitale Nazionale dei Dati (o altrimenti nota come DAF) - PDND - grazie a due fonti dati principali conferite nella stessa.

**Stato**: stabile

### Fonti
1. [elenco dei comuni di ISTAT](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv) (dato aperto in formato CSV con licenza CC-BY 3.0 IT)
2. [archivio storico dei comuni gestito nell'ambito ANPR (Anagrafe Nazionale Popolazione Residente)](https://www.anpr.interno.it/portale/documents/20182/50186/ANPR_archivio_comuni+10062019.csv/94a1a635-c24c-4205-849f-7ca9150aa803) e allineato al dataset ISTAT (dato aperto in formato CSV - licenza specificata nelle note legali del Ministero dell'Interno - CC-BY 3.0)

### Processo di generazione del vocabolario controllato
Il vocabolario è stato generato utilizzando un processo che nella PDND è chiamato [triplificatore](https://github.com/italia/daf-semantic-triplifier).
Il triplificatore si interfaccia, mediante query SQL, a dati conferiti alla PDND e memorizzati su [Impala](https://impala.apache.org/) nel dataset, disponibile per il download in CSV, denominato [Anpr archivio storico](https://dataportal.daf.teamdigitale.it/#/dataset/anpr_archivio_storico_exte). I dati vengono poi trasformati secondo il modello RDF (in particolare sono serializzati in RDF-Turtle) utilizzando l'ontologia dei luoghi/indirizzi creata in collaborazione con ISTAT.

La trasformazione dei dati in RDF avviene sulla base di script definiti mediante lo standard [R2RML](https://www.w3.org/TR/r2rml/).
Gli script sono forniti nella relativa directory scriptR2RML del vocabolario.
Come si nota, gli script eseguono tipicamente una query SQL sulle due fonti dati prima menzionate e i dati ottenuti vengono poi utilizzati per la costruizione delle triple soggetto - predicato - oggetto del vocabolario



### Struttura del Vocabolario
Il vocabolario è strutturato seguendo il modello CLV - Core Location Vocabulary di OntoPiA e il modello [skos](http://www.w3.org/2004/02/skos/core#), quest'ultimo utilizzato per tutti gli altri vocabolari controllati della rete.

Un esempio di definizione di un Comune attualmente attivo è la seguente:

```
<https://w3id.org/italia/controlled-vocabulary/territorial-classifications/cities/025001-(1866-11-19)> a <https://w3id.org/italia/onto/CLV/City> , <https://w3id.org/italia/onto/CLV/Feature> , <https://w3id.org/italia/onto/CLV/AdminUnitComponent> , <http://www.w3.org/2004/02/skos/core#Concept> ;
	<http://www.w3.org/2002/07/owl#sameAs> <http://pt.dbpedia.org/resource/Agordo> , <http://fr.dbpedia.org/resource/Agordo> , <http://dbpedia.org/resource/Agordo> , <http://dati.isprambiente.it/id/place/25001> ;
	<http://www.w3.org/2004/02/skos/core#broader> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> ;
	<http://www.w3.org/2004/02/skos/core#broaderTransitive> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<http://www.w3.org/2004/02/skos/core#inScheme> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/cities> ;
	<http://www.w3.org/2004/02/skos/core#notation> "025001" ;
	<http://www.w3.org/2004/02/skos/core#preflabel> "AGORDO"@it ;
	<https://w3id.org/italia/onto/CLV/:hasGeographicalDistribution> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/geographical-distribution/2> ;
	<https://w3id.org/italia/onto/CLV/:hasHigherRank> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<https://w3id.org/italia/onto/CLV/hasDirectHigherRank> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> ;
	<https://w3id.org/italia/onto/CLV/hasIdentifier> <https://w3id.org/italia/data/identifiers/cities-identifiers/progressive-code/001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/alphanumeric-istat-code/025001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/numeric-istat-code/25001> , <https://w3id.org/italia/data/identifiers/cities-identifiers/cadastral-code/A083> ;
	<https://w3id.org/italia/onto/CLV/hasRankOrder> "4" ;
	<https://w3id.org/italia/onto/CLV/hasSOValidity> <https://w3id.org/italia/data/time-intervals/(1866-11-19)-(9999-12-31)> ;
	<https://w3id.org/italia/onto/CLV/situatedWithin> <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/025> , <https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/05> ;
	<https://w3id.org/italia/onto/TI/modified> "2016-06-17"^^<http://www.w3.org/2001/XMLSchema#date> ;
	<https://w3id.org/italia/onto/l0/name> "AGORDO"@it .
```

### URI
Essendo un vocabolario controllato è stata usata la stessa convenzione utilizzata in generale per i vocabolari controllati: https://w3id.org/italia/controlled-vocabulary seguito da tutti i concetti specifici del vocabolario.
Ogni URI del comune termina con la "concatenazione" del codice ISTAT e della data di istituzione, due elementi stabili nel tempo (ad eccezione di casi molto particolari in cui questi due elementi cambiano per via di errori di trascrizione alle fonti; questi eventi sono comunque rari).

### Interlinking
Il vocabolario controllato è collegato al vocabolario controllato delle regioni e delle province. Inoltre sono stati materializzati collegamenti ai seguenti due dataset esterni:

1. [DBpedia](https://wiki.dbpedia.org/) (inglese, francese e portoghese)
2. [Linked Open Data di ISPRA](http://dati.isprambiente.it/dataset/i-luoghi/).


### Note finali e ringraziamenti
Il dataset Archivio storico dei comuni non era in formato aperto prima dell'inizio del presente lavoro. Grazie all'impulso della PDND e alla produzione di questo dataset anche la fonte ora risulta essere disponibile a un permanent URL, in formato CSV, con la codifica UTF8 gestita e una tabella di accompagnamento che descrive la semantica delle colonne del CSV.

A tal proposito si ringrazia tutto il team dell'ANPR che ha prontamente agito in base alle richieste giunte, anche dalle comunità.
