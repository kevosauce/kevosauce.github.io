var width = 20;
var height = 20;
var stepTime = 200;
var board = ["1"];
var rule = {"111":"0", "110":"1", "101":"1", "100":"0", "011":"1", "010":"1", "001":"1", "000":"0"}; 
var stopAfter = 300;

function startGame() {
    myGameArea.start();
}

var myGameArea = {
    canvas : document.createElement("canvas"),
    start : function() {
        this.canvas.width = 1000;
        this.canvas.height = 2000;
        this.context = this.canvas.getContext("2d");
        document.body.insertBefore(this.canvas, document.body.childNodes[0]);
        this.interval = setInterval(updateGameArea, stepTime);
    },
    clear : function() {
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    },
    iters : 0
}

function updateGameArea() {
    genNextRow();
    repaint();
    myGameArea.iters += 1;
    if (myGameArea.iters > stopAfter) {
        clearInterval(myGameArea.interval);
    }
}

function genNextRow() {
    var lastRow = "0" + board[board.length - 1];
    var newRow = "";
    for (idx = 0; idx < lastRow.length; idx++) {
        var triplet = (lastRow[idx - 1] || "0") + (lastRow[idx] || "0") + (lastRow[idx + 1] || "0");
        newRow += rule[triplet];
    };
    board.push(newRow);
}

function repaint() {
    ctx = myGameArea.context;
    for (row = 0; row < board.length; row++) {
	var len = board[row].length;
        for (col = 0; col < len; col++) {
	    var alive = board[row][col];
	    ctx.fillStyle = alive == "1" ? "black" : "white";
	    ctx.fillRect((len - col - 1) * width, row * height, width, height);
      }
   }
}

