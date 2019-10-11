var someVar = document.getElementById("chartPlaceHolder");
Highcharts.chart(someVar, {
    chart: {
        type: 'bar'
    },
    title: {
        text: 'UCSD Admission Statistics by Gender' 
    },
    subtitle: {
        text: 'The Number of applicants, number of admittances and number of enrollments at UCSD betweeen 2005 and 2018 by Gender'
    },
    xAxis: {
        categories: [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,
            2016, 2017, 2018],
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of People',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ''
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
    },
    credits: {
        enabled: false
    },
    series : [
        {
          name: 'Full-time Men Applied',
          data: [18147,
           19838,
           20566,
           21590,
           21725,
           22332,
           25097,
           28758,
           31992,
           34618,
           37009,
           39779,
           41583,
           45636]
        },
        {
          name: "Full-time Women Applied",
          data: [22371,
           23748,
           24507,
           25775,
           25321,
           25761,
           28351,
           32049,
           35408,
           38822,
           41047,
           44430,
           46845,
           52265]
          
        },
        {
           name: "Full-time Men Admitted",
           data: [7580,
              9210,
              8419,
              8517,
              7816,
              8365,
              8707,
              10917,
              11866,
              11758,
              12748,
              14103,
              13981,
              13781]
        },
        {
           name: "Full-time Women Admitted",
           data: [10311,
              12135,
              10759,
              11200,
              9863,
              9991,
              10269,
              12046,
              12966,
              12837,
              13761,
              16170,
              16231,
              15821]
        }
      ]
});