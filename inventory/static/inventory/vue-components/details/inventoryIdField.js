
import inventoryIdChanges from "inventoryidchanges"
export default {
    props:["objectid"],
    components:{
        "inventoryidchanges":inventoryIdChanges
    },
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
    async mounted(){
     
        
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

    },
    template:`
    <label class="form-label">Inventory Id&nbsp; <inventoryidchanges :objectid="objectid"></inventoryidchanges></label>
    <input id="inventoryId" name="inventoryId" type="text" class="form-control" :value="value" :disabled="!editingMode" ></input>
    `
}