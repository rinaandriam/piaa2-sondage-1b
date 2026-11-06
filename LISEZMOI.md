# Appli Sondage des ménages 1B · PIAA2 (version 1.0)

Application de saisie hors ligne du sondage des ménages (onglet 1B « Sondage des ménages » de l'outil de diagnostic et dimensionnement T0). Elle s'installe sur un téléphone Android depuis Chrome, fonctionne sans connexion, compte les ménages volontaires et possibles, et produit un fichier Excel au format exact de l'onglet 1B (colonnes A à V, mêmes libellés, mêmes listes).

## Contenu du dossier

| Fichier | Rôle |
|---|---|
| `index.html` | L'application complète (sondage, compteur, enregistrement, export Excel, fusion) |
| `sw.js` | Fonctionnement hors ligne |
| `manifest.webmanifest` | Nom, couleur et icônes de l'appli installée |
| `icons/` | Icônes de l'écran d'accueil |
| `icones.py` | Script qui régénère les icônes si besoin |

## 1. Mettre l'appli en ligne (une seule fois)

L'appli doit être publiée à une adresse https pour pouvoir s'installer. Le plus simple : GitHub Pages, gratuit, comme pour l'appli d'enquête T0.

1. Sur github.com, créer un **nouveau dépôt public**, par exemple `piaa2-sondage-1b`. Ne pas utiliser le dépôt PIAA2 existant : le dépôt de l'appli est public et ne contient que le code, aucune donnée de sondage.
2. Dans le dépôt : **Add file > Upload files**, déposer `index.html`, `sw.js`, `manifest.webmanifest` et le dossier `icons`, puis **Commit changes**.
3. **Settings > Pages** : Source « Deploy from a branch », branche `main`, dossier `/ (root)`, **Save**.
4. Une à deux minutes plus tard, l'appli est à l'adresse `https://<compte>.github.io/piaa2-sondage-1b/`.

## 2. Installer l'appli sur chaque téléphone

1. Avec une connexion, ouvrir l'adresse dans **Chrome**.
2. Toucher **Installer** dans l'appli, ou le menu ⋮ de Chrome > **Installer l'application** (ou **Ajouter à l'écran d'accueil**).
3. Ouvrir l'appli depuis l'écran d'accueil, puis **Réglages** : nom de l'enquêtrice, site, fokontany, **code du fokontany** et **code du site** (les mêmes que dans l'onglet Paramètres de l'outil), premier numéro de ménage, objectif (20), destinataire des fichiers.
4. Vérifier le hors ligne : mettre le téléphone en mode avion et rouvrir l'appli.

Plusieurs téléphones sur un même site : donner à chacun une plage de numéros (premier numéro 1, 101, 201…) pour éviter les doublons. Le code ménage est construit comme dans l'outil : code fokontany-code site-numéro, par exemple A3-17-S1-012.

## 3. Sur le terrain

- **Nouveau ménage** : identification, compréhension et intérêt (questions ouvertes d'abord), jusqu'à **3 dispositifs qui l'intéressent et possibles chez lui** (place et accord du propriétaire), volonté d'être accompagné, contribution, frein principal.
- Un ménage est **volontaire et possible** s'il est volontaire et si ses choix contiennent au moins un dispositif eau de pluie (citerne, cour perméable, puisard) et un dispositif déchets (composteur, coin de tri). L'appli l'affiche dès que les réponses sont données.
- **Compteur** sur l'accueil : ménages volontaires et possibles de ce téléphone par rapport à l'objectif. Le sondage s'arrête vers 20 ; avec plusieurs téléphones, le total se lit à la fusion ou dans l'outil.
- « Terminer » signale les réponses manquantes ; un second « Terminer » enregistre la fiche telle quelle.

**Chaque soir : Envoyer les données en Excel.** Selon le téléphone, l'appli ouvre directement WhatsApp ou Gmail. Sinon, le fichier est enregistré dans Téléchargements : le joindre comme document.

À ne pas faire avant d'avoir envoyé les fiches : effacer les données de Chrome, désinstaller l'appli, utiliser la navigation privée.

## 4. À la coordination

Chaque fichier reçu contient :

- **1B à coller** : une ligne par ménage, colonnes A à V identiques à l'onglet 1B de l'outil ;
- **Métadonnées** : identifiant de fiche, code ménage, « volontaire et possible », enquêtrice, dates, état de la fiche ;
- **Lisez-moi** : mode d'emploi du fichier.

**Plusieurs fichiers reçus :** ouvrir l'appli (téléphone ou ordinateur, même adresse), **Réglages > Fusionner des fichiers reçus**, choisir tous les fichiers. La fusion garde la version la plus récente de chaque fiche, donne le total des ménages volontaires et possibles et produit un fichier consolidé avec un onglet **Contrôles** (numéros en double, fiches à compléter).

**Report dans l'outil :** dans l'onglet « 1B à coller », sélectionner les lignes de données de la colonne A à la colonne V, copier ; dans l'onglet 1B de l'outil, se placer en colonne A sur la première ligne vide (à partir de la ligne 10), puis **Collage spécial > Valeurs**. Ne rien coller dans les colonnes grises W à Y : le code ménage, « volontaire et possible » et la ligne de l'enquête 1C se calculent seuls. Coller les nouveaux ménages sous les anciens : l'ordre des lignes de 1B donne l'ordre des lignes de 1C.

Test réalisé : 4 ménages saisis dans l'appli (numéros 101 à 104), exportés, fusionnés, puis collés dans une copie de l'outil exemple fictif : mêmes codes ménage (FKT-S1-101…), les 2 ménages volontaires et possibles passent seuls dans l'onglet 1C, compteur mis à jour, aucune erreur de calcul.

## 5. Points d'attention

- **Listes :** l'appli reprend exactement les libellés de l'onglet Paramètres de l'outil (bénéfices, intérêt, dispositifs, autre contribution, freins). Si ces listes changent, régénérer l'appli avec `assembler.py` (scripts du projet).
- **Ordre des dispositifs dans Paramètres :** les 3 premiers sont les dispositifs eau de pluie, les 2 derniers les dispositifs déchets ; l'appli et l'outil s'appuient sur cet ordre.
- **Pas de serveur :** rien n'arrive automatiquement. Les données restent sur le téléphone jusqu'à l'envoi du fichier.
- **Changer de téléphone :** Réglages > Changer de téléphone, puis choisir le dernier fichier Excel envoyé.

## 6. Mettre à jour l'appli

1. Remplacer les fichiers dans le dépôt GitHub.
2. Changer le numéro `VERSION` en tête de `sw.js` (par exemple `1.1`).
3. Les téléphones reçoivent la nouvelle version à la deuxième ouverture avec connexion. Les fiches déjà saisies sont conservées.
