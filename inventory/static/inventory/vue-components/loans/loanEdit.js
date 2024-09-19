export default {
    props:["loan","id"],
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
    },
    computed:{
      csrfToken(){
        return this.getCookie("csrftoken")
      }
    },
    mounted(){
       
        
       
       
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
        $('#loan-description-'+this.id).summernote("code",this.loan.description)

        flatpickr("#startDate-"+this.id, {
            enableTime: false,
            
        });

        flatpickr("#endDate-"+this.id, {
            enableTime: false,
            
        });
    },
    template:`
  <button type="button" class="btn btn-secondary" data-bs-toggle="modal" :data-bs-target="'#editLoanModal'+id">
  Edit
</button>

<!-- Modal -->
<div class="modal fade" :id="'editLoanModal'+id" tabindex="-1" :aria-labelledby="'editLoanModalLabel'+id" aria-hidden="true">
  <form :action="'/member/inventory/object/'+loan.inventoryObject.id+'/loans/edit'" method="POST">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" :id="'editLoanModalLabel'+id">Edit loan</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
            <input type="hidden" name="loanId" :value="loan.id"></input>
            <label :for="'startDate-'+id">Start date</label>
            <input class="form-control loan-datetime" name="startDate" :id="'startDate-'+id" placeholder="Enter start date of loan" :value="loan.startDate"></input>
            <label :for="'endDate-'+id">End date</label>
            <input class="form-control loan-datetime" name="endDate" :id="'endDate-'+id" placeholder="Enter end date of loan" :value="loan.endDate"></input>
            <label for="ongoing">Ongoing</label>
            <input id="ongoing" type="checkbox" name="ongoing" :checked="loan.ongoing"></input>  
            <textarea name="description" class="loan-description" :id="'loan-description-'+id" ></textarea>
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