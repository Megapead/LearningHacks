//
// // Chart js And for a doughnut chart
// const CHART = document.getElementById("doughnutChart");
// console.log(CHART);
// // var myDoughnutChart = new Chart(ctx, {
// //     type: 'doughnut',
// //     data: data,
// //     options: options
// // });
// let myDoughnutChart = new Chart(CHART, {
//     type: 'doughnut',
//     data: {
//         datasets: [{
//             data: [10, 20, 30]
//         }],
//         labels: [
//             'Red',
//             'Yellow',
//             'Blue'
//         ]
//     },
//     options: options
// });
let ctx = document.getElementById('doughnutChart').getContext('2d');
let labels = ['', 'Hot Dog 🌭'];
let colorHex = ['#e6e6e6','#43AA8B'];

let myChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [40,60],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: false,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: 'white',
        anchor: 'end',
        align: 'right',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 10,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '5'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})
