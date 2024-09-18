
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
            let reservelocation=objectRes.reservelocation
            this.value=reservelocation
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-labels">Reserve location</label>
    <input name="reservelocation" type="text" class="form-controls" :value="value" :disabled="!editingMode" ></input>
    `
}