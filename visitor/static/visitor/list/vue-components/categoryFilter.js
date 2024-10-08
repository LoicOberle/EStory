export default {
    data(){
        return {
            categories:[],
        }
    },
    methods:{
        async  fetchData(){
            let categoryReq=await fetch("/api/categories",{
                method:"GET",
                credentials: 'omit'
            })
            let categoryRes=await categoryReq.json()
          
            this.categories=categoryRes.results
            
        },
        updateCategoryFilterString(){
           
            let categoryFilterCheckboxes=$(".categoryFilterCheckbox")
            let filterString=""
            categoryFilterCheckboxes.each((index,element)=>{
             
                if(element.checked){
                    filterString+="."+element.previousSibling.innerText+","
                }

            })
           
            filterString=filterString.slice(0,-1)
          
            this.$root.categoryFilterString=filterString
            
        }
    },
    async mounted(){
        await this.fetchData()
    },
    template:`
       
        <div id="categorieFilters" v-if="categories.length>0">
            <h4>Categories</h4>
            <div class="form-check form-switch" v-for="(category,index) in categories">
                <label class="form-check-label" :for="'categoryFilterChecbox-'+index">{{category.name}}</label>
                <input role="switch" @change="updateCategoryFilterString" type="checkbox" class="categoryFilterCheckbox form-check-input" :id="'categoryFilterChecbox-'+index"></input>
            </div>
        </div>
    `
}