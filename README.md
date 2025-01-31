# Projet PARM SI3

Voir `doc/Description_Projet_PARM_SI3.pdf` pour la description du projet.

## En-têtes C

| Programme | Description |
|-|-|
| crypto | Cryptographie |
| fixed | Nombres décimaux à virgule fixe |
| math | Outils mathématiques |
| parm | En-tête principale |
| stdio | Entrées/sorties textuelles (clavier, terminal) |
| string | Implémentation basique de chaînes |
| string2 | Autre implémentation basique de chaînes |
| trigo | Fonctions trigonométriques (séries de Taylor) |
| utils | Outils de débogage |
| video | Écran matriciel |

## Programmes fournis en exemple

### Programmes C

|   Programme   |                       Description                           |
|---------------|-------------------------------------------------------------|
| calckeyb		| Calculatrice avec clavier et terminal                       |
| calculator	| Calculatrice avec DIP-switches                              |
| simple_add    | Effectue l'addition de deux variables et l'affiche dans RES |
| testfp		| Démonstration des macros de nombres à virgule fixe          |
| tty			| Affiche "Projet PARM" dans le terminal                      |

## MMIO

Voir `parm.h` pour la documentation technique des broches.


-------------------------------

## Qu'est-ce que Parm354N ?

Il s'agit d'un processeur 32-bits virtuel à jeu d'instructions réduit (~50 instructions) sur 16 bits.
Réalisé par les étudiant de Polytech Nice-Sophia en spécialité informatique :
- **Patrick BIZOT**
- **Lohann COLLE**
- **Deyann KOPERECZ**
- **Zaynab NACHABE**

Lien vers le github de Parm354N : https://github.com/BarbaTeam/parm-based-processor-24-25-Parm354N

## Compiler son code C pour Parm354N

### Méthode classique :

1. Traduire son code en langage assembleur adapté au processeurParm354N avec la commande suivante :
   ```sh
   clang -S -target arm-none-eabi -mcpu=cortex-m0 -O0 -mthumb -nostdlib -I./include main.c
   ```
   > [!NOTE]
   > S'assurer que son code C est dans le dossier `code_c`, autrement il faudra modifier le chemin `./include`.
2. Puis assembler le fichier avec la commande suivante :
    ```sh
    python ./script/parm_assembler.py main.s main.bin
    ```

### Méthode simplifiée :

Utiliser le scripts `scripts/parmesan.sh` :
```sh
./parmesan.sh ./main.c ./main.bin
```