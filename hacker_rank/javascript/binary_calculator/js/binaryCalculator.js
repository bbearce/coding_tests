


var btn1 = document.getElementById('btn1').innerHTML 

function addNumbersAndOperands(e){
    /* Older IE browsers have a srcElement property,
    but other browsers have a 'target' property; 
    Set btn to whichever exists. */
    var btn = e.target || e.srcElement;
    
    /* Get the clicked element's innerHTML */
    document.getElementById('res').innerHTML = document.getElementById('res').innerHTML + btn.innerHTML;
}

function calculate(){
    const expression = document.getElementById('res').innerHTML;
    re_operands = /\d+/g
    re_operator = /[+]|[-]|[*]|[/]/
    const operands = expression.match(re_operands)
    const operator = expression.match(re_operator)[0]
    operand1 = parseInt(operands[0],2)
    operand2 = parseInt(operands[1],2)
    const finalExpression = String(operand1)+operator+String(operand2)
    answer_int = Math.floor(eval(finalExpression))
    answer_bin = (answer_int).toString(2)

    document.getElementById('res').innerHTML = answer_bin






}

function clear(){
    document.getElementById('res').innerHTML = ''
}

// clear
document.getElementById('btnClr').addEventListener('click', clear)

// append to <p id=res>
document.getElementById('btn0').addEventListener('click', addNumbersAndOperands)
document.getElementById('btn1').addEventListener('click', addNumbersAndOperands)
document.getElementById('btnSum').addEventListener('click', addNumbersAndOperands)
document.getElementById('btnSub').addEventListener('click', addNumbersAndOperands)
document.getElementById('btnMul').addEventListener('click', addNumbersAndOperands)
document.getElementById('btnDiv').addEventListener('click', addNumbersAndOperands)

// calculate answer
document.getElementById('btnEql').addEventListener('click', calculate)



