# Vocabolario Controllato Relazioni di Parentela

### Contesto
Il vocabolario è stato creato per risolvere un problema nell'ontologia Core Person Vocabulary - Italian Application Profile (CPV-AP_IT) che si era venuto a creare tra il concetto di intestatario del foglio di famiglia e quello di relazione parentale. L'intestatario era infatti sia una persona che una relazione parentale. Questo creava un'incoerenza semantica derivante da alcune classi disgiunte di L0 allineate ai concetti qui riportati.
La soluzione al problema adottata è la seguente: l'intestatario del foglio di famiglia è una persona. Esiste comunque una relazione parentale che lo coinvolge e tutti i diversi tipi di relazioni parentali a oggi disponibili pubblicamente sono stati gestiti mediante anche questo vocabolario controllato, oltre che con relazioni tra persone già presenti nell'ontologia, anche nelle sue versioni più vecchie (in quest'ultimo caso, le relazioni sono le più comuni ma non tutte rispetto al vocabolario controllato qui riportato).
Il vantaggio di avere un vocabolario controllato a parte è che comunque esso può servire altri scopi e in caso di modifica delle voci o di aggiunta di nuove, queste non vanno a modificare la semantica offerta dall'ontologia.

**Stato**: prima versione bozza - il vocabolario non è completo ed è necessario attendere il raccordo di ISTAT in base ai regolamenti europei

### Fonti
1. [documentazione ISTAT](http://demografiche.istat.it/fileadmin/DCIS/TRACCIATO_E_REGOLE_CONTROLLO_01.pdf)
2. [Tabelle di riferimento - Tabella 5 Anagrafe Nazionale Popolazione Residente )](https://www.anpr.interno.it/portale/documents/20182/50186/tabella_5_relazioni_parentela.xlsx) allineato alle indicazioni ISTAT (dato di livello 2 secondo il modello per i dati a stelle - formato Excel - licenza specificata nelle note legali del Ministero dell'Interno - CC-BY 3.0)
