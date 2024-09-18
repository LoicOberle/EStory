
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
            let inventoryId=objectRes.inventoryId
            this.value=inventoryId
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-labels">Inventory Id</label>
    <input name="inventoryId" type="text" class="form-controls" :value="value" :disabled="!editingMode" ></input>
    `
}