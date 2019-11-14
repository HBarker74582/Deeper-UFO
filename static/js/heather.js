console.log("hi");

function buildCharts() {

    d3.json(`/alien_data`).then(function (data) {
        console.log(data.sighting.date);

        var sighting = data.sighting.date;
        var place = data.state_short;
        var state = data.city_state;

        // @TODO: Build a Bubble Chart using the sample data
        var bubbleTrace = [{
            x: place,
            y: sighting,
            mode: "markers",
            text: state,
            marker: {
                size: 5,
                color: "ff4000"
            }
        }];

        var traceBubble = bubbleTrace;
        Plotly.newPlot("bubble", traceBubble);
    });
}
buildCharts();