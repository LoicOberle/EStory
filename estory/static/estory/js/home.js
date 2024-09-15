import { createApp } from 'vue'

import museumName from 'museumName'
import userMenu from 'userMenu'

const app = createApp({

    data() {
      return {
      }
    }
  })

  app.component('museumname', museumName);
  app.component('usermenu',userMenu)

  app.mount("#app")