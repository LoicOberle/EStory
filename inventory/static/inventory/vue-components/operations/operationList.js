export default {

    data(){
        return{
            operations:[]
        }
    },
    props:["objectid"],
    methods:{
        async fetchData(){
            let operationReq=await fetch(`/member/inventory/operation/${this.objectid}/all`,{
                method:"GET"
            })
            let operationRes=await operationReq.json()
          
            
            this.operations=operationRes
            
        },
        prettyDate(date){
           
            let jsDate=new Date(Date.parse(date));
          
            
            let res=``
            let display=moment(jsDate).fromNow();
            res=jsDate.toLocaleString("fr-FR")
            return res
        },
        timeStampDate(date){
            let jsDate=new Date(Date.parse(date));
            return jsDate.getTime()
        }
    },
    async mounted(){
        await this.fetchData()
        let table = new DataTable('#operationList', {
            columns: [{ 
                searchable: false,
                "orderable": true
             }, { 
                searchable: true ,
                "orderable": false
            }, { 
                searchable: true,
                "orderable": false
             }]
        });
    

    },

    template:`
        <table id="operationList">
        <thead>
            <tr>
                <th>Date</th>
                <th>Description</th>
                <th>Author</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="operation in operations">
                <td :data-order="timeStampDate(operation.date)" v-html="prettyDate(operation.date)"></td>
                <td v-html="operation.description"></td>
                <td v-html="operation.author.username"></td>
            </tr>
        </tbody>
    </table>
    `
}