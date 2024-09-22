
export default {
    props:["objectid"],
    data(){
        return {
            value:"",
            editingMode:false,
            photos:[],
            files:[]
        }
    },
  
    methods:{
     async sendChanges(e){
        e.preventDefault()
        $("form").dirty("setAsClean");
        const formData = new FormData(document.querySelector("form"));
  
           
            formData.delete("files")
        this.photos.forEach((img,index) => {
            formData.append(`photos-${index}`, img.file);
        });
        this.files.forEach((file,index) => {
            formData.append(`files-${index}`, file.file);
        });
       

        
        let postReq=await fetch(`/member/inventory/object/${this.objectid}/infos/save`, {
            method: 'POST',
            body: formData,
        })
        var notyf = new Notyf();
        if(postReq.status==200){
            notyf.success('Your changes have been successfully saved!');
        }else{
            console.error(postReq);
            
            notyf.error('An error occured !');
        }

     
        },
        
    },
    mounted(){
       
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

        document.addEventListener("collectPhotos",(e)=>{
          
            this.photos=e.detail.photos
            
        })
        document.addEventListener("collectFiles",(e)=>{
          
            this.files=e.detail.files
            
        })

       

    },

    template:`
   
    <button @click="sendChanges" class="btn btn-primary" :disabled="!editingMode" >Confirm changes</button>
    `
}