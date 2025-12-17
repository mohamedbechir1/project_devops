import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    host: true,
    proxy: {
      '/api': {
        target: 'http://devops_backend:8000',
        changeOrigin: true
      },
      '/health': {
        target: 'http://devops_backend:8000',
        changeOrigin: true
      }
    }
  }
})
