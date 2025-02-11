# Aufgabe 13 (Advanced)

Bewege den Character aus der Spirale raus, aber verwende nur `for` loops.




Idee: Das man for loops stacked um jede länge wieder etwas weiter muss.

```python
for i in range(5):
    for j in range(i):
        move()
```

Hier wird aber move gegeben. Ist eine komplexere methode die automatisch die richtige richtung geht für die Spirale.