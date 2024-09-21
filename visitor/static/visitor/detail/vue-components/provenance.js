export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.provenance
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
     <p>Provenance: {{value}}</p>
    `
}