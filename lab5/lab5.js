
// Variable block
//-----------------------------------------------

var canvas;
var context;
var canvasWidth = 800;
var canvasHeight = 800;
var clickX = new Array();
var clickY = new Array();
var locked = new Array();
var edge = [];
var paint = false;
var pointX = -1;
var pointY = -1;
var lastX = 0;
var lastY = 0;
var delay = false;
var cursorX;
var cursorY;
var currentColor = 0;
var minX = 2000;
var minY = 2000;
var maxX = 0;
var maxY = 0;

var Color = function() {
    this.r = this.g = this.b = 0;
};

Color.prototype.cssRGB = function() {
    return "rgb("+Math.round(this.r)+", "+Math.round(this.g)+", "+Math.round(this.b)+")";
};

Color.prototype.red = function() { return this.r; };
Color.prototype.green = function() { return this.g; };
Color.prototype.blue = function() { return this.b; };

Color.prototype.compare = function(other) {
	return (this.r == other.r) && (this.g == other.g) && (this.b == other.b);
}

Color.makeRGB = function() {
    var c = new Color();
    if(arguments.length < 3 || arguments.length > 4)
        throw new Error("error: 3 or 4 arguments");
    c.r = arguments[0];
    c.g = arguments[1];
    c.b = arguments[2];
    return c;
};

var colorOff = Color.makeRGB(255, 255, 255);
var colorOn = Color.makeRGB(0, 0, 0);
var colorBorder = Color.makeRGB(130, 100, 40);


//-----------------------------------------------
// Main block
//-----------------------------------------------

function prepareCanvas()
{
	canvas = document.getElementById("myCanvas");
 
	context = canvas.getContext("2d");

	context.imageSmoothingEnabled = false;

	init();

	var mouseIsDown = false;

	canvas.onmousedown = function(e){

		var rect = canvas.getBoundingClientRect();
	    var mouseX = e.clientX - rect.left;
		var mouseY = e.clientY - rect.top;

	    mouseIsDown = true;
	    addClick(mouseX, mouseY, false);
	}

	canvas.onmouseup = function(e){
	    mouseIsDown = false;
	}

	canvas.onmousemove = function(e){
	    cursorX = e.pageX;
	    cursorY = e.pageY;
	}

	setInterval(checkCursor, 100);
	function checkCursor(){
	    document.getElementById('currentPosition').innerHTML = 'Mouse position: ' + cursorX + ", " + cursorY;
	}

	$("#input-element-rect-color").change(function($this) {
	    var c = $(this).val();

	    var r = parseInt(c.substring(1, 3), 16);
	    var g = parseInt(c.substring(3, 5), 16);
	    var b = parseInt(c.substring(5, 7), 16);
	    colorOn = Color.makeRGB(r, g, b);
    });

    $("#input-element-background-color").change(function($this) {
	    var c = $(this).val();

	    var r = parseInt(c.substring(1, 3), 16);
	    var g = parseInt(c.substring(3, 5), 16);
	    var b = parseInt(c.substring(5, 7), 16);
	    colorOff = Color.makeRGB(r, g, b);
	    init();
	    redraw();
    });

}

function init()
{
	let oldStyle = context.fillStyle;
	context.fillStyle = colorOff.cssRGB();
	context.fillRect(0, 0, canvasWidth, canvasHeight);
	context.fillStyle = oldStyle;
}

//-----------------------------------------------
// Button block
//-----------------------------------------------

function fill()
{
	fillEdgeAlgorithm();
}

function delayCheck(checkboxElem)
{
	if (checkboxElem.checked)
		delay = true;
	else
		delay = false;
}

function circuit()
{
	var i = clickX.length;
	if (clickX[i-1] != pointX || clickY[i-1] != pointY)
	{
		addClick(pointX, pointY, false);
		pointX = -1;
		pointY = -1;
		redraw();
	}
}

function addPoint()
{
	var x=document.getElementById("results").value;
	var y=document.getElementById("results2").value;

    results = parseFloat(x);
    if(results==null)
        results=0;
    results2 = parseFloat(y);
    if(results2==null)
        results2=10;
	addClick(results, results2, false);
}

