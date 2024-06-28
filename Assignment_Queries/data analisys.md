# Chart types 
We can make an **intro** with a **correlation matrix** to see if we can find other correlations to inspect.
- bar ch.
- scatter plot (multicolor) (matrix ?)
- combination
- stacked bar ch.
- cohort
- dist-plot
- chart with nations (geopandas)

> **Optionals:**
> - line ch. (?)
> - heat and treemap (?)
> - violin plot (?)
> - joint histogram (?)

---

## Line Chart
- Acquisti-vendite (spostamenti di giocatori) nei diversi anni 
- distribuzione dei giocatori per età (y= quantità di giocatori, x= età \[prevediamo una gaussiana])
- 

## Bar Chart
- x= numero partite (vittorie/sconfitte), y=anni, di una nazione (valutare se usare i club al posto delle nazioni/anni)
- x= numero partite (vittorie/sconfitte), y=nazioni, di un intervallo di tempo (valutare se usare i club al posto delle nazioni/anni)

### Heat and Treemap
- z= numero goal, x= campionati, y= Età >> prestazioni dei giocatori in diversi campionati in base all'età. (permette di capire se dei campionati sono più o meno adatti a giocatori con esperienza)
- y= nazione, x= età, z= player value (in base alla nazione, quanto vengono valutati i giocatori di diverse età \[prevedo che sarà una scena globale del calcio e non ci saranno particolari differenze tra le nazioni])

### Combinations
- pie chart= cartellini \[giallo, rosso, (altro?) ], y= quantità (di cartellini), x1=range di tempo 1 x2=range di tempo 2 ...
	correttezza di gioco col passare del tempo (riferito a un campionato?)
- pie chart= cartellini presi da giocatori in diverse categorie di età, y=y= quantità (di cartellini), x1=capionato? stagione?  x2=capionato? stagione? ...

### Stacked bar
- y=valore club stackati, x= nazione
	valore delle squadre per club (per ogni nazione)

---

# Storytelling
- **mobilità** dei giocatori (non per forza incentrata sui giocatori)
- studio di giocatori per **età** (incentrata sull'età)
- _quali squadre comprano più o meno giocatori?_
- studio dei **club** rispetto a: risultati delle partite (previsione), tendenza a vendere o comprare, 

# ?
- età media del massimo valore di mercato (y= quantità di giocatori, x= età dei giocatori nel loro picco massimo vi valore, z= densità dei giocatori per età dell'ultima valutazione)
- mobilità dei giocatori per nazione
- ==cartellini per origine dei player==