$(function () {

var acc = document.getElementsByClassName("cart_expand");

var i;



for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
    // this.parentElement.style.backgroundColor = '#f5f5f5';
    

        var up = this.getElementsByClassName('up');
        var down = this.getElementsByClassName('down');

        console.log(up[0]);

        var panel = this.parentElement.nextElementSibling;


        if (panel.style.display === "block") {
            panel.style.display = "none";
            up[0].style.display = "none";
            down[0].style.display = "block";
            this.parentElement.classList.add("hover");
        
        } else {
            panel.style.display = "block";
            up[0].style.display = "block";
            down[0].style.display = "none";
            this.parentElement.classList.remove("hover");
        }
    });
    }

});

$(function () {
    const stars = document.getElementsByClassName('star');

        for (i = 0; i < stars.length; i++) {
            stars[i].addEventListener("click", function() {
                alert('hi')
        } 
    )}
});


//  $(function () {
//     var matches_body = $('#cart_league_body');

//     $('#content').on("click", function(event){

//         header = event.target;
        
//         if(header.className == 'cart_expand flex justify-between w-full'){
//             body = header.parentElement.nextElementSibling;

//             if(body.style.display === "block"){
//                 body.style.display = "none";
//             }

//             $('#content').on("click", function(event){

//                 if(body.style.display === "none"){
                    
//                     if(header.className == 'cart_expand flex justify-between w-full'){
                        
//                         body.style.display = "block";
//                     }  
//                 }

//             })
//         }
//     })    
// });



// Matches
// $(function () {
//     var matches_body = $('#cart_league_body');

//     $('#matches_arr_down').hide()

//     $('#cart_league_header').on("click", function(){
//         matches_body.slideToggle();

//         if( $('#matshes_arr_up').css('display') != 'none' )  { 
//             /*success*/ 
//             $('#matshes_arr_up').hide()
//             $('#matches_arr_down').show()
//             $('#cart_league_header').css('background-color', '#e5e7eb')
//         } 
//         else { 
//             /*does not have*/ 
//             $('#matshes_arr_up').show()
//             $('#matches_arr_down').hide()
//             $('#cart_league_header').css('background-color', '')
//         }

//     });
// });

 // Matches2
//  $(function () {
//     var matches_body = $('#cart_league_body2');

//     $('#matches_arr_down2').hide()

//     $('#cart_league_header2').on("click", function(){
//         matches_body.slideToggle();

//         if( $('#matshes_arr_up2').css('display') != 'none' )  { 
//             /*success*/ 
//             $('#matshes_arr_up2').hide()
//             $('#matches_arr_down2').show()
//             $('#cart_league_header2').css('background-color', '#e5e7eb')
//         } 
//         else { 
//             /*does not have*/ 
//             $('#matshes_arr_up2').show()
//             $('#matches_arr_down2').hide()
//             $('#cart_league_header2').css('background-color', '')
//         }

//     });
// });


// H2H
// $(function () {
//     var header = $('#h2h_header');
//     var table = $('#h2h_table');
//     var match_details = $('#h2h_match_details');

//     table.hide()

//     $('#h2h_arr_down').hide()

//     $('#h2h_header').on("click", function(){
//         table.slideToggle();

//         if( $('#h2h_arr_up').css('display') != 'none' )  { 
//             /*success*/ 
//             $('#h2h_arr_up').hide()
//             $('#h2h_arr_down').show()
//         } 
//         else { 
//             /*does not have*/ 
//             $('#h2h_arr_up').show()
//             $('#h2h_arr_down').hide()
//         }
//     });

//     // header.on('click', function(){
//     //     if(match_details.hasClass('open') == true){
//     //         console.log('false')
//     //         match_details.removeClass('open')
//     //         table.hide()
//     //     }else{
//     //         match_details.addClass('open')
//     //         table.show()
//     //     }

//     // });
     
// });

// Standings
//  $(function () {
//     var st_body = $('#teams_standings_body');
//     st_body.hide()

//     $('#stat_arr_down').hide()

//     $('#teams_standings_header').on("click", function(){
//         st_body.slideToggle();

//         if( $('#stat_arr_up').css('display') != 'none' )  { 
//             /*success*/ 
//             $('#stat_arr_up').hide()
//             $('#stat_arr_down').show()
//         } 
//         else { 
//             /*does not have*/ 
//             $('#stat_arr_up').show()
//             $('#stat_arr_down').hide()
//         }
//     });

//  });