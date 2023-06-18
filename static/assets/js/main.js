// League
$(function () {
    var body = $('#right_sidebar_body');

    $('#liga_arr_down').hide()

    $('#right_sidebar_header').on("click", function(){
        body.slideToggle();

        if( $('#liga_arr_up').css('display') != 'none' )  { 
            /*success*/ 
            $('#liga_arr_up').hide()
            $('#liga_arr_down').show()
        } 
        else { 
            /*does not have*/ 
            $('#liga_arr_up').show()
            $('#liga_arr_down').hide()
        }

    });
 });

 // Matches
$(function () {
    var matches_body = $('#cart_league_body');

    $('#matches_arr_down').hide()

    $('#cart_league_header').on("click", function(){
        matches_body.slideToggle();

        if( $('#matshes_arr_up').css('display') != 'none' )  { 
            /*success*/ 
            $('#matshes_arr_up').hide()
            $('#matches_arr_down').show()
            $('#cart_league_header').css('background-color', '#e5e7eb')
        } 
        else { 
            /*does not have*/ 
            $('#matshes_arr_up').show()
            $('#matches_arr_down').hide()
            $('#cart_league_header').css('background-color', '')
        }

    });
});

 // Matches2
 $(function () {
    var matches_body = $('#cart_league_body2');

    $('#matches_arr_down2').hide()

    $('#cart_league_header2').on("click", function(){
        matches_body.slideToggle();

        if( $('#matshes_arr_up2').css('display') != 'none' )  { 
            /*success*/ 
            $('#matshes_arr_up2').hide()
            $('#matches_arr_down2').show()
            $('#cart_league_header2').css('background-color', '#e5e7eb')
        } 
        else { 
            /*does not have*/ 
            $('#matshes_arr_up2').show()
            $('#matches_arr_down2').hide()
            $('#cart_league_header2').css('background-color', '')
        }

    });
});


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