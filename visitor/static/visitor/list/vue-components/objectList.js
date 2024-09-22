export default {
    data(){
        return {
            objects:[],
            dummy:""
        }
    },
    methods:{
        async fetchData(){
            const objectReq=await fetch("/api/objects",{
                method:"GET",
                credentials: 'omit'
            })
            
            
            const objectRes=await objectReq.json()
          
            
            this.objects=objectRes.results.filter((o)=>{return o.viewable})
            

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
