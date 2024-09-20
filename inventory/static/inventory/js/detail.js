import { createApp } from 'vue'
import inventoryIdField from 'inventoryidfield'
import editSwitch from 'editswitch'
import confirmChangesButton from 'confirmChangesButton'
import nameField from "namefield"
import originField from "originfield"
import datingField from "datingfield"
import provenanceField from "provenancefield"
import reserveLocationField from "reservelocationfield"
import authorField from "authorfield"
import categoryField from "categoryfield"
import materialField from "materialfield"
import descriptionField from "descriptionfield"
import bibliographyField from "bibliographyfield"
import roomField from "roomfield"
import photoField from "photofield"
import fileField from "filefield"
import navbar from "navbar"
import operationList from 'operationlist'
import newoperation from "newoperation"
import loanList from 'loanlist'
import newloan from "newloan"
const app = createApp({
    delimiters: ["[[", "]]"],
    data() {
      return {
        objectid:$("#app").data("objectid"),
        objectData:null,
        loaded:false
      }
    },
    methods:{
        async fetchData(){
            
            let objectReq=await fetch("/api/inventory/object/"+this.objectid,{
                method:"GET"
            })
            let objectRes=await objectReq.json()
            
            
            this.objectData=objectRes
            this.loaded=true
            
        }
    },
    async created(){
       await this.fetchData()
    },
    async mounted(){
        

 

     
    }
  })

  //General components
  app.component('navbar',navbar)

  //Infos components
  app.component('inventoryidfield',inventoryIdField)
  app.component('namefield',nameField)
  app.component('originfield',originField)
  app.component('datingfield',datingField)
  app.component('provenancefield',provenanceField)
  app.component('reservelocationfield',reserveLocationField)
  app.component('authorfield',authorField)
  app.component('categoryfield',categoryField)
  app.component('materialfield',materialField)
  app.component('descriptionfield',descriptionField)
  app.component('bibliographyfield',bibliographyField)
  app.component('roomfield',roomField)
  app.component('photofield',photoField)
  app.component('filefield',fileField)
  app.component('editswitch',editSwitch)
  app.component('confirmchangesbutton',confirmChangesButton)

  //Operations components
  app.component('operationlist',operationList)
  app.component('newoperation',newoperation)

  //Loan components
  app.component('loanlist',loanList)
  app.component('newloan',newloan)

  app.mount("#app")

  $(document).ready(()=>{
 
    
    let form=$('form')
    form.dirty({
        preventLeaving: true,
        leavingMessage: "There are unsaved changes, do you want to continue ?"
    });
  
  })