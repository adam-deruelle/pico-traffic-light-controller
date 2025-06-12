# 🚦 SAÉ 4 – Contrôleur de feux de circulation intelligent

## 🎯 Objectif du projet

Créer un système automatisé de gestion de feux de circulation, capable de :
- Gérer deux feux de circulation (Voie 1 et Voie 2)
- Intégrer une **priorité piéton** via des boutons
- Basculer entre **mode jour/nuit**
- Détecter une **panne** et afficher l'état du système

Le système est embarqué sur une carte **Raspberry Pi Pico**, programmé en **CircuitPython**.

## ⚙️ Architecture générale

Le contrôleur gère :

- **6 LED pour les feux** (Vert, Orange, Rouge x2)
- **2 boutons piétons**
- **1 boucle magnétique** (détection véhicule)
- **1 écran OLED SPI** (interface utilisateur)
- **1 LED intégrée** (indication mode)
- **3 boutons Menu/Plus/Moins** pour modifier les durées

Le programme utilise :
- Des **temporisations** configurables via `TON` (Timer ON)
- Une interface **affichée en temps réel** sur l’écran OLED
- Une **détection analogique de panne** (seuil > 3V)

## 🛠️ Fonctionnalités implémentées

### 🔁 Cycle des feux

| Étapes       | Description                          |
|--------------|--------------------------------------|
| X0           | Feu 1 : Vert                         |
| X10 → X20    | Feu 1 : Orange puis Rouge            |
| X30 → X50    | Feu 2 : Vert → Orange                |
| X60          | Feu 2 : Rouge → retour à X0          |

Les transitions sont déclenchées par des temporisations et/ou événements : bouton piéton, boucle magnétique.

### 🧭 Modes de fonctionnement

- `jour/nuit` : alternance automatique via minuteurs
- `jour` : mode fixe en journée
- `nuit` : mode fixe en nocturne
- Le mode est configurable via l’écran OLED et les boutons

### 🧱 Affichage OLED (menu interactif)

L'écran affiche :
- Durée de chaque feu (modifiable)
- Mode de fonctionnement
- Possibilité de redémarrer ou sortir du menu

### ⚠️ Gestion de panne

Un capteur analogique vérifie une tension > 3V.  
En cas de panne :
- Le programme affiche l’erreur
- Les feux sont désactivés ou figés selon le mode

## 💡 Logique de programmation

La logique principale repose sur :
- Des variables d’étapes (`X0`, `X10`, …)
- Des conditions d’évolution (CE) basées sur `Timer.Q` et entrées
- La mise à jour permanente des sorties en fonction de l'état

## ✅ Résultats obtenus

- Système 100% fonctionnel en conditions simulées
- Interface intuitive pour modifier les durées
- Détail complet de l'automatisme dans le code Python
- Affichage clair de l'état et détection de panne efficace

---

## 📝 Compétences mobilisées

- Programmation microcontrôleur (CircuitPython)
- Utilisation de GPIO (entrées/sorties digitales et analogiques)
- Interface utilisateur embarquée (écran SPI)
- Logique séquentielle et états
- Maintenance logicielle et affichage dynamique

---

> 👨‍💻 Projet réalisé par Adam DERUELLE - Melvin ALLARD – GEII – IUT de Rennes
