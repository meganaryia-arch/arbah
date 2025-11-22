/**
 * Composable pour gérer l'état de connexion à l'API
 */

import { ref, computed, onMounted, onUnmounted } from 'vue';
import apiService from '@/services/api.service';

export type ApiStatus = 'online' | 'offline' | 'checking';

export interface UseApiStatusReturn {
  // State
  apiStatus: ApiStatus;
  apiStatusText: string;
  isOnline: boolean;
  isOffline: boolean;
  isChecking: boolean;

  // Methods
  checkApiStatus: () => Promise<void>;
  startStatusPolling: () => void;
  stopStatusPolling: () => void;
}

export function useApiStatus(pollingInterval: number = 30000): UseApiStatusReturn {
  // State
  const apiStatus = ref<ApiStatus>('checking');
  const statusPollingInterval = ref<NodeJS.Timeout | null>(null);

  // Computed
  const apiStatusText = computed(() => {
    switch (apiStatus.value) {
      case 'online':
        return 'API en ligne';
      case 'offline':
        return 'API hors ligne';
      case 'checking':
        return 'Vérification de la connexion...';
    }
  });

  const isOnline = computed(() => apiStatus.value === 'online');
  const isOffline = computed(() => apiStatus.value === 'offline');
  const isChecking = computed(() => apiStatus.value === 'checking');

  // Methods
  const checkApiStatus = async (): Promise<void> => {
    apiStatus.value = 'checking';

    try {
      const isOnline = await apiService.isApiOnline();
      apiStatus.value = isOnline ? 'online' : 'offline';
    } catch (error) {
      console.error('Erreur lors de la vérification du statut API:', error);
      apiStatus.value = 'offline';
    }
  };

  const startStatusPolling = (): void => {
    // Nettoyer l'intervalle existant
    stopStatusPolling();

    // Vérifier immédiatement
    checkApiStatus();

    // Démarrer le polling
    statusPollingInterval.value = setInterval(() => {
      checkApiStatus();
    }, pollingInterval);
  };

  const stopStatusPolling = (): void => {
    if (statusPollingInterval.value) {
      clearInterval(statusPollingInterval.value);
      statusPollingInterval.value = null;
    }
  };

  // Lifecycle
  onMounted(() => {
    startStatusPolling();
  });

  onUnmounted(() => {
    stopStatusPolling();
  });

  return {
    // State
    apiStatus,
    apiStatusText,
    isOnline,
    isOffline,
    isChecking,

    // Methods
    checkApiStatus,
    startStatusPolling,
    stopStatusPolling,
  };
}