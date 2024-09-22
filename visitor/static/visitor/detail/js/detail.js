import { createApp } from 'vue'
import title from 'title'
import carousel from 'carousel'
import description from 'description'
import materials from 'materials'
import categories from 'categories'
import origin from 'origin'
import dating from 'dating'
import provenance from 'provenance'
import author from 'author'
import files from 'files'
import bibliography from 'bibliography'




const app = createApp({
   
    data() {
      return {
        objectid:$("#app").data("objectid"),
        object:null
      }
    },
    methods:{
        async fetchData(){
           
            
            let objectReq=await fetch("/api/objects/"+this.objectid,{
                method:"GET",
                credentials: 'omit'
            })
           
            
            let objectRes=await objectReq.json()
           
            this.object=objectRes
        }
    },
    async mounted(){
        await this.fetchData()
    }
  })

  app.component('objecttitle',title)
  app.component('carousel',carousel)
  app.component('description',description)
  app.component('materials',materials)
  app.component('categories',categories)
  app.component('origin',origin)
  app.component('dating',dating)
  app.component('provenance',provenance)
  app.component('author',author)
  app.component('files',files)
  app.component('bibliography',bibliography)
  app.mount("#app")