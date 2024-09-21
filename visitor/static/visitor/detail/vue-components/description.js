export default {
    data(){
        return {
            value:""
        }
    },
    methods:{
        fetchData(){
            let object=this.$root.object
            this.value=object.description
        }
    },
    mounted(){
        this.fetchData()
    },
    template:`
    <p v-html="value"></p>
    `
}