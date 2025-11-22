/**
 * Service API pour communiquer avec le backend Arbah
 */

import { API_CONFIG, API_ENDPOINTS, ERROR_MESSAGES, type ApiResponse, type Quote, type QuoteListResponse, type HealthResponse } from '@/config/api';

class ApiService {
  private baseUrl: string;

  constructor() {
    this.baseUrl = API_CONFIG.BASE_URL;
  }

  /**
   * Effectue une requête HTTP avec gestion d'erreurs
   */
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), API_CONFIG.TIMEOUT);

    try {
      const response = await fetch(url, {
        ...options,
        headers: {
          ...API_CONFIG.HEADERS,
          ...options.headers,
        },
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        throw new Error(this.getErrorMessage(response.status));
      }

      return await response.json();
    } catch (error) {
      clearTimeout(timeoutId);

      if (error instanceof Error) {
        if (error.name === 'AbortError') {
          throw new Error(ERROR_MESSAGES.TIMEOUT);
        }
        throw error;
      }

      throw new Error(ERROR_MESSAGES.UNKNOWN);
    }
  }

  /**
   * Récupère un message d'erreur selon le code HTTP
   */
  private getErrorMessage(status: number): string {
    switch (status) {
      case 404:
        return ERROR_MESSAGES.HTTP_404;
      case 500:
        return ERROR_MESSAGES.HTTP_500;
      default:
        return `Erreur HTTP: ${status}`;
    }
  }

  /**
   * Vérifie la santé de l'API
   */
  async checkHealth(): Promise<HealthResponse> {
    return this.request<HealthResponse>(API_ENDPOINTS.HEALTH);
  }

  /**
   * Ping l'API
   */
  async ping(): Promise<{ ping: string }> {
    return this.request<{ ping: string }>(API_ENDPOINTS.PING);
  }

  /**
   * Récupère une citation aléatoire
   */
  async getRandomQuote(): Promise<ApiResponse<Quote>> {
    return this.request<ApiResponse<Quote>>(API_ENDPOINTS.QUOTES_RANDOM);
  }

  /**
   * Récupère toutes les citations
   */
  async getAllQuotes(): Promise<QuoteListResponse> {
    return this.request<QuoteListResponse>(API_ENDPOINTS.QUOTES_ALL);
  }

  /**
   * Récupère une citation par son ID
   */
  async getQuoteById(id: number): Promise<ApiResponse<Quote>> {
    return this.request<ApiResponse<Quote>>(API_ENDPOINTS.QUOTES_BY_ID(id));
  }

  /**
   * Récupère les citations d'un auteur
   */
  async getQuotesByAuthor(author: string): Promise<QuoteListResponse> {
    return this.request<QuoteListResponse>(API_ENDPOINTS.QUOTES_BY_AUTHOR(author));
  }

  /**
   * Récupère les citations d'une catégorie
   */
  async getQuotesByCategory(category: string): Promise<QuoteListResponse> {
    return this.request<QuoteListResponse>(API_ENDPOINTS.QUOTES_BY_CATEGORY(category));
  }

  /**
   * Recherche des citations
   */
  async searchQuotes(query: string): Promise<QuoteListResponse> {
    return this.request<QuoteListResponse>(API_ENDPOINTS.QUOTES_SEARCH(query));
  }

  /**
   * Vérifie si l'API est accessible
   */
  async isApiOnline(): Promise<boolean> {
    try {
      await this.ping();
      return true;
    } catch {
      try {
        await this.checkHealth();
        return true;
      } catch {
        return false;
      }
    }
  }
}

// Export une instance singleton du service
export const apiService = new ApiService();
export default apiService;