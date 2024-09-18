
export default {
    props:["objectid"],
    data(){
        return {
            value:"",
            originalValue:"",
            editingMode:false,
            rooms:[]
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
            let room=objectRes.room
         
            
            this.value=room==null?-1:room
            this.originalValue=room==null?-1:room

            let roomsReq=await fetch("/api/inventory/rooms",{
                method:"GET"
            })
            let roomsRes=await roomsReq.json()
            this.rooms=roomsRes.data
     

            $("#room").on("change",(e)=>{
              
                this.value=e.target.value
        
                
                if (this.value!=this.originalValue) {
                
                    $("form").trigger("dirty")
                   
                }
                
            })
            
            
        }
    },
   
    mounted(){
        this.fetchData()
      
        document.addEventListener("toggleEditMode",(e)=>{
           
            this.editingMode=e.detail.editingMode
            
        })

       

    },
    template:`
    <label class="form-labels">Room</label>
    <select id="room" name="room" class="form-controls" :value="value" :disabled="!editingMode" >
    <option v-for="room in rooms"  :value="room.id">{{room.name}}</option>
    </select>
    `
}