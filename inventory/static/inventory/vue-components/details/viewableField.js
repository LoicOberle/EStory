
export default {
    props:["objectid"],
    data(){
        return {
            value:false,
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
          
            
            let viewable=objectRes.viewable
            this.value=viewable
          
            
        }
    },
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
        <div class="form-check form-switch">

            <input name="viewable" class="form-check-input" type="checkbox" role="switch" id="viewableField" :disabled="!editingMode"  :checked="value">
            <label class="form-check-label" for="viewableField" >Viewable</label>
        </div>
  
    `
}