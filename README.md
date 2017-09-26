# Ontologie e Vocabolari Controllati

Questo è il repository delle ontologie e dei vocabolari controllati sviluppati nell'ambito delle azioni previste dal piano triennale e a supporto del lavoro da svolgere per l'[elenco delle basi di dati chiave](http://elenco-basi-di-dati-chiave.readthedocs.io/it/latest/).
Le ontologie create sono tra loro collegate creando una vera e propria network chiamata **OntoPA** - a OntoNet system.

Il repository è suddiviso in due directory:

  + **Ontologie**: contiene le ontologie OWL, serializzate principalmente in RDF/Turtle e altre serializzazioni RDF quali RDF/XML e JSON-LD. I diagrammi UML delle ontologie sono attualmente in fase di definizione e revisione a seguito dei collegamenti abilitati tra tutte le ontologie. Le ontologie hanno label e commenti sia in inglese (EN), sia in italiano (IT).
  + **Vocabolari controllati**: contiene un primo elenco dei vocabolari controllati sviluppati anche a supporto delle ontologie.

Il contenuto della directory Ontologie è attualmente il seguente:

  + **Globale-AP**: Ontologia che importa tutte quelle finora sviluppate presenti in questa directory e quelle che saranno inserite nel catalogo delle ontologie e dei vocabolari controllati (si veda la parte [daf-semantics](https://github.com/italia/daf-semantics) e [ontonethub](https://github.com/teamdigitale/ontonethub) per il software relativo al catalogo). L'ontologia è attualmente in fase di sviluppo e includerà alcuni assiomi generali e servirà come unico punto di accesso a tutte.
  + **Eventi IoT**: Ontologia del profilo applicativo italiano degli eventi IoT (IoT-AP_IT - IoT Italian Application Profile).
  + **Persone**: Ontologia del profilo applicativo italiano sulle persone (CPV-AP_IT - Core Person Vocabulary-Italian Application Profile). Nella directory relativa all'ultima versione attuale dell'ontologia vi è anche il file con i relativi allineamenti a ontologie esterne del Web (e.g., FOAF).
  + **Organizzazioni**: Ontologia del profilo applicativo italiano sulle organizzazioni (pubbliche e private) (COV-AP_IT - Core Organization Vocabulary - Italian Application Profile). E' attualmente in fase di definizione il file di allineamneti a ontologie esterne del Web quali Org, RegOrg, Core Public Organization Vocabulary, ecc.
  + **Indirizzi/luoghi**: Ontologia del profilo applicativo italiano sugli indirizzi e luoghi (CLV-AP_IT - Core Location Vocabulary - Italian Application Profile). Nella directory relativa all'ultima versione attuale dell'ontologia vi è anche il file con i relativi allineamenti a ontologie esterne del Web (e.g., Core Location Vocabulary, AD conforme a INSPIRE, GeoSparql, Geonames, ecc.).
  + **SocialMedia**: Ontologia di supporto. Essa è il profilo applicativo italiano per la modellazione dei social media, utilizzati sia nell'ontologia delle organizzazioni che in quella delle persone.
  + **Tempo**: Primissima versione dell'ontologia di supporto del tempo utilizzata in tutte le ontologie precedenti per cogliere la dimensione temporale dei principali concetti.
  + **Livello0 (L0)**: E' un'ontologia top-level che consente di collegare tutte le ontologie sopra elencate abilitando così la network di ontologie.

Il contenuto della directory Vocabolari Controllati è attualmente il seguente:

  + **Tipi Eventi Pubblici**: E' una classificazione dei possibili tipi di eventi pubblici.
  + **Licenze**: E' la classificazione delle licenze suddivise per tipologia. Questo è il vocabolario controllato da utilizzare per il profilo di metadatazione nazionale DCAT-AP_IT.
  + **Mapping Temi-Sottotemi**: E' il mapping tra i 13 temi del profilo DCAT-AP_IT e alcune voci del vocabolario Eurovoc da utilizzare per la proprietà [dct:subject](https://linee-guida-cataloghi-dati-profilo-dcat-ap-it.readthedocs.io/it/latest/dataset_elementi_raccomandati.html#sottotema-del-dataset-dct-subject) del profilo DCAT-AP_IT. Il mapping puà essere utilizzato anche in applicativi per guidare l'utente a selezionare i sottotemi Eurovoc in linea con i temi DCAT-AP_IT. Il mapping è basato principalmente sull'analogo mapping utilizzato dall'European Data Portal.
  + **Classificazione Territorio**: E' un dataset RDF allineato con l'ontologia degli Indirizzi/Luoghi suddetta (CLV-AP_IT) basato sul dataset CSV fornito da ISTAT sulla suddivisione Regione/Provincia/Comune e relativi codici.

Le ontologie e i vocabolari controllati potranno ancora subire cambiamenti rispetto a quelli qui inclusi anche a seguito di collaborazioni in atto con altri team quali quello dell'ISTAT e il team ANPR.
