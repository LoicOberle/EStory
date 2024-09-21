export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.origin
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
    <p>Origin: {{value}}</p>
    `
}