
export default {
    props:["objectid"],
    data(){
        return {
            value:"",
            editingMode:false,
            summernote:null
        }
    },
    watch:{
        async editingMode(newValue,oldValue){
            await this.fetchData()
            
            $('#bibliography').summernote({
                toolbar: [
                    // [groupName, [list of button]]
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough', 'superscript', 'subscript']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']]
                  ],
                placeholder:this.value==""?"Enter bibliography":"",
                callbacks: {
                    onChange: function(contents, $editable) {
                    
                        if(component.value!=$("#bibliography").summernote('code')){
                            
                            $("form").dirty("setAsDirty")
                        }
                    }
                  }
               
            });
            $("#bibliography").summernote('code', this.value);
            $('#bibliography').summernote(this.editingMode?"enable":"disable")
            
        }
    },
    methods:{
        async fetchData(){
            let objectRes=this.$root.objectData
         
            
            let bibliography=objectRes.bibliography
            this.value=bibliography
            
        },
       
    },
    mounted(){
      const component=this
     
        $(document).ready(function() {
            component.fetchData()
      
            document.addEventListener("toggleEditMode",(e)=>{
               
                component.editingMode=e.detail.editingMode
                
            })
            $("#bibliography").html(component.value)
            $('#bibliography').summernote({
                toolbar: [
                    // [groupName, [list of button]]
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough', 'superscript', 'subscript']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']]
                  ],
                placeholder:component.value==""?"Enter bibliography":"",
                callbacks: {
                    onChange: function(contents, $editable) {

                        
                        if(component.value!=$("#bibliography").summernote('code')){
                            
                            $("form").dirty("setAsDirty")
                        }
                    }
                  }
               
            });
           
            
            $("#bibliography").summernote('code', component.value);
            $('#bibliography').summernote(component.editingMode?"enable":"disable")
        });
       

    },
    template:`
    <label class="form-labels">Bibliography</label>
    <textarea name="bibliography" id="bibliography" type="text" class="form-controls" ></textarea>
    `
}