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
let labels = ['Pizza 🍕', 'Taco 🌮', 'Hot Dog 🌭', 'Sushi 🍣'];
let colorHex = ['#FB3640', '#EFCA08', '#43AA8B', '#253D5B'];

let myChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [30, 10, 40, 20],
      backgroundColor: colorHex
    }],
    labels: labels
  },
  options: {
    responsive: true,
    legend: {
      position: 'bottom'
    },
    plugins: {
      datalabels: {
        color: '#fff',
        anchor: 'end',
        align: 'start',
        offset: -10,
        borderWidth: 2,
        borderColor: '#fff',
        borderRadius: 25,
        backgroundColor: (context) => {
          return context.dataset.backgroundColor;
        },
        font: {
          weight: 'bold',
          size: '10'
        },
        formatter: (value) => {
          return value + ' %';
        }
      }
    }
  }
})
