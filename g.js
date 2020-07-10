var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
var activeSs = SpreadsheetApp.getActiveSpreadsheet()
var activeCell = ss.getActiveCell();
var activeRow = ss.getActiveCell().getRow();
var currentCol = ss.getActiveCell().getColumn();

function onOpen() {

  // Menu functions
  var options = [
    {name:"Resize Image Column", functionName:"imageCellResize"},
  ];
    
    activeSs.addMenu("Inventory Options", options);
}

function imageCellResize() {
  ss.setRowHeight(i+1, 70);
}