function clearAll()
{
	document.location.reload(true);
}

//-----------------------------------------------
// Function block
//-----------------------------------------------

function addClick(x, y, dragging)
{
	checkForMinMax(x, y);
	clickX.push(x);
	clickY.push(y);
	if (pointX == -1 && pointY == -1)
	{
		locked.push(1);
		pointX = x;
		pointY = y;
	}
	else
	{
		buildEdge();
		locked.push(0);
	}
	redraw();
}

function checkForMinMax(x, y)
{
	if (x < minX)
		minX = x;
	if (y < minY)
		minY = y;
	if (x < maxX)
		maxX = x;
	if (y > maxY)
		maxX = y;
}
function buildEdge()
{
	var i = clickX.length;
	edge.push([clickX[i-1], clickY[i-1], clickX[i-2], clickY[i-2]]);
	//alert(edge[0][0]);
}

function clearCanvas()
{
	context.clearRect(0, 0, canvasWidth, canvasHeight);
}

//-----------------------------------------------
// Draw block
//-----------------------------------------------

function colorAtIndex(imageData, index)
{
	let color = Color.makeRGB(imageData.data[index], imageData.data[index + 1], imageData.data[index + 2]);
	return color;
}

var g_i, g_j;

function redrawScreen()
{
	var imageData = context.getImageData(0, 0, canvasWidth, canvasHeight);
	var l = Math.min(edge[g_j][0], edge[g_j][2]);
	var x = ((g_i - edge[g_j][1])*(edge[g_j][2] - edge[g_j][0])/(edge[g_j][3] - edge[g_j][1])) + edge[g_j][0];

	for (l; l < canvasWidth; l = l+1)
	{
		if (l > x)
		{
			var index = 4 * (l + g_i * canvasWidth);
			let color = colorAtIndex(imageData, index);
			if (color.compare(colorOn))
			{
				imageData.data[index] = colorOff.r;
				imageData.data[index + 1] = colorOff.g;
				imageData.data[index + 2] = colorOff.b;
				imageData.data[index + 3] = 255;
			}
			else
			{
				imageData.data[index] = colorOn.r;
				imageData.data[index + 1] = colorOn.g;
				imageData.data[index + 2] = colorOn.b;
				imageData.data[index + 3] = 255;
			}
		}
		// if (delay)
		// {
		// 	var delayInMilliseconds = 10000;
		// 	setTimeout(function() {
		// 		return;
		// 	}, delayInMilliseconds);
		// }
	}
	context.putImageData(imageData, 0, 0);
	redraw();

	g_i = g_i + 1;
	if (g_i >= Math.max(edge[g_j][1], edge[g_j][3])) {
		g_j = g_j + 1;
		g_i = Math.min(edge[g_j][1], edge[g_j][3]);;
		if (g_j < edge.length) {
			window.requestAnimationFrame(redrawScreen);
		} else {
			alert("Done!");
		}
	} else {
		window.requestAnimationFrame(redrawScreen);
	}
}

function fillEdgeAlgorithm()
{
	g_i = 0;
	g_j = 0;
	g_i = Math.min(edge[g_j][1], edge[g_j][3]);;
	window.requestAnimationFrame(redrawScreen);
}

function delay()
{
	var delayInMilliseconds = 5000; //1 second

	setTimeout(function() {
		return;
	}, delayInMilliseconds);
	return;
}

function redraw()
{
	//clearCanvas();
	let oldStyle = context.fillStyle;
	context.fillStyle = colorBorder.cssRGB();
	context.beginPath();
	var i;
	var j = clickX.length;
	context.moveTo(clickX[j-2],clickY[j-2]);
	for (i = 0; i < clickX.length; i++) {
		//context.fillRect(clickX[i], clickY[i], 2, 2);
		if (locked[i] == 1){
			context.moveTo(clickX[i], clickY[i]);
		}
		else{
			context.lineTo(clickX[i], clickY[i]);
		}
	}
	context.stroke();
	context.fillStyle = oldStyle;
}

//-----------------------------------------------