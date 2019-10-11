var someVar = document.getElementById("chartPlaceHolder");
Highcharts.chart(someVar, {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'UCSD Admission Statistics for 2018 by Gender' 
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            },
            showInLegend: true
        }
    },
    series :[ {
        name: 'UCSD 2018 Admissions',
        colorByPoint: true,
        sliced: true,
        data: [
        {
           name: "Full-time Men Admitted",
           y: 13781
        },
        {
           name: "Full-time Women Admitted",
           y: 15821
        }]
    }]
});