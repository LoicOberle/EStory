export default {
    data(){
        return {
            objects:[],
            ownership:[]
        }
    },
    methods:{
        async retrieveData(){
         
            let objectReq=await fetch("/api/inventory/objects",{
                method:"GET"
            })
            let objectRes=await objectReq.json()
        
            this.objects=objectRes.data
            this.ownership=objectRes.ownership
         
            
            
            
        },
        deleteObject(index){
            Swal.fire({
                title: "Are you sure?",
                text: "You won't be able to revert this!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Yes, delete it!"
              }).then(async (result) => {
                await fetch(`/api/inventory/object/${index}/delete`,{
                    method:"DELETE",
                    headers:{
                        'X-CSRFToken': this.getCookie("csrftoken") // Include the CSRF token in the header
                      }
                })
                if (result.isConfirmed) {
                  Swal.fire({
                    title: "Deleted!",
                    text: "Your object has been deleted.",
                    icon: "success"
                  }).then(()=>{
                    window.location.reload()
                  });
                }
              });
        },
        getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        },
    },
    async mounted(){
        await this.retrieveData()
        let table = new DataTable('#objectList', {
            responsive: true,
            searching: true
        });
    },
    template:`
    <table id="objectList">
        <thead>
            <tr>
                <th>Object</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(object,index) in objects" :key="object.id">
                <td>{{object.inventoryId}}</td>
                <td><a class="btn btn-info" :href="'/member/inventory/object/' + object.id + '/detail'">Details</a> <button @click="deleteObject(object.id)" class="btn btn-danger" :disabled="!ownership[index]" >Delete</button></td>
            </tr>
        </tbody>
    </table>


    `
}