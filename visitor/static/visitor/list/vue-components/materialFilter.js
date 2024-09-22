export default {
    data(){
        return {
            materials:[],
        }
    },
    methods:{
        async  fetchData(){
            let materialReq=await fetch("/member/inventory/material/all",{
                method:"GET",
                credentials: 'omit',
                
                headers:{
                    'X-Skip-Auth': 'true',
                    'Referer': window.location.origin,
                }
            })
            let materialRes=await materialReq.json()
            console.log(materialRes);
            this.materials=materialRes
            
        },
        updateMaterialFilterString(){
           
            let materialFilterCheckboxes=$(".materialFilterCheckbox")
            let filterString=""
            materialFilterCheckboxes.each((index,element)=>{
             
                if(element.checked){
                    filterString+="."+element.previousSibling.innerText+","
                }

            })
           
            filterString=filterString.slice(0,-1)
          
            this.$root.materialFilterString=filterString
            
        }
    },
    async mounted(){
        await this.fetchData()
    },
    template:`
       
        <div id="materialsFilters">
            <h4>Groups</h4>
            <div v-for="(material,index) in materials" v-if="materials.length>0" class="form-check form-switch">
                <label class="form-check-label" :for="'materialFilterChecbox-'+index">{{material.name}}</label>
                <input role="switch" @change="updateMaterialFilterString" type="checkbox" class="materialFilterCheckbox form-check-input" :id="'materialFilterChecbox-'+index"></input>
            </div>
        </div>
    `
}