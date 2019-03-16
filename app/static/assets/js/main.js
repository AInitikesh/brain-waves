var tableApp = new Vue({
  el: '#tableApp',
  delimiters: ['[[',']]'],
  data: {
    rows: [],
    tradeDateFrom: "",
    tradeDateTo: "",
    settlDateFrom: "",
    settlDateTo: "",
    currency: "",
    picked: "",
    rate: "",
    page: 0
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
        $.getJSON( "/results", { status : this.picked, tradeFrom: this.tradeDateFrom, tradeTo: this.tradeDateTo, settlFrom : this.settlDateFrom, settlTo : this.settlDateTo, currency : this.currency , rate: this.rate,},function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
      },
      next: function(){
        this.page += 1
        tableApp.rows = []
        $.getJSON( "/results", { status : this.picked, tradeFrom: this.tradeDateFrom, tradeTo: this.tradeDateTo, settlFrom : this.settlDateFrom, settlTo : this.settlDateTo, currency : this.currency , rate: this.rate, page: this.page},function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
      },
      back: function() {
        if (this.page <= 0){
          return
        }
        this.page -= 1
        tableApp.rows = []
        $.getJSON( "/results", { status : this.picked, trade: this.tradeDate, settl : this.settlDate, currency : this.currency , rate: this.rate, page: this.page},function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
      },
      merge: function(id){
        $.getJSON( "/merge", { id : id},function( data ) {});
        tableApp.rows = []
        $.getJSON( "/results", { status : this.picked, trade: this.tradeDate, settl : this.settlDate, currency : this.currency , rate: this.rate, page: this.page},function( data ) {
          $.each( data, function( key, val ) {
            tableApp.rows.push( val);
          });
        });
      }
    }
})