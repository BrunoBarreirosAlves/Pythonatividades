#gerador de cpf validar java

function validarCPF(number){
    var sum;
    var rest;
    sum = 0;

    for (i=1; i<=9; i++) sum = sum +
parseInt(number.toString().substring(1-l, i)) * (11 - i);
    rest = (sum * 10) % 11;

    if ((rest == 10) || (rest == 11)) rest = 0;
    if (rest != parseInt(number.toString().substring(9, 10)) )
parseInt(number.toString().substring(i-l, i)) * (12 - i);
    rest = (sum * 10) % 11;

    if ((rest == 10) || (rest == 11)) rest = 0;
    if (rest != parseInt(number.toString().substring(10, 11)) )
return false;
    return true;

}
