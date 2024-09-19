export default {
    props:["objectid"],
    data(){
        return {
            
        }
    },
    methods:{
        sendNewOperation(){
            let id=this.objectid
            let datetime=$("#operation-datetime").val()
            let description=$("#operation-description").summernote('code');
            console.log(id,datetime,description);
            
            
        },
        getCookie(name) {
          const value = `; ${document.cookie}`;
          const parts = value.split(`; ${name}=`);
          if (parts.length === 2) return parts.pop().split(';').shift();
      },
    },
    computed:{
      csrfToken(){
        return this.getCookie("csrftoken")
      }
    },
    mounted(){
        flatpickr("#operation-datetime", {
            enableTime: true,
            
        });
       
        $('#operation-description').summernote({
            toolbar: [
                // [groupName, [list of button]]
                ['style', ['bold', 'italic', 'underline', 'clear']],
                ['font', ['strikethrough', 'superscript', 'subscript']],
                ['fontsize', ['fontsize']],
                ['color', ['color']],
                ['para', ['ul', 'ol', 'paragraph']],
                ['height', ['height']]
              ],
            placeholder:"Enter description",
           
        });
    },
    template:`
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#newOperationModal">
  Add operation
</button>

<!-- Modal -->
<div class="modal fade" id="newOperationModal" tabindex="-1" aria-labelledby="newOperationModalLabel" aria-hidden="true">
  <form :action="'/member/inventory/object/'+objectid+'/operations/save'" method="POST">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="newOperationModalLabel">New operation</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
          <input class="form-control" name="datetime" id="operation-datetime" placeholder="Enter date and time of operation"></input>
          <textarea name="description" id="operation-description"></textarea>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="submit" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </form>
</div>

    
    `
}