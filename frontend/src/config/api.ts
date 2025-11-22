/**
 * Configuration de l'API pour l'application Arbah
 */

// Configuration de base de l'API
export const API_CONFIG = {
  // URL de base de l'API backend
  BASE_URL: 'http://localhost:8000/api/v1',

  // Timeout par défaut pour les requêtes (en millisecondes)
  TIMEOUT: 10000,

  // En-têtes par défaut
  HEADERS: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
};

// Endpoints de l'API
export const API_ENDPOINTS = {
  // Quotes
  QUOTES_RANDOM: '/quotes/random',
  QUOTES_ALL: '/quotes/',
  QUOTES_BY_ID: (id: number) => `/quotes/${id}`,
  QUOTES_BY_AUTHOR: (author: string) => `/quotes/author/${encodeURIComponent(author)}`,
  QUOTES_BY_CATEGORY: (category: string) => `/quotes/category/${encodeURIComponent(category)}`,
  QUOTES_SEARCH: (query: string) => `/quotes/search/?q=${encodeURIComponent(query)}`,

  // Health & Meta
  HEALTH: '/health/',
  HEALTH_DETAILED: '/health/detailed',
  PING: '/health/ping',
  META: '/meta',
} as const;

// Messages d'erreur
export const ERROR_MESSAGES = {
  NETWORK: 'Erreur de connexion au serveur',
  TIMEOUT: 'Le serveur ne répond pas, veuillez réessayer',
  HTTP_404: 'Ressource non trouvée',
  HTTP_500: 'Erreur interne du serveur',
  UNKNOWN: 'Une erreur inattendue est survenue',
} as const;

// Types pour les réponses API
export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message: string;
}

export interface Quote {
  id: number;
  text: string;
  author: string;
  category: string;
  language: string;
  created_at: string | null;
  updated_at: string | null;
}

export interface QuoteListResponse {
  success: boolean;
  data: Quote[];
  count: number;
  message: string;
}

export interface HealthResponse {
  status: string;
  timestamp: number;
  app_name: string;
  version: string;
  environment: string;
  uptime: string;
}