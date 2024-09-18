
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
            
            $('#description').summernote({
                toolbar: [
                    // [groupName, [list of button]]
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough', 'superscript', 'subscript']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']]
                  ],
                placeholder:this.value==""?"Enter description":"",
                callbacks: {
                    onChange: function(contents, $editable) {
                        if(component.value!=$("#description").summernote('code')){
                            
                            $("form").dirty("setAsDirty")
                        }
                    }
                  }
               
            });
            $("#description").summernote('code', this.value);
            $('#description').summernote(this.editingMode?"enable":"disable")
        }
    },
    methods:{
        async fetchData(){
            let objectRes=this.$root.objectData
         
            
            let description=objectRes.description
            this.value=description
            
        },
        temp(e){
            e.preventDefault()
            
        }
    },
    mounted(){
      const component=this
     
        $(document).ready(function() {
            component.fetchData()
      
            document.addEventListener("toggleEditMode",(e)=>{
               
                component.editingMode=e.detail.editingMode
                
            })
            $("#description").html(component.value)
            $('#description').summernote({
                toolbar: [
                    // [groupName, [list of button]]
                    ['style', ['bold', 'italic', 'underline', 'clear']],
                    ['font', ['strikethrough', 'superscript', 'subscript']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']]
                  ],
                placeholder:component.value==""?"Enter description":"",
                callbacks: {
                    onChange: function(contents, $editable) {
                 
                        if(component.value!=$("#description").summernote('code')){
                            
                            $("form").dirty("setAsDirty")
                        }
                       
                    }
                  }
               
            });
           
            
            $("#description").summernote('code', component.value);
            $('#description').summernote(component.editingMode?"enable":"disable")
        });
       

    },
    template:`
    <label class="form-labels">Description</label>
    <textarea name="description" id="description" type="text" class="form-controls" ></textarea>
    `
}