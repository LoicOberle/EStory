
export default {
    props:["objectid"],
    data(){
        return {
            values:[],
            materials:[],
            editingMode:false,
            tagify:null
        }
    },
    watch:{
        async editingMode(newValue,oldValue){
            await this.fetchData()

            this.tagify.setReadonly(!this.editingMode);
            $("#materials").prop("value","")
            $("#materials").prop("value",this.values.map(a => a.name).join(","))
            
          
        }
    },
    methods:{
        async fetchData(){
            let objectRes=this.$root.objectData
       
            let objectMaterials=objectRes.materials
            
            this.values=objectMaterials

            let materialsReq=await fetch("/api/inventory/materials",{
                method:"GET"
            })
        
            
            let materialsRes=await materialsReq.json()
            
            
            let materials=materialsRes.data
            this.materials=materials

            
        }
    },
    async mounted(){
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

      
     
        
        var suggestions = this.materials.map(a => {return {"id":a.id,"value":a.name}})
        
        // Initialize Tagify
        var input = document.querySelector('#materials');
        this.tagify = new Tagify(input, {
    whitelist: suggestions,
    enforceWhitelist: false, // Allow adding new tags not in the whitelist
    dropdown: {
        enabled: 1, // Show suggestions after 1 character is typed
        maxItems: 5 // Limit the number of suggestions displayed
    },
  
            });
        
            this.tagify.setReadonly(!this.editingMode);
            $("#materials").prop("value",this.values.map(a => a.name).join(","))
    },
    computed:{
   
    },
    template:`
    <label class="form-labels">Materials</label>
    <input id="materials" name="materials" placeholder="Add materials..."/>
  
    `
}