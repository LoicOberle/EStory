export default {
    props:["objectid"],
    data(){
        return {
            
        }
    },
    methods:{
        sendNewloan(){
            let id=this.objectid
            let datetime=$("#loan-datetime").val()
            let description=$("#loan-description").summernote('code');
          
            
            
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
      flatpickr("#startDate", {
        enableTime: false,
        
    });

    flatpickr("#endDate", {
        enableTime: false,
        
    });
       
        $('.loan-description').summernote({
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
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#newloanModal">
  Add loan
</button>

<!-- Modal -->
<div class="modal fade" id="newloanModal" tabindex="-1" aria-labelledby="newloanModalLabel" aria-hidden="true">
  <form :action="'/member/inventory/object/'+objectid+'/loans/save'" method="POST">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="newloanModalLabel">New loan</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
         <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
            <label for="startDate">Start date</label>
            <input class="form-control loan-datetime" name="startDate" id="startDate" placeholder="Enter start date of loan" ></input>
            <label for="endDate">End date</label>
            <input class="form-control loan-datetime" name="endDate" id="endDate" placeholder="Enter end date of loan"></input>
            <label for="ongoing">Ongoing</label>
            <input id="ongoing" type="checkbox" name="ongoing" ></input>
            <textarea name="description" class="loan-description"></textarea>
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