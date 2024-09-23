
import eventBus from 'eventBus';  // Adjust the path as needed




export default {
    props:["objectid"],
    data(){
        return {
            values:[],
            editingMode:false,
            imageCounter : 0,
            photos:[],
            legends:[],
            descriptions:[],
            thumbnail:-1
        }
    },
    watch:{
        editingMode(newValue,oldValue){
            this.fetchData()
        },
        photos(){
           
        }
    },
    methods:{
        async urlToFile(imageUrl) {
            const response = await fetch(imageUrl);
            const blob = await response.blob();
        
            // Convert Blob to Base64 using FileReader
            const base64Data = await new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.onerror = reject;
                reader.readAsDataURL(blob);
            });
        
            // Extract filename from URL
            const urlSegments = imageUrl.split('/');
            const filename = urlSegments[urlSegments.length - 1];  // Get the last part of the URL as filename
        
            // Create a File object with the Blob
            const file = new File([blob], filename, { type: blob.type });
        
            // Attach the Base64 string as a custom property to the File object
            file.base64 = base64Data;  // Now `file` contains both the file and its Base64 representation
        
            return file;
        },
        async fetchData(){
            this.photos=[]
            this.legends=[]
            this.descriptions=[]

            let objectRes=this.$root.objectData
            let photos=objectRes.photos
           
           for (let i = 0; i < photos.length; i++) {
            const photo = photos[i];
            
            
            let photoToStore=await this.urlToFile(photo.image)
           
            
            this.photos.push({
                file: photoToStore,          // Store the actual file object
                base64: photoToStore.base64,  // Optionally store the base64 data for preview
                viewable:photo.viewable
              })
            this.legends.push(photo.legend)
            this.descriptions.push(photo.description)
            if(photo.thumbnail){
                this.thumbnail=i
            }
            
           }
            this.values=photos
            
            
        },
        photoInputChange(event){
            $("form").dirty("setAsDirty")
            const files = event.target.files
            const component=this
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                
                
                const reader = new FileReader();
                reader.onload = function(e) {
                    
                    
                    component.photos.push({
                        file: file,          // Store the actual file object
                        base64: e.target.result,  // Optionally store the base64 data for preview
                        viewable:true
                      });
                    component.legends.push(file.name.split(".")[0])
                    component.descriptions.push("")
                    if(component.thumbnail==-1){
                        component.thumbnail=0
                    }
                    
                }
                reader.readAsDataURL(file);
               
            }
            event.target.value = '';

           
           
           
        },
        reloadTextareas(){
            $('.photo-description').summernote({
                toolbar: [
                    // [groupName, [list of button]]
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough', 'superscript', 'subscript']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']]
                  ],
                placeholder:this.value==""?"Enter photo description":"",
                callbacks: {
                    onChange: function(contents, $editable) {
                    
                        $("form").dirty("setAsDirty")
                    }
                  }
                  
            });
            $('.photo-description').summernote(this.editingMode?"enable":"disable")
        },
        reloadTextInputs(){
            $('.photo-legend').on("input",()=>{
             
                $("form").dirty("setAsDirty")
            })
        },
        reloadRadioButton(){
            $('.photo-thumbnail').on("change",()=>{
                
                $("form").dirty("setAsDirty")
            })
        },
        updatePhotoListButton(){
            const collectPhotosEvent = new CustomEvent('collectPhotos', {
                detail: { photos: this.photos } // Optional additional data
            });
            document.dispatchEvent(collectPhotosEvent)
        },
        deletePhoto(event,index){
           event.preventDefault()
           
            
            this.photos.splice(index,1)
            this.descriptions.splice(index,1)
            this.legends.splice(index,1)
            this.updatePhotoListButton()
            $("form").dirty("setAsDirty")
        
           
        }
    },
    updated(){
        this.reloadTextareas()
        this.reloadTextInputs()
        this.reloadRadioButton()

    },
    async mounted(){
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })
        
        

    },
    template:`
    <label class="form-label">Photos</label>
    <input @change="photoInputChange" type="file" id="photoInput" accept="image/*" multiple :disabled="!editingMode">
   
    <div id="photoList" class="overflow-y-scroll">
        
        <ul class="list-group">
            <li v-for="(photo , index) in photos"  class="list-group-item">
                <div class="row">
                    <div class="col-md-2">
                       <img :src="photo.base64" style="width:100px"></img>
                    </div>
                      <div class="col-md-2 col-form-label col-form-label">
                     
                    </div>
                    <div class="col-md-8">
                        <input :id="'photo-thumbnail-'+index" class="photo-thumbnail form-check-input" :value="index" type="radio" name="thumbnail" :checked="index==thumbnail" :disabled="!editingMode"></input>  
                        <div class="form-check form-switch">
                            <input :name="'photo-viewable-'+index" class="form-check-input" type="checkbox" role="switch" :id="'photo-viewable-'+index" :disabled="!editingMode"  :checked="photo.viewable">
                            <label class="form-check-label" :for="'photo-viewable-'+index" >Viewable</label>
                        </div> 
                        <input class="photo-legend form-control" type="text" :name="'photo-legend-'+index" :id="'photo-legend-'+index" :value="legends[index]" :disabled="!editingMode"/>
            
                    </div>
                </div>
            <div class="row">
                <div class="col-12">
                    <textarea class="photo-description" :name="'photo-description-'+index" :value="descriptions[index]"></textarea>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <button class="btn btn-danger" @click="(event) => deletePhoto(event,index)" :disabled="!editingMode">Delete</button>
                </div>
                
            </div>
            
           
            </li>
            {{updatePhotoListButton()}}
        
        </ul>
      
    </div>
      
  
    `
}