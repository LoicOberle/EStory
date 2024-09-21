export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.author
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
     <p>Author: {{value}}</p>
    `
}