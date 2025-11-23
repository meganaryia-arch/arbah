/**
 * Composable pour gérer la logique des citations
 */

import { ref, computed, type Ref, type ComputedRef } from 'vue';
import type { Quote, QuoteListResponse } from '@/config/api';
import apiService from '@/services/api.service';

export interface UseQuotesReturn {
  // State
  currentQuote: Ref<Quote>;
  allQuotes: Ref<Quote[]>;
  loading: Ref<boolean>;
  error: Ref<string | null>;

  // Computed
  hasQuotes: ComputedRef<boolean>;
  quoteCount: ComputedRef<number>;

  // Methods
  fetchRandomQuote: () => Promise<void>;
  fetchAllQuotes: () => Promise<void>;
  clearError: () => void;
}

export function useQuotes(): UseQuotesReturn {
  // State
  const currentQuote = ref<Quote>({} as Quote);
  const allQuotes = ref<Quote[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  // Computed
  const hasQuotes = computed(() => allQuotes.value.length > 0);
  const quoteCount = computed(() => allQuotes.value.length);

  // Methods
  const fetchRandomQuote = async (): Promise<void> => {
    loading.value = true;
    error.value = null;

    try {
      const response = await apiService.getRandomQuote();

      if (response.success && response.data) {
        currentQuote.value = response.data;
      } else {
        throw new Error('Format de réponse invalide');
      }
    } catch (err) {
      console.error('Erreur lors de la récupération de la citation aléatoire:', err);
      error.value = err instanceof Error ? err.message : 'Erreur inconnue';
    } finally {
      loading.value = false;
    }
  };

  const fetchAllQuotes = async (): Promise<void> => {
    try {
      const response = await apiService.getAllQuotes();

      if (response.success && response.data) {
        allQuotes.value = response.data;
      } else {
        throw new Error('Format de réponse invalide');
      }
    } catch (err) {
      console.error('Erreur lors de la récupération de toutes les citations:', err);
      error.value = err instanceof Error ? err.message : 'Erreur inconnue';
    }
  };

  const clearError = (): void => {
    error.value = null;
  };

  return {
    // State
    currentQuote,
    allQuotes,
    loading,
    error,

    // Computed
    hasQuotes,
    quoteCount,

    // Methods
    fetchRandomQuote,
    fetchAllQuotes,
    clearError,
  };
}