
import eventBus from 'eventBus';  // Adjust the path as needed




export default {
    props:["objectid"],
    data(){
        return {
            values:[],
            editingMode:false,
            fileCounter : 0,
            files:[],
            names:[],
        }
    },
    watch:{
        editingMode(newValue,oldValue){
            this.fetchData()
        }
    },
    methods:{
        async urlToFile(fileUrl) {
            const response = await fetch(fileUrl);
            const blob = await response.blob();
        
            // Convert Blob to Base64 using FileReader
            const base64Data = await new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onloadend = () => resolve(reader.result);
                reader.onerror = reject;
                reader.readAsDataURL(blob);
            });
        
            // Extract filename from URL
            const urlSegments = fileUrl.split('/');
            const filename = urlSegments[urlSegments.length - 1];  // Get the last part of the URL as filename
        
            // Create a File object with the Blob
            const file = new File([blob], filename, { type: blob.type });
            const type= blob.type
            // Attach the Base64 string as a custom property to the File object
            file.base64 = base64Data;  // Now `file` contains both the file and its Base64 representation
            return file;
        },
        async fetchData(){
            this.files=[]
            this.names=[]

            let objectRes=this.$root.objectData
            let files=objectRes.files
           
           for (let i = 0; i < files.length; i++) {
            const file = files[i];
            
            
            let fileToStore=await this.urlToFile(file.file)
           
            
            this.files.push({
                file: fileToStore,          // Store the actual file object
                base64: fileToStore.base64, // Optionally store the base64 data for preview
                type:fileToStore.type
              })
            this.names.push(file.name)

            
           }
            this.values=files
            
            
        },
        fileInputChange(event){
            $("form").dirty("setAsDirty")
            const files = event.target.files
            const component=this
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                
                
                const reader = new FileReader();
                reader.onload = function(e) {
                    
                    
                    component.files.push({
                        file: file,          // Store the actual file object
                        base64: e.target.result,  // Optionally store the base64 data for preview
                        type: file.type
                      });
                    component.names.push(file.name.split(".")[0])

                    
                }
                reader.readAsDataURL(file);
               
            }
            event.target.value = '';

           
           
           
        },

        reloadTextInputs(){
            $('.file-name').on("input",()=>{
             
                $("form").dirty("setAsDirty")
            })
        },

        updateFileListButton(){
            const collectfilesEvent = new CustomEvent('collectFiles', {
                detail: { files: this.files } // Optional additional data
            });
            document.dispatchEvent(collectfilesEvent)
        },
        deleteFile(event,index){
           
            event.preventDefault()
            this.files.splice(index,1)
            this.names.splice(index,1)
            this.updateFileListButton()
            $("form").dirty("setAsDirty")
        },
        fileIcon(mimeType){
         
            
            switch (mimeType) {
                case "application/zip":
                    return `<i class="bi bi-file-earmark-zip"></i>`
                    break;
                case "application/pdf":
                    return `<i class="bi bi-file-earmark-pdf"></i>`
                    break
                case "application/msword":
                case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                case "application/vnd.oasis.opendocument.text":
                    return `<i class="bi bi-file-earmark-word"></i>`
                    break;
                case "application/vnd.oasis.opendocument.spreadsheet":
                case "application/vnd.ms-excel":
                case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    return `<i class="bi bi-file-earmark-excel"></i>`
                    break
                case "application/vnd.oasis.opendocument.presentation":
                case "application/vnd.ms-powerpoint":
                case "application/vnd.openxmlformats-officedocument.presentationml.presentation":
                    return `<i class="bi bi-file-earmark-powerpoint"></i>`
                    break;

                case "text/plain":
                    return `<i class="bi bi-filetype-txt"></i>`

                case "audio/mpeg":
                    return `<i class="bi bi-filetype-mp3"></i>`
                case "audio/wav":
                    return `<i class="bi bi-filetype-wav"></i>`
                case "video/mp4":
                    return `<i class="bi bi-filetype-mp4"></i>`
            
                default:
                    return `<i class="bi bi-file-earmark"></i>`
                    break;
            }
        }
    },
    updated(){
        this.reloadTextInputs()

    },
    async mounted(){
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })
        
        

    },
    template:`
    <label class="form-label">files</label>
    <input @change="fileInputChange" type="file" id="fileInput" accept="file/*" multiple :disabled="!editingMode">
   
    <div id="fileList" class="overflow-y-scroll">
        
        <ul class="list-group">
            <li v-for="(file , index) in files"  class="list-group-item">
                <div class="row">
                    <div class="col-md-2">
                       <a class="fileLink" :href="file.base64" v-html="fileIcon(file.type)"></a>
                    </div>
                      <div class="col-md-2 col-form-label col-form-label">
                        <label class="form-label" :for="'file-name-'+index">name</label>
                    </div>
                    <div class="col-md-8">
                        <input class="file-name form-control" type="text" :name="'file-name-'+index" :id="'file-name-'+index" :value="names[index]" :disabled="!editingMode"/>
            
                    </div>
                </div>

            <div class="row">
                <div class="col-12">
                    <button class="btn btn-danger" @click="(event) => deleteFile(event,index)" :disabled="!editingMode">Delete</button>
                </div>
                
            </div>
            
           
            </li>
            {{updateFileListButton()}}
        
        </ul>
      
    </div>
      
  
    `
}