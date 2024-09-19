
export default {
    props:["objectid"],
    data(){
        return {
            value:"",
            editingMode:false,
            photos:[]
        }
    },
    watch:{
        editingMode(newValue,oldValue){
           
        }
    },
    methods:{
     async sendChanges(e){
        e.preventDefault()
        $("form").dirty("setAsClean");
        const formData = new FormData(document.querySelector("form"));
           
            formData.delete("files")
        this.photos.forEach((img,index) => {
            formData.append(`files-${index}`, img.file);
        });
       
        
        await fetch(`/member/inventory/object/${this.objectid}/infos/save`, {
            method: 'POST',
            body: formData,
        })
        window.location.reload()

     
        },
        
    },
    mounted(){
       
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

        document.addEventListener("collectPhotos",(e)=>{
          
            this.photos=e.detail.photos
            
        })

       

    },

    template:`
   
    <button @click="sendChanges" class="btn btn-primary" :disabled="!editingMode" >Confirm changes</button>
    `
}