
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
            let provenance=objectRes.provenance
            this.value=provenance
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-labels">Provenance</label>
    <input name="provenance" type="text" class="form-controls" :value="value" :disabled="!editingMode" ></input>
    `
}