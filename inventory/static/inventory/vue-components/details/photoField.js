
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
            let objectReq=await fetch("/api/inventory/object/"+this.objectid,{
                method:"GET"
            })
            let objectRes=this.$root.objectData
            let photos=objectRes.photos
           
           for (let i = 0; i < photos.length; i++) {
            const photo = photos[i];
            let photoToStore=await this.urlToFile(photo.image)
           
            
            this.photos.push({
                file: photoToStore,          // Store the actual file object
                base64: photoToStore.base64  // Optionally store the base64 data for preview
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
                        base64: e.target.result  // Optionally store the base64 data for preview
                      });
                      component.legends.push("")
                      component.descriptions.push("")
                    
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
        deletePhoto(index){
           
            
            this.photos.splice(index,index)
            this.descriptions.splice(index,index)
            this.legends.splice(index,index)
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
    <label class="form-labels">Photos</label>
    <input @change="photoInputChange" type="file" id="photoInput" accept="image/*" multiple :disabled="!editingMode">
   
    <div id="photoList">
        
       <div v-for="(photo , index) in photos">
       <img :src="photo.base64" style="width:100px"></img>
       <input class="photo-thumbnail" :value="index" type="radio" name="thumbnail" :checked="index==thumbnail" :disabled="!editingMode"></input>
       <input class="photo-legend" type="text" :name="'photo-legend-'+index" :value="legends[index]" :disabled="!editingMode"/>
       <textarea class="photo-description" :name="'photo-description-'+index" :value="descriptions[index]"></textarea>
       <button @click="deletePhoto(index)">Delete</button>
       </div>
       {{updatePhotoListButton()}}
     
    </div>
      
  
    `
}