
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
            let dating=objectRes.dating
            this.value=dating
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-labels">Dating</label>
    <input name="dating" type="text" class="form-controls" :value="value" :disabled="!editingMode" ></input>
    `
}