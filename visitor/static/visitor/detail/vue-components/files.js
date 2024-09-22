export default {
    data(){
        return {
            values:[],
            fileContent:[]
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
            let object=this.$root.object
            this.values=object.files
           for (let i = 0; i < this.values.length; i++) {
            const element = this.values[i];
            this.fileContent.push(await this.determineFileType(element))
            
           }
        },
        async determineFileType(file){
            let fileToSee=await this.urlToFile(file.file)
           
            
            switch (fileToSee.type) {
                case "audio/wav":
                case "audio/mpeg":
                    return ` <audio controls src="${file.file}"></audio>`
                    break;
                case "video/webm":
                case "video/mp4":
                    return `<video controls width="400">
                            <source src="${file.file}" type="${fileToSee.type}" />
                            <p>
                               You browser can't read HTML5 videos. You can download it
                                <a href="${file.file}">here</a>.
                            </p>
                            </video>
                        `
                        break;
            
                default:
                    return `Not viewable file, <a href="${file.file}">download<a>`
                    break;
            }
           
        }
    },
    async mounted(){
        await this.fetchData()
    },
    template:`
    <div id="files">
        <ul>
            <li v-for="(file,index) in values" :id="'file-'+index">
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#fileModal-'+index">
                    {{file.name}}
                </button>

                <!-- Modal -->
                <div class="modal fade" :id="'fileModal-'+index" :tabindex="index" aria-labelledby="modal" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">{{file.name}}</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body" v-html="fileContent[index]">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>



            </li>
        </ul>
    </div>
    `
}