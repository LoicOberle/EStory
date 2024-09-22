export default {
    data(){
        return {

        }
    },
    methods:{
        getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        },
        async createObject(inventoryId,nexStep){
          
            let newObjectReq = await fetch("/member/inventory/object/create",{
                method:"POST",
                body:JSON.stringify({
                    "inventoryId":inventoryId
                }),
                headers:{
                    'X-CSRFToken': this.getCookie("csrftoken") // Include the CSRF token in the header
                  }
            })
            let newObjectRes=await newObjectReq.json()
            let newObjectId=newObjectRes.id
            
            //What to do next
            switch (nexStep) {
                case 0: //Edit object noz
                    window.location.href=`/member/inventory/object/${newObjectId}/detail/`
                    break;
            
                case 1: //Edit object later
                    window.location.reload()
                    break;
            }
        },
        openNewObjectDialog(){
            Swal.fire({
                title: "Enter the inventory id of the new object",
                html: `
               <input type="text" class="form-control" id="newInventoryObjectId" ></input>
              `,
                showDenyButton: true,
                showCancelButton: true,
                confirmButtonText: "Create and edit now",
                denyButtonText: `Create and edit later`,
                cancelButtonText:"Cancel"
              }).then(async (result) => {
                /* Read more about isConfirmed, isDenied below */
                const popup = Swal.getPopup()
                let element=popup.querySelector("#newInventoryObjectId")
                
                if(element.value!=""){
                    if (result.isConfirmed) {
                        await this.createObject(element.value,0)
                    } else if (result.isDenied) {
                        await this.createObject(element.value,1)
                    }else if (result.isDismissed) {
                        
                      }
                }
              
              });
        }
    },
    template:`
    <button class="btn btn-primary" @click="openNewObjectDialog" >New Object</button>
    `
}