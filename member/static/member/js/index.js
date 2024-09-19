import { createApp } from 'vue'
import navbar from 'navbar'

const app = createApp({

    data() {
      return {
      }
    }
  })

  app.component('navbar',navbar)
  app.mount("#app")