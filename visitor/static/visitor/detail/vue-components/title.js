export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.name
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
    <h1>{{value}}</h1>
    `
}