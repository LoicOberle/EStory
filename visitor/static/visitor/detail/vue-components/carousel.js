export default {
    data(){
        return {
            photos:[]
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
           
            
            this.photos=object.photos
            
            
        },
        getPhotoClasses(index){
            let res="carousel-item "
            if (index==0) {
                res+="active"
            }
            return res
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
   <div id="carousel" class="carousel slide">
    <div class="carousel-indicators">
        <button v-for="(photo,index) in photos" type="button" data-bs-target="#carousel" :data-bs-slide-to="index"
            class="active" aria-current="true" :aria-label="'Photo'+(index+1)"></button>
    </div>

    <div class="carousel-inner">
        <div v-if="photos.length>0" v-for="(photo,index) in photos" :class="getPhotoClasses(index)">
            <img :src="photo.image" class="d-block w-100" :alt="photo.name" data-bs-toggle="modal"
                :data-bs-target="'#photoModal-'+index">
            <div class="carousel-caption d-none d-md-block">
                <h5>{{photo.legend}}</h5>
            </div>

            <div class="modal fade" :id="'photoModal-'+index" :tabindex="index" aria-labelledby="photoModal"
                aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h1 class="modal-title fs-5" :id="'photoModalLabel-'+index">{{photo.legend}}</h1>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body" v-html="photo.description"></div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>

            
        </div>
        <div v-if="photos.length==0" class="carousel-item active">
            <img src="/media/assets/noImage.jpg" class="d-block w-100" alt="No image">
        </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carousel" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
</div>
    `
}