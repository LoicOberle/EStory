export default {
    props:["objectid"],
    data(){
        return {
            values:[]
        }
       
    },
    methods:{
        async fetchData(){
            let changesReq=await fetch(`/api/inventory/object/${this.objectid}/changes/inventoryId`,{
                method:"GET"
            })
            let changesRes=await changesReq.json()
            console.log(changesRes);
            this.values=changesRes
            
        },
        prettyDate(date){
           
            let jsDate=new Date(Date.parse(date));
          
            
            let res=``
            let display=jsDate.toLocaleString("en-GB")
            res=display
            return res
        },
    },
    async mounted(){
    
        
        await this.fetchData()
        let content=document.getElementById("inventoryIdChangeList")
        tippy('#inventoryIdChanges', {
            content: content.innerHTML,
            trigger: 'mouseenter focus click',
            allowHTML: true,
          });
    },
    template:`
    <span id="inventoryIdChanges"><i class="bi bi-clock-history"></i></span>
    <div  id="inventoryIdChangeList" style="display:none">
     <ul>
        <li v-for="value in values">
            {{prettyDate(value.modifiedAt)}} | {{value.oldValue}} -> {{value.newValue}} | {{value.modifiedBy.username}}
        </li>
    </ul>
    </div>
   
    `

}