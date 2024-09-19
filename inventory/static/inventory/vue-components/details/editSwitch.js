import eventBus from 'eventBus';  // Adjust the path as needed



export default {
    data(){
        return {
            editingMode:false
        }
    },
    methods:{
        toggleEditingMode(){
            this.editingMode=!this.editingMode
            
           
            
            if( $("form").dirty("isDirty")){
                Swal.fire({
                    title: "Are you sure?",
                    text: `There are unsaved changes, leaving the editing mode will reset values of the fields to their saved content.
                     Do you want to continue ?`,
                    icon: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#3085d6",
                    cancelButtonColor: "#d33",
                    confirmButtonText: "Yes"
                  }).then((result) => {
                  
                    
                    if (result.isConfirmed) {
                       
                        const toggleEditModeEvent = new CustomEvent('toggleEditMode', {
                            detail: { editingMode: this.editingMode } // Optional additional data
                        });
                        $("form").dirty("setAsClean");
                        document.dispatchEvent(toggleEditModeEvent)
                    }else if(result.isDismissed){
                        this.editingMode=true
                        $("#toggleEditingModeSwitch").prop( "checked", true );
                    }
                  });
            }else{
               
                        const toggleEditModeEvent = new CustomEvent('toggleEditMode', {
                            detail: { editingMode: this.editingMode } // Optional additional data
                        });
                        document.dispatchEvent(toggleEditModeEvent)
            }
       
            
            
            
        }
    },
    template:`
        <div class="form-check form-switch">

            <input  @change="toggleEditingMode" class="form-check-input" type="checkbox" role="switch" id="toggleEditingModeSwitch">
            <label class="form-check-label" for="toggleEditingModeSwitch">Enable editing mode</label>
        </div>
       
    `
}