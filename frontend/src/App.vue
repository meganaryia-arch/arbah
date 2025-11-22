<template>
  <div class="app">
    <h1>Citation du jour</h1>

    <div class="quote-box">
      <p>{{ quote }}</p>
    </div>

    <button @click="fetchQuote">Nouvelle citation</button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const quote = ref("Clique pour charger une citation…");

async function fetchQuote() {
  const res = await fetch("http://localhost:8000/api/v1/quotes/random");
  const data = await res.json();
  quote.value = data.quote;
}

fetchQuote();
</script>

<style>
.app {
  font-family: sans-serif;
  text-align: center;
  padding: 50px;
}
.quote-box {
  margin: 20px auto;
  padding: 20px;
  border-left: 4px solid #42b883;
  font-style: italic;
  width: 60%;
}
button {
  padding: 10px 20px;
  background: #42b883;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 6px;
}
button:hover {
  background: #2d8f6f;
}
</style>
