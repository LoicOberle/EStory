export default {
    data(){
        return {
            objects:[],
            dummy:""
        }
    },
    methods:{
        async fetchData(){
            const objectReq=await fetch("/api/inventory/objects",{
                method:"GET",
                credentials: 'omit'
            })
            
            
            const objectRes=await objectReq.json()
          
            this.objects=objectRes.data
            

        },
        getClasses(object){
          
            
            let res="object-item card"
            object.categories.forEach(element => {
                res+=" "+element.name
            });
            object.materials.forEach(element => {
                res+=" "+element.name
            });
            object.createdBy.groups.forEach(element => {
                res+=" "+element.name
            });
         
         
            
            return res
        },

        getThumbnail(object){
            
            let thumbnailAvailable=false
            let thumbnailSrc=""
            console.log(object.photos);
           object.photos.forEach(element => {
                if(element.thumbnail && element.viewable){
                    thumbnailAvailable=true
                    thumbnailSrc=element.image
                } 
           });
           if(!thumbnailAvailable){
            thumbnailSrc="/media/assets/noImage.jpg"
           }
            return thumbnailSrc
            
        }
    },
    async mounted(){
        await this.fetchData()

        
    },
    updated(){
        this.$root.$forceUpdate()
        
    },
    template:`

   


<div class="grid">


    <div v-for="object in objects" :class="getClasses(object)" data-category="transition" style="width: 18rem">
        <img :src="getThumbnail(object)" class="card-img-top" :alt="object.name" style="width: 100%;height:10rem;object-fit: cover; ">
            <div class="card-body">
                <h5 class="card-title name">{{object.name}}</h5>
                <a :href="'/visitor/list/detail/'+object.id" class="btn btn-primary">Detail</a>
            </div>
    </div>

</div>


    `
}

{/* 
     <div v-for="object in objects" class="object-item" data-category="transition">
    <h3 class="name">{{object.name}}</h3>

  </div>
    <div id="objectList">
 <input type="text" class="fuzzy-search" />

 <!-- Filter Buttons -->
<div class="filter-button-group">
  <button data-filter="*">Show All</button>
  <button data-filter=".test">Category 1</button>
  <button data-filter=".tree">Category 2</button>
</div>

    <ul id="my-list" class="list">
        <li v-for="object in objects" :class="getClasses(object)">
            <p class="name">{{object.name}}</p>
        </li>
    </ul>
 </div> */}