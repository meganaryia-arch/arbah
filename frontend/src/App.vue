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

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: #333;
}

/* Header */
.header {
  text-align: center;
  padding: 3rem 1rem 2rem;
  color: white;
}

.header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.subtitle {
  font-size: 1.2rem;
  opacity: 0.9;
  font-weight: 300;
}

/* Quote Container */
.quote-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Loading State */
.loading {
  text-align: center;
  padding: 3rem;
  color: white;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-top: 4px solid white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Error State */
.error {
  text-align: center;
  padding: 2rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  margin: 2rem 0;
}

.error p {
  color: #e74c3c;
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.retry-btn {
  background: #e74c3c;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s ease;
}

.retry-btn:hover {
  background: #c0392b;
}

/* Quote Card */
.quote-card {
  background: white;
  border-radius: 16px;
  padding: 2.5rem;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  margin: 2rem 0;
  position: relative;
  overflow: hidden;
}

.quote-card::before {
  content: '"';
  position: absolute;
  top: -20px;
  left: 20px;
  font-size: 120px;
  color: #f8f9fa;
  font-family: Georgia, serif;
  z-index: 0;
}

.quote-text {
  position: relative;
  z-index: 1;
  margin-bottom: 1.5rem;
}

.quote-text p {
  font-size: 1.4rem;
  line-height: 1.8;
  color: #2c3e50;
  font-style: italic;
  text-align: center;
}

.quote-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  position: relative;
  z-index: 1;
}

.author {
  font-size: 1.1rem;
  color: #7f8c8d;
  font-weight: 600;
}

.category {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

/* Navigation */
.navigation {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.btn {
  padding: 14px 28px;
  border: none;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background: linear-gradient(135deg, #42b883 0%, #35a06e 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(66, 184, 131, 0.4);
}

.btn-secondary {
  background: linear-gradient(135deg, #6c757d 0%, #5a6268 100%);
  color: white;
}

.btn-secondary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(108, 117, 125, 0.4);
}

/* All Quotes Section */
.all-quotes {
  margin: 3rem 0;
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.all-quotes h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
  font-size: 1.8rem;
}

.quotes-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.quote-item {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 12px;
  border-left: 4px solid #42b883;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.quote-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}

.quote-item p {
  font-size: 1rem;
  line-height: 1.6;
  color: #2c3e50;
  font-style: italic;
  margin-bottom: 1rem;
}

.quote-item-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.quote-item-meta .author {
  font-size: 0.9rem;
  color: #7f8c8d;
  font-weight: 600;
}

.quote-item-meta .category {
  background: #e9ecef;
  color: #495057;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
}

/* API Status */
.api-status {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-top: 2rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  backdrop-filter: blur(10px);
  color: white;
  font-size: 0.9rem;
}

.status-indicator {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  animation: pulse 2s infinite;
}

.status-indicator.online {
  background-color: #27ae60;
}

.status-indicator.offline {
  background-color: #e74c3c;
}

.status-indicator.checking {
  background-color: #f39c12;
}

@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7);
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255, 255, 255, 0);
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .header h1 {
    font-size: 2rem;
  }

  .subtitle {
    font-size: 1rem;
  }

  .quote-card {
    padding: 1.5rem;
    margin: 1rem 0;
  }

  .quote-text p {
    font-size: 1.2rem;
  }

  .navigation {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 300px;
  }

  .quotes-grid {
    grid-template-columns: 1fr;
  }

  .quote-meta {
    flex-direction: column;
    text-align: center;
  }
}
</style>
