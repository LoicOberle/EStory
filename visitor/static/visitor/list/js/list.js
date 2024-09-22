import { createApp } from 'vue'

import objectList from 'objectlist'
import categoryFilter from 'categoryfilter'
import materialFilter from 'materialfilter'
import groupFilter from 'groupfilter'
import searchBar from 'searchbar'

const app = createApp({

    data() {
      return {
        isotope:null,
        categoryFilterString:"",
        materialFilterString:"",
        groupFilterString:"",
        mainFilterString:"",
        searchString:""

      }
    },
    watch:{
        categoryFilterString(){
            this.mainFilterString=this.createPossibilities(this.categoryFilterString,this.materialFilterString,this.groupFilterString)
            this.updateFilter()
        },
        materialFilterString(){
            this.mainFilterString=this.createPossibilities(this.categoryFilterString,this.materialFilterString,this.groupFilterString)
            this.updateFilter()
        },
        groupFilterString(){
            this.mainFilterString=this.createPossibilities(this.categoryFilterString,this.materialFilterString,this.groupFilterString)
            this.updateFilter()
        },
        searchString(){
            this.mainFilterString=this.createPossibilities(this.categoryFilterString,this.materialFilterString,this.groupFilterString)
         
            this.updateFilter()
        }
    },
    methods:{
        updateFilter(){
            let component=this
            this.isotope.isotope({ 
                //filter: this.mainFilterString,
               
                filter: function() {
                    let qsRegex = new RegExp(component.searchString, 'gi' );
                    
                    if($(this).is(component.mainFilterString) || component.mainFilterString==""){
                        return qsRegex ? $(this).find(".name").text().match( qsRegex ) : true;
                    }else{
                        return false
                    }
                
              } });
        },
        createPossibilities(a,b,c){
            // Split each string by commas to get individual selectors
            const aSelectors = a.split(',');
            const bSelectors = b.split(',');
            const cSelectors = c.split(',');
            
            // Initialize an array to store all combinations
            let combinations = [];

            // Triple nested loop to generate all combinations
            for (let i = 0; i < aSelectors.length; i++) {
                for (let j = 0; j < bSelectors.length; j++) {
                for (let k = 0; k < cSelectors.length; k++) {
                    // Create a combination string by concatenating selectors without spaces
                    combinations.push(`${aSelectors[i].trim()}${bSelectors[j].trim()}${cSelectors[k].trim()}`);
                }
                }
            }

            // Join all combinations into a single string, separated by commas
            return combinations.join(', ');
        },
        initIsotope(){
            
            
      // quick search regex
      var qsRegex;

      // init Isotope
      this.isotope = $('.grid').isotope({
        itemSelector: '.object-item',
        layoutMode: 'fitRows'
      });
     
      
     

        },
        refreshIsotope(){
          
            
            this.isotope.isotope('reloadItems') // Reload new DOM elements
            this.isotope.isotope();
        }
    },
    mounted() {
        // Initialize Isotope after the component is mounted
        let component=this
        this.$nextTick(() => {
            this.initIsotope();
            component.isotope.isotope('reloadItems')
            component.isotope.isotope();
          });
        
    
      },
      updated() {
        // Re-initialize or refresh Isotope whenever the component is updated
        this.$nextTick(() => {
          this.refreshIsotope();
        });
    }
  })

    app.component('objectlist', objectList);
    app.component('categoryfilter', categoryFilter);
    app.component('materialfilter', materialFilter);
    app.component('groupfilter', groupFilter);
    app.component('searchbar', searchBar);

    app.mount("#app")

