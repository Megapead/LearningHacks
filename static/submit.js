//
// function getUrlVars() {
//     var vars = {};
//     var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
//         vars[key] = value;
//     });
//     return vars;
// }
// var percentage = getUrlVars()["result"];
// var percentage2 = 100 - percentage;
// // percentage wheel
// let ctx = document.getElementById('doughnutChart').getContext('2d');
// let labels = ['', 'resemblance'];
// let colorHex = ['#e6e6e6','#43AA8B'];
// let myChart = new Chart(ctx, {
//     type: 'doughnut',
//     data: {
//         datasets: [{
//             data: [percentage,percentage2],
//             backgroundColor: colorHex
//         }],
//         labels: labels
//     },
//     options: {
//         responsive: false,
//         hover: {
//             mode: 'index'
//         },
//         legend: {
//             position: ''
//         },
//         plugins: {
//             datalabels: {
//                 color: 'white',
//                 anchor: 'end',
//                 align: 'bottom',
//                 offset: 0,
//                 borderWidth: 2,
//                 borderColor: '#fff',
//                 borderRadius: 10,
//                 backgroundColor: (context) => {
//                     return context.dataset.backgroundColor;
//                 },
//                 font: {
//                     weight: 'bold',
//                     size: '10'
//                 },
//                 formatter: (value) => {
//                     return value + ' %';
//                 }
//             }
//         }
//     }
// })
