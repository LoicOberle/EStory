import { createApp } from 'vue'
import inventoryObjectList from 'inventoryobjectlist'
import newObjectButton from 'newobjectbutton'
import navbar from 'navbar'

const app = createApp({

    data() {
      return {
      }
    }
  })

  app.component('inventoryobjectlist',inventoryObjectList)
  app.component('newobjectbutton',newObjectButton)
  app.component('navbar',navbar)
  app.mount("#app")