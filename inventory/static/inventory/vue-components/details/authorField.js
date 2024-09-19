
export default {
    props:["objectid"],
    data(){
        return {
            value:"",
            editingMode:false
        }
    },
    watch:{
        editingMode(newValue,oldValue){
            this.fetchData()
        }
    },
    methods:{
        async fetchData(){
            let objectRes=this.$root.objectData
            let author=objectRes.author
            this.value=author
            
        }
    },
    async mounted(){
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-label">Author</label>
    <input name="author" type="text" class="form-control" :value="value" :disabled="!editingMode" ></input>
    `
}