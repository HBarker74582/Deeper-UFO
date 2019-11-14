function displayToolTip() { 

    //set svg dimensions
    var svgWidth = 900;
    var svgHeight = 600;
    
    //set borders in svg
    var margin = {
        top: 10,
        right: 50,
        bottom: 150,
        left: 150
    };
    
    //Calculate chart width and height
    var width = svgWidth - margin.right - margin.left;
    var height = svgHeight - margin.top - margin.bottom;
    
    
    //append chart to the scatter id in html
    var chart = d3.select("#scatter").append("div").classed("chart", true);
    
    //append svg 
    var svg = chart.append("svg")
        .attr("width", svgWidth)
        .attr("height", svgHeight);
    
    //append group
    var chartGroup = svg.append("g")
        .attr("transform", `translate(${margin.left}, ${margin.top})`);
    
    
    var xLabelName = "State";
    var yLabelName = "Number of UFO sightings";
    
    // Read CSV
    d3.json("/sightings_Vs_marijuana").then(function(sightingsData) {
    
        // parse data
        sightingsData.forEach(function(data) {
          data.state_long = +data.state_long;
          data.sightings_total = +data.sightings_total;
        });
    
    
        // create scales
        var xScale = d3.scaleBand()
        .domain([d3.min(sightingsData, d => d.state_long) - 1, d3.max(sightingsData, d => d.state_long) + 2])
        .range([0, width])
        .padding(0.1);
    
        var yScale = d3.scaleLinear()
        .domain([d3.min(sightingsData, d => d.sightings_total) - 1, d3.max(sightingsData, d => d.sightings_total) + 2])
        .range([height, 0]);
    
        // create axes
        var xAxis = d3.axisBottom(xScale);
        var yAxis = d3.axisLeft(yScale);
    
        //append x axis
        chartGroup.append("g")
        .classed("x-axis", true)
        .attr("transform", `translate(0, ${height})`)
        .call(xAxis);
    
        //append y axis
        chartGroup.append("g")
        .classed("y-axis", true)
        .call(yAxis);
    
    
        // append circles to data points
        var circlesGroup = chartGroup.selectAll("circle")
        .data(sightingsData)
        .enter()
        .append("circle")
        .classed("stateCircle", true)
        .attr("cx", d => xScale(d.state_long))
        .attr("cy", d => yScale(d.sightings_total))
        .attr("opacity", ".75")
        .attr("r", "12");
    
        //append initial text
        chartGroup.selectAll(".stateText")
        .data(sightingsData)
        .enter()
        .append("text")
        .classed("stateText", true)
        .attr("x", d => xScale(d.state_long))
        .attr("y", d => yScale(d.sightings_total))
        .attr("dy", 3)
        .attr("font-size", "10px")
        .text(function(d){return d.state_short});
    
        //append label
        var xLabel = chartGroup.append("g")
        .attr("transform", `translate(${width / 2}, ${height + 20 + margin.top})`);
        
        //append label text
        xLabel.append("text")
        .attr("x", 0)
        .attr("y", 20)
        .attr("value", "state_long")
        .text("State");
        
        //append label
        var yLabel = chartGroup.append("g")
        .attr("transform", `translate(${0 - margin.left/4}, ${(height/1.5)})`);
    
        //append label text
        yLabel.append("text")
        .attr("x", 0)
        .attr("y", 0 - 20)
        .attr("transform", "rotate(-90)")
        .attr("value", "sightings_total")
        .text("Total Sightings");
    
        // Step 1: Initialize Tooltip
        var toolTip = d3.tip()
            .attr("class", "d3-tip")
            .offset([-8, 0])
            .html(function(d) {
            //console.log(`${d.state_long}`);
            //console.log(`${xLabelName} ${d.state_long}`);
            //console.log(`${yLabelName} ${d.sightings_total}`);
            return (`${d.state_long}<br>${xLabelName} ${d.state_long}% <br>${yLabelName} ${d.sightings_total}%`);
        });
    
        // Step 2: Create the tooltip in chartGroup.
        circlesGroup.call(toolTip);
    
        //add events
        circlesGroup.on("mouseover", function(d) {
            toolTip.show(d, this);
          })
          // Step 4: Create "mouseout" event listener to hide tooltip
            .on("mouseout", function(d) {
              toolTip.hide(d);
            });
         }).catch(function(error) {
               console.log(error);
        });
        
    }
    // When the browser loads, displayToolTip() is called.
    displayToolTip();
    
    