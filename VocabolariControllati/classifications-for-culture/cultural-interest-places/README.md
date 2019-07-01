# Vocabolario controllato sui luoghi pubblici di interesse culturale

Il vocabolario controllato nasce dalla continua e proficua collaborazione tra il Team Digitale, l'Agenzia per l'Italia Digitale e il Ministero delle Attività e dei Beni Culturali (MIBAC).
Lo scopo del vocabolario è quello di individuare categorie di luoghi pubblici di interesse culturale.
Il vocabolario è stato creato principalmente per supportare la classificazione dei luoghi che si ritrovano nei siti web dei comuni; tuttavia, le voci del vocabolario sono sufficientemente generali per poter essere applicate in svariati contesti applicativi.

Le seguenti fonti sono state analizzate per la definizione del presente vocabolario.

## Fonti

1. Vocabolario controllato Beni Architettonici e Paesaggistici (BAP);
2. Vocaboli utilizzati nel contesto del Catalogo dei Beni Culturali dell'ICCD (Istituto Centrale per il Catalogo e la Documentazione)
3. Siti web dei comuni (es: [Comune di Trento](https://www.comune.trento.it/Aree-tematiche/Turismo/Visitare), [Comune di Bologna](https://www.bolognawelcome.com/home/scopri/luoghi/), ecc.)
4. Ontologia Cultural-ON e dati disponibili su dati.beniculturali.it

Il vocabolario è una tassonomia organizzata su due livelli.

## I livello

Il primo livello è costituito da 9 voci, identificate da etichette ufficiali, tipicamente al singolare, ed etichette alternative che si incontrano in altri sistemi o che sono più adatte per essere utilizzate nel contesto del design dei siti Web.
In particolare le voci ufficiali sono le seguenti:

1. Architettura militare e fortificata
2. Architettura residenziale
3. Area archeologica
4. Centro per la cultura
5. Edificio di culto
6. Monumento e complesso monumentale
7. Parco e giardino
8. Bellezza naturale
9. Luogo per lo sport e il tempo libero

Le etichette alternative, definite anche al plurale per esigenze di presentazione agli utenti, utilizzate per i siti web sono:

1. Rocche e castelli
2. Edifici residenziali
3. Aree archeologiche
4. Centri per la cultura
5. Edifici di culto
6. Monumenti
7. Parchi e giardini
8. Bellezze naturali
9. Luoghi per lo sport e il tempo libero

## II livello
Il secondo livello specializza il primo. Così come per il primo livello, anche per il secondo livello sono state individuate etichette ufficiali ed una o più etichette alternative (anche per i plurali dei nomi).
Di seguito riportiamo esempi di voci di secondo livello per ciascun elemento di primo livello.

1. Rocche e castelli --> Rocche, Castelli, Torri, Roccaforte, ecc.
2. Edifici residenziali --> Palazzi, Trulli, Ville, ecc.
3. Aree archeologiche --> Aree archeologiche, Siti archeologici
4. Centri per la cultura --> Cinema, Teatri, Gallerie, Musei, Scuole, Università/Facoltà, Archivi, ecc.
5. Edifici di culto --> Chiese, Cattedrali, Monasteri, Battisteri, Duomo, ecc.
6. Monumenti --> Monumenti, Complessi Monumentali, Sepolcri, ecc.
7. Parchi e giardini --> Parchi, Giardini, Belvedere, ecc.
8. Bellezze naturali --> Riserve naturali, Vulcani, Corsi d'acqua, ecc.
9. Luoghi per lo sport e il tempo libero --> Campi sportivi

## Osservazioni
Il vocabolario controllato, come tutti gli altri, segue le regole di OntoPiA ed è stato modellato mediante l'uso dell'ontologia standard del W3C [SKOS](https://www.w3.org/2004/02/skos/).
Ove ciò è stato possibile, il vocabolario controllato è allineato a concetti dell'ontologia schema.org.
L'allineamento è stato specificato mediante proprietà dell'ontologia skos quali exactMatch, quando l'allineamento vuole indicare equivalenza dei termini, closeMatch, quando l'allineamento indica concetti molto vicini tra loro e relatedMatch quando i concetti sono in un qualche modo correlati tra loro ma non necessariamente la stessa cosa.

Il Ministero dei Beni e delle Attività Culturali (MIBAC) sta predisponendo una variante del presente vocabolario che include molte più voci sia di primo livello che di secondo livello. La variante nasce per esigenze interne di catalogazione di un insieme molto più specifico di dati sui contenitori fisici dell'ICCD. Il vocabolario sarà pubblicato su repository github ufficiale del Ministero stesso e sarà allineato al presente, sempre mediante le proprietà succitate di SKOS. Quando il vocabolario sarà disponibile, anche il presente sarà allineato a quello del MIBAC.
