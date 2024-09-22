
export default {
    props:["objectid"],
    data(){
        return {
            values:[],
            categories:[],
            editingMode:false,
            tagify:null
        }
    },
    watch:{
        async editingMode(newValue,oldValue){
            await this.fetchData()

            this.tagify.setReadonly(!this.editingMode);
            $("#categories").prop("value","")
            $("#categories").prop("value",this.values.map(a => a.name).join(","))
            
          
        }
    },
    methods:{
        async fetchData(){
            let objectRes=this.$root.objectData
       
            let objectCategories=objectRes.categories
            
            this.values=objectCategories

            let categoriesReq=await fetch("/member/inventory/category/all",{
                method:"GET"
            })
        
            
            let categoriesRes=await categoriesReq.json()
            
            
            let categories=categoriesRes
            this.categories=categories
            
        }
    },
    async mounted(){
        await this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
          
            this.editingMode=e.detail.editingMode
            
        })

      
     
        
        var suggestions = this.categories.map(a => {return {"id":a.id,"value":a.name}})
       
        // Initialize Tagify
        var input = document.querySelector('#categories');
        this.tagify = new Tagify(input, {
    whitelist: suggestions,
    enforceWhitelist: false, // Allow adding new tags not in the whitelist
    dropdown: {
        enabled: 1, // Show suggestions after 1 character is typed
        maxItems: 5 // Limit the number of suggestions displayed
    },
  
            });
        
            this.tagify.setReadonly(!this.editingMode);
            $("#categories").prop("value",this.values.map(a => a.name).join(","))
    },
    computed:{
   
    },
    template:`
    <label class="form-label">Categories</label>
    <input id="categories" name="categories" placeholder="Add categories..."/>
  
    `
}