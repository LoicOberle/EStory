export default {
    data(){
        return {
            values:[]
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.values=object.categories
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
   <div>
   <span v-for="value in values" class="badge text-bg-secondary">{{value.name}}</span>
   </div>
    `
}