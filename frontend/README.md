# Frontend Arbah - Application Vue.js

## 📖 Description

Le frontend Arbah est une application Vue.js 3 moderne qui consomme l'API backend Arbah pour afficher des citations inspirantes en français.

## 🏗️ Architecture

### Structure des Fichiers

```
frontend/src/
├── App.vue              # Composant principal de l'application
├── main.ts              # Point d'entrée de l'application Vue
├── config/
│   └── api.ts           # Configuration de l'API (URLs, endpoints, types)
├── composables/
│   ├── useQuotes.ts     # Logique de gestion des citations
│   └── useApiStatus.ts  # Logique de surveillance de l'état de l'API
├── services/
│   └── api.service.ts   # Service de communication avec l'API backend
├── stores/
│   └── counter.ts       # Store Pinia (exemple)
└── router/
    └── index.ts         # Configuration du routeur Vue Router
```

## 🔧 Technologies Utilisées

- **Vue.js 3** - Framework JavaScript progressif
- **TypeScript** - Typage statique JavaScript
- **Composition API** - Approche moderne de Vue.js
- **Composables** - Logique réutilisable
- **Fetch API** - Communication avec le backend
- **CSS3** - Styles modernes avec animations

## 📡 Connexion API

L'application se connecte au backend Arbah via ces endpoints principaux :

### Endpoints Utilisés

- `GET /api/v1/quotes/random` - Citation aléatoire
- `GET /api/v1/quotes/` - Toutes les citations
- `GET /api/v1/health/` - Vérification de santé de l'API

### Configuration CORS

Le backend est configuré pour autoriser les requêtes depuis :
- `http://localhost:3000`
- `http://localhost:8080`
- `http://localhost:5173` (serveur de développement Vite)

## 🚀 Démarrage Rapide

### Prérequis

- Node.js 18+
- npm ou yarn

### Installation

```bash
# Installer les dépendances
npm install

# Démarrer le serveur de développement
npm run dev
```

L'application sera accessible sur `http://localhost:5173`

## 🎨 Fonctionnalités

### Interface Principale

- **Affichage de citation aléatoire** avec bouton de rafraîchissement
- **Visualisation de toutes les citations** en mode grille
- **Indicateur de statut API** en temps réel
- **Gestion des erreurs** avec messages clairs et bouton de retry
- **Loading states** avec animations fluides

### État de Connexion

- 🟢 **En ligne** - API accessible
- 🔴 **Hors ligne** - API inaccessible
- 🟡 **Vérification** - En cours de test

## 🔧 Personnalisation

### Configuration API

Modifier `src/config/api.ts` pour changer :

```typescript
export const API_CONFIG = {
  BASE_URL: 'http://localhost:8000/api/v1',  // URL de votre API
  TIMEOUT: 10000,                           // Timeout en ms
};
```

### Styles

Les styles sont personnalisables dans `App.vue` :

- Thème de couleurs (dégradé violet)
- Typographie et espacements
- Animations et transitions
- Design responsive (mobile-first)

## 🛠️ Architecture des Composables

### useQuotes

Gère la logique des citations :
- Récupération des citations aléatoires
- Récupération de toutes les citations
- Gestion des états (loading, error)
- Données réactives

### useApiStatus

Surveille l'état de l'API :
- Vérification régulière de la connectivité
- Polling automatique (30s par défaut)
- Indicateurs visuels d'état

## 🔄 Communication avec le Backend

### Flux de Données

1. **Composant App.vue** utilise `useQuotes()` et `useApiStatus()`
2. **useApiStatus()** vérifie la connectivité via `apiService`
3. **useQuotes()** récupère les données via `apiService`
4. **apiService** fait les appels HTTP avec gestion d'erreurs
5. **Backend** répond avec JSON formaté

### Format de Réponse Backend

```json
{
  "success": true,
  "data": {
    "id": 1,
    "text": "La vie est une fleur dont l'amour est le miel.",
    "author": "Victor Hugo",
    "category": "Amour",
    "language": "fr",
    "created_at": null,
    "updated_at": null
  },
  "message": "Random quote retrieved successfully"
}
```

## 🎯 Améliorations Futures

- [ ] Système de favoris pour les citations
- [ ] Filtrage par catégorie et auteur
- [ ] Mode sombre/clair
- [ ] Partage de citations sur réseaux sociaux
- [ ] Mode plein écran
- [ ] Animations de transition améliorées
- [ ] Internationalisation (i18n)

## 🐛 Débogage

### Outils de Développement

- **Vue DevTools** - Inspection des composants et états
- **Console du navigateur** - Logs d'erreurs et réseau
- **Network Tab** - Vérification des requêtes API

### Erreurs Courantes

1. **CORS** - Vérifier que le backend autorise votre origine
2. **API Down** - Démarrer le backend sur le port 8000
3. **Type Errors** - Vérifier les imports TypeScript

## 📝 Développement

### Ajouter une Nouvelle Fonctionnalité

1. Créer un nouveau composable si nécessaire
2. Ajouter les types dans `config/api.ts`
3. Implémenter la méthode dans `services/api.service.ts`
4. Utiliser dans les composants Vue

### Bonnes Pratiques

- Utiliser TypeScript pour le typage fort
- Garder les composants petits et réutilisables
- Gérer les états de chargement et d'erreur
- Écrire des tests pour les fonctions critiques
- Documenter les nouvelles fonctionnalités

---

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

**Développé avec ❤️ pour l'application Arbah**