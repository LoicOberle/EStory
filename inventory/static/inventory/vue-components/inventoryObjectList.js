export default {
    data(){
        return {
            objects:[]
        }
    },
    methods:{
        async retrieveData(){
         
            let objectReq=await fetch("/api/inventory/objects",{
                method:"GET"
            })
            let objectRes=await objectReq.json()
        
            this.objects=objectRes.data
            
            
        }
    },
    mounted(){
        this.retrieveData()
    },
    template:`
    Inventory object list
    <ul>
    <li v-for="object in objects" :key="object.id">
        {{object.inventoryId}}
        <a :href="'/member/inventory/object/' + object.id + '/detail'" >Detail</a>
    </li>
    </ul>
    `
}