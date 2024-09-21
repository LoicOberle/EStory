export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.dating
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
     <p>Dating: {{value}}</p>
    `
}