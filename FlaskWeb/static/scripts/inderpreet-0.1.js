// Custom code for the updating functionality

// var refresh_time=0
// var myTimer

// /**
//  * @brief   Function to be called when the refresh_control is change in the page
//  * 
//  *          This function will start or stop the interval timer so as to 
//  *          allow ajax generation of the graph
//  */
// function refreshGraph(){
//     refresh_time = parseInt( document.getElementById('refresh_control').value )
//     // alert("Changed to " + document.getElementById('refresh_control').value/1000 + " Seconds");
//     if(refresh_time > 0){
//         clearInterval(myTimer)
//         myTimer = setInterval(function(){

//             console.log("Refresh")
//             /**
//              * Refresh for graph-1
//              */
//             $.ajax({
//                 url: "/graphs",
//                 type: "GET",
//                 contentType: 'application/json;charset=UTF-8',
//                 data: {
//                     'selected': document.getElementById('first_cat').value
//                 },
//                 dataType:"json",
//                 success: function (data) {
//                     Plotly.newPlot('graph-1', data );
//                 }
//             });  
        
//             /**
//              * Refresh for graph-2
//              */
//             $.ajax({
//                 url: "/graphs",
//                 type: "GET",
//                 contentType: 'application/json;charset=UTF-8',
//                 data: {
//                     'selected': document.getElementById('first_cat').value
//                 },
//                 dataType:"json",
//                 success: function (data) {
//                     Plotly.newPlot('graph-2', data );
//                 }
//             });

//         }, refresh_time)
//     } else {
//         clearInterval(myTimer)
//     }
// }

/**
 * @brief   Jquery Stuff
 */
$(document).ready(function(){

    //var socket = io.connect('http://127.0.0.1:5555');
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function(){
        socket.send('Page Connected!');
    });

    socket.on('message', function(msg){
        $("#light_status").text(decodeURI(msg));
    });

    $("#button_light1_on").click(function(){
        $.get("http://localhost:5555/api/rest/set/light/1/True")
    });

    $("#button_light1_off").click(function(){
        $.get("http://localhost:5555/api/rest/set/light/1/False")
    });

    $("#button_light2_on").click(function(){
        $.get("http://localhost:5555/api/rest/set/light/2/True")
    });

    $("#button_light2_off").click(function(){
        $.get("http://localhost:5555/api/rest/set/light/2/False")
    });

    // $('#refresh_cat').val(0);


    // $("#refresh_control").on('change', function(){
    //     refreshGraph()
        
    // })


    // $('#first_cat').on('change',function(){
    //     console.log('plot type changed')
    //     $.ajax({
    //         url: "/graphs",
    //         type: "GET",
    //         contentType: 'application/json;charset=UTF-8',
    //         data: {
    //             'selected': document.getElementById('first_cat').value
    //         },
    //         dataType:"json",
    //         success: function (data) {
    //             Plotly.newPlot('graph-1', data );
    //             Plotly.newPlot('graph-2', data );
    //         }
    //     });
    // })

    
});// end document.ready

