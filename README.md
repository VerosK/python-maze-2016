
# Bludiště

*Vytvořte modul pro řešení bludiště.*

Bludiště je konečná 2D matice, která může v každém bodu obsahovat buď
zeď nebo chodbu. Mezi sousedícími chodbami je možné procházet, zdí
procházet není možné. Za sousední políčko se považují taková políčka
se souřadnicemi (x1,y1), (x2,y2) pro která platí 

    abs(x1-x2) + abs(y1-y2) == 1

Bludiště má jeden začátek a jeden konec, ty se nachází na volných
polích.

Modul by měl implementovat:

- třídu `MazeGame`, kterýse umí inicializovat z řetězce

   - `MazeGame` by měl obsahovat metodu `getSize`, která vrátí
     velikost hrací desky
   - `MazeGame` by měl obsahovat metodu `isFree`, která vrátí
     jestli na daném políčku je volno nebo zeď
   - `MazeGame` by mělo obsahovat metodu `getSolution`, která
      vrátí nějakou nejkratší cestu mezi začátkem a koncem
      jako objekt `MazePath`
      - Pokud cesta neexistuje, vyvolá se výjimka `MazeError`
- výjimku `MazeError`, která se vyvolá v neočekávaných situacích
- objekt `MazePath`  umí vráti svoji délku (metoda `length`)
- objekt `MazePath` poskytuje iterátor, který vrací postupně
  všechny projitá políčka

## Ukázka použití:

    from maze import MazeGame

    # vytvoříme hru ze souboru (deska 2x3)
    game = MazeGame.fromString('B  \n  E')
    solution = game.getSolution()
    path_len = solution.length()
    for step,pos in enumerate(solution):
        print("{0}. Step to {1[0]}, {1[1]}".format(step, pos))


Pro řešení můžete použít libovovolné moduly (třeba pro BFS či 
Dijstrův algoritmus).  Pokud potřebujete nějaké speciální
moduly, přidejte je prosím do `requirements.txt`

Modul by měl projít dodanými testy. Pokud potřebujete něco otestovat, přidejte
testy i do modulu. Kromě základních testů budu testovat i délku a validitu cesty.

Pokud se všechno povede, tak zkusím připravit i nástroj na vizualizaci.

