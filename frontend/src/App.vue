<template>
  <main style="font-family: system-ui, sans-serif; padding: 2rem; max-width: 680px; margin: 0 auto;">
    <h1>DevOps Demo App</h1>
    <p>Frontend: Vue 3 + Vite. Backend: FastAPI. DB: PostgreSQL.</p>

    <section style="margin-top: 1rem;">
      <button @click="pingBackend" :disabled="loading">{{ loading ? 'Loading...' : 'Ping Backend' }}</button>
      <pre v-if="message" style="background:#f5f5f5; padding: 1rem; white-space: pre-wrap;">{{ message }}</pre>
    </section>

    <section style="margin-top: 2rem;">
      <h2>Sentiment Analysis</h2>
      <div style="display:flex; gap:0.5rem; align-items:flex-start;">
        <input v-model="inputText" placeholder="Type text here..." style="flex:1; padding:0.5rem;" />
        <button @click="analyze" :disabled="analyzing || !isValid">{{ analyzing ? 'Analyzing...' : 'Analyze' }}</button>
      </div>
      <small v-if="!isValid" style="color:#b71c1c; display:block; margin-top:0.25rem;">Enter at least 3 non-space characters.</small>
      <pre v-if="aiResult" style="background:#f5f5f5; padding: 1rem; white-space: pre-wrap; margin-top:0.75rem;">{{ aiResult }}</pre>
      <div v-if="aiData" style="margin-top:0.75rem; display:flex; align-items:center; gap:0.5rem;">
        <span class="badge" :class="aiData.label === 1 ? 'badge-pos' : 'badge-neg'">{{ aiData.label === 1 ? 'Positive' : 'Negative' }}</span>
        <span>Score: {{ (aiData.score * 100).toFixed(0) }}%</span>
      </div>
      <div v-if="aiData" class="bar" aria-label="sentiment score" :title="`Score ${Math.round(aiData.score*100)}%`">
        <div class="bar-fill" :style="{ width: Math.max(0, Math.min(100, Math.round(aiData.score*100))) + '%' }"></div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import axios from 'axios'
import { ref, computed } from 'vue'

const loading = ref(false)
const message = ref('')
const inputText = ref('')
const analyzing = ref(false)
const aiResult = ref('')
const aiData = ref<{ label: number; score: number } | null>(null)
const isValid = computed(() => (inputText.value || '').trim().length >= 3)


async function pingBackend() {
  loading.value = true
  message.value = ''
  try {
    const res = await axios.get('/api/hello', { timeout: 5000 })
    message.value = JSON.stringify(res.data, null, 2)
  } catch (e: any) {
    message.value = e?.message || String(e)
  } finally {
    loading.value = false
  }
}

async function analyze() {
  analyzing.value = true
  aiResult.value = ''
  aiData.value = null
  try {
    const res = await axios.post('/api/sentiment', { text: inputText.value }, { timeout: 5000 })
    aiResult.value = JSON.stringify(res.data, null, 2)
    aiData.value = { label: Number(res.data?.label ?? 0), score: Number(res.data?.score ?? 0) }
  } catch (e: any) {
    aiResult.value = e?.message || String(e)
  } finally {
    analyzing.value = false
  }
}
</script>

<style>
button { padding: 0.5rem 1rem; }
input { border: 1px solid #ddd; border-radius: 4px; }
.badge { padding: 0.25rem 0.5rem; border-radius: 9999px; font-size: 0.85rem; color: #fff; }
.badge-pos { background: #2e7d32; }
.badge-neg { background: #c62828; }
.bar { height: 10px; background: #eee; border-radius: 6px; overflow: hidden; margin-top: 0.5rem; }
.bar-fill { height: 100%; background: linear-gradient(90deg, #c62828, #f9a825, #2e7d32); }
.theme-toggle { background: transparent; color: var(--muted); border: 1px solid var(--border); }
</style>
