export default {
   props:{
    isuserconnected: {
        type: Boolean,
        default: false
      }
   },
      data() {
        return {
         isPopupVisible:false
        }
      },
      methods:{
        getCookie(name) {
          const value = `; ${document.cookie}`;
          const parts = value.split(`; ${name}=`);
          if (parts.length === 2) return parts.pop().split(';').shift();
      },
        redirectToLogin(){
          window.location.href="/auth/login"
        },
        async logout(){
            let logoutReq=await fetch("/auth/logout/",{
              method:"POST",
              headers:{
                'X-CSRFToken': this.getCookie("csrftoken") // Include the CSRF token in the header
              }
            })
            console.log(logoutReq);
            
            window.location.href="/"
            

        },
        togglepopup(){
          this.isPopupVisible=!this.isPopupVisible
          document.getElementsByClassName("userMenuPopup")[0]
        }
      },
      computed:{
        popupVisibility(){
          if (this.isPopupVisible) {
            return "visible"
          } else {
            return "hidden"
          }
        },
        popupOpacity(){
          if (this.isPopupVisible) {
            return 1
          } else {
            return 0
          }
        }
      },
      template: `
      <div class="userMenu">
        <button id="userMenuButton" @click="togglepopup" class=" rounded-circle btn btn-primary btn-lg"><i class="bi bi-person"></i></button>
        <div class="userMenuPopup" :style="{visibility:popupVisibility,
                                            opacity:popupOpacity}">
          <ul class="userMenuList">

            <li v-if="this.isuserconnected"><button @click="logout"  class="btn btn-primary">Log out</button></li>
            <li v-else><button @click="redirectToLogin" class="btn btn-primary">Log in</button></li>

          </ul>
        </div>
      </div>
    
     
        `
    }