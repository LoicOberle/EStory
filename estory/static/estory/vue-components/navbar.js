export default {
    props:["title"],
    data(){
        return {

        }
    },
    methods:{
        async logout(){
            let logoutReq=await fetch("/auth/logout/",{
                method:"POST",
                headers:{
                  'X-CSRFToken': this.getCookie("csrftoken") // Include the CSRF token in the header
                }
              })
        
              
              window.location.href="/"
        },
        getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        },
       
    },
    template:`
    <nav class="navbar bg-body-tertiary ">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">Estory</a>
      <a class="navbar-brand" href="/">{{title}}</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/member">Dashboard</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/member/inventory">Inventory</a>
            </li>
            <li class="nav-item">
                <button @click="logout"  class="nav-link">Log out</button>
              </li>
            
          </ul>
          
        </div>
      </div>
    </div>
  </nav>
    `
}