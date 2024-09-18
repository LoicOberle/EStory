import { createApp } from 'vue'
import inventoryObjectList from 'inventoryobjectlist'
import newObjectButton from 'newobjectbutton'


const app = createApp({

    data() {
      return {
      }
    }
  })

  app.component('inventoryobjectlist',inventoryObjectList)
  app.component('newobjectbutton',newObjectButton)
  app.mount("#app")