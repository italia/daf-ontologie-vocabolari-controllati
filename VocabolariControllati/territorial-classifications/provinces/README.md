# Vocabolario Controllato delle Province d'Italia

### Contesto
Il vocabolario è stato creato in maniera automatica all'interno della Piattaforma Digitale Nazionale dei Dati (o altrimenti nota come DAF) - PDND - grazie a un dataset di ISTAT conferito nella stessa.

**Stato**: stabile

### Fonti
In particolare la fonte dati utilizzata è la seguente:

1. [elenco dei comuni di ISTAT](https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv) (dato aperto in formato CSV con licenza CC-BY 3.0 IT)

### Processo di generazione del vocabolario controllato
Il vocabolario è stato generato mediante un processo che nella PDND è chiamato [triplificatore](https://github.com/italia/daf-semantic-triplifier).
Il triplificatore si interfaccia mediante query SQL a dati conferiti alla PDND e memorizzati su [Impala](https://impala.apache.org/) nel dataset, disponibile in download CSV, denominato [Istat comuni italiani](https://dataportal.daf.teamdigitale.it/#/dataset/istat_comuni_italiani) e trasforma i dati secondo il modello RDF (in particolare sono serializzati in RDF-Turtle) utilizzando l'ontologia dei luoghi/indirizzi creata in collaborazione con ISTAT.

La trasformazione dei dati in RDF avviene sulla base di script definiti mediante lo standard [R2RML](https://www.w3.org/TR/r2rml/).
Gli script sono forniti nella relativa directory scriptR2RML del vocabolario.
Come si nota, gli script eseguono tipicamente una query SQL sulla fonte dati menzionata e i dati ottenuti vengono poi utilizzati per la costruizione delle triple soggetto - predicato - oggetto del vocabolario



### Struttura del Vocabolario
Il vocabolario è strutturato seguendo il modello CLV - Core Location Vocabulary di OntoPiA e il modello [skos](http://www.w3.org/2004/02/skos/core#), quest'ultimo utilizzato per tutti gli altri vocabolari controllati della rete.
