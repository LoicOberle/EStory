import loanEdit from "loanedit"

export default {
    components:{
        "loanedit":loanEdit
    },
    props:["objectid"],
    data(){
        return{
            loans:[]
        }
    },
    methods:{
        async fetchData(){
            let loanReq=await fetch(`/member/inventory/loan/${this.objectid}/all`,{
                method:"GET"
            })
            let loanRes=await loanReq.json()
            
            
            this.loans=loanRes
            
        },
        editLoan(loan){
           
            
        },
        endText(endDate,ongoing){
            let res=``
            if(ongoing){
                res=`<span class="badge text-bg-warning">Ongoing</span>`
            }else{
                res=endDate
            }
            return res
        },
        timeStampDate(date){
            let jsDate=new Date(Date.parse(date));
            return jsDate.getTime()
        },

    },
    async mounted(){
        await this.fetchData()
        let table = new DataTable('#loanList', {
            columns: [{ 
                searchable: false,
                "orderable": true
             }, { 
                searchable: true ,
                "orderable": false
            }, { 
                searchable: true,
                "orderable": false
             },
             { 
                searchable: true,
                "orderable": false
             }]
        });


    },

    template:`
        <table id="loanList">
        <thead>
            <tr>
                <th>Start</th>
                <th>End</th>
                <th>Description</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(loan,index) in loans">
                <td :data-order="timeStampDate(loan.startDate)" v-html="loan.startDate"></td>
                <td v-html="endText(loan.endDate,loan.ongoing)"></td>
                <td v-html="loan.description"></td>
                <td><loanedit :loan="loan" :id="index"></loanedit></td>
            </tr>
        </tbody>
    </table>
    `
}