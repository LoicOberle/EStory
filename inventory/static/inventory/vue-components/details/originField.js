
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
            let origin=objectRes.origin
            this.value=origin
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-label">Origin</label>
    <input name="origin" type="text" class="form-control" :value="value" :disabled="!editingMode" ></input>
    `
}