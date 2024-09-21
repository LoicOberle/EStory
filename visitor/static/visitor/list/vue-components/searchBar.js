export default {
    data(){
        return {
            searchString:""
        }
    },
    watch:{
        searchString(){
           
            this.$root.searchString=this.searchString
            
        }
    },
    methods:{
        updateSearchString(){
       
            this.searchString=$("#searchBar").val()
           
        }
    },
    template:`
    <input id="searchBar" @input="updateSearchString" :value="searchString" placeholder="Search"></input>
    `
    
}