var tableApp = new Vue({
  el: '#tableApp',
  delimiters: ['[[',']]'],
  data: {
    rows: [],
    date: "",
    currency: "",
    picked: "",
  },
    created: function(){
        $.getJSON( "/results", function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
    },
    methods: {
      handleSearch: function(event){
        tableApp.rows = []
        $.getJSON( "/results", { status : this.picked },function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
      }
    }
})