export default {
    data(){
        return {
            groups:[],
        }
    },
    methods:{
        async  fetchData(){
            let groupReq=await fetch("/api/groups",{
                method:"GET",
                credentials: 'omit'
            })
            let groupRes=await groupReq.json()
            this.groups=groupRes.results
            
        },
        updateGroupFilterString(){
           
            let groupFilterCheckboxes=$(".groupFilterCheckbox")
            let filterString=""
            groupFilterCheckboxes.each((index,element)=>{
             
                if(element.checked){
                    filterString+="."+element.previousSibling.innerText+","
                }

            })
           
            filterString=filterString.slice(0,-1)
          
            this.$root.groupFilterString=filterString
            
        }
    },
    async mounted(){
        await this.fetchData()
    },
    template:`
       
        <div id="groupFilters" v-if="groups.length>0">
            <h4>Groups</h4>
            <div class="form-check form-switch" v-for="(group,index) in groups">
                <label class="form-check-label" :for="'groupFilterChecbox-'+index">{{group.name}}</label>
                <input role="switch" @change="updateGroupFilterString" type="checkbox" class="groupFilterCheckbox form-check-input" :id="'groupFilterChecbox-'+index"></input>
            </div>
        </div>
    `
}