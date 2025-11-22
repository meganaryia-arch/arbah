<template>
  <div class="app">
    <header class="header">
      <h1>📚 Arbah Citations</h1>
      <p class="subtitle">Des citations inspirantes en français</p>
    </header>

    <div class="quote-container">
      <!-- Loading State -->
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Chargement...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error">
        <p>❌ {{ error }}</p>
        <button @click="handleRetry" class="retry-btn">Réessayer</button>
      </div>

      <!-- Quote Display -->
      <div v-else class="quote-card">
        <div class="quote-text">
          <p>"{{ currentQuote.text }}"</p>
        </div>
        <div class="quote-meta">
          <p class="author">— {{ currentQuote.author }}</p>
          <span v-if="currentQuote.category" class="category">{{ currentQuote.category }}</span>
        </div>
      </div>

      <!-- Navigation -->
      <div v-if="!loading && !error" class="navigation">
        <button @click="fetchQuote" class="btn btn-primary">
          🎲 Citation aléatoire
        </button>
        <button @click="showAllQuotes = !showAllQuotes" class="btn btn-secondary">
          📋 {{ showAllQuotes ? 'Masquer' : 'Voir' }} toutes les citations
        </button>
      </div>

      <!-- All Quotes Section -->
      <div v-if="showAllQuotes && !loading" class="all-quotes">
        <h2>Toutes les citations ({{ quoteCount }})</h2>
        <div class="quotes-grid">
          <div v-for="quote in allQuotes" :key="quote.id" class="quote-item">
            <p>"{{ quote.text }}"</p>
            <div class="quote-item-meta">
              <span class="author">{{ quote.author }}</span>
              <span class="category">{{ quote.category }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- API Status -->
      <div class="api-status">
        <span :class="['status-indicator', apiStatus]"></span>
        <span>{{ apiStatusText }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useQuotes } from '@/composables/useQuotes';
import { useApiStatus } from '@/composables/useApiStatus';

// State
const showAllQuotes = ref(false);

// Use composables
const {
  currentQuote,
  allQuotes,
  loading,
  error,
  hasQuotes,
  quoteCount,
  fetchRandomQuote,
  fetchAllQuotes,
  clearError,
} = useQuotes();

const {
  apiStatus,
  apiStatusText,
  isOnline,
  isOffline,
  isChecking,
} = useApiStatus();

// Methods
const handleRetry = async () => {
  clearError();
  await fetchRandomQuote();
  await fetchAllQuotes();
};

// Lifecycle
onMounted(async () => {
  await fetchRandomQuote();
  await fetchAllQuotes();
});
</script>

<style lang="scss">
@use './styles/main.scss';
</style>
