// mensajes de validación
var confirmacion = "Las contraseñas si coinciden";
var negacion = "No coinciden las contraseñas";
var vacio = "La contraseña no puede estar vacía";
var formato = "La contraseña debe contener minúsculas, mayúsculas, números, y debe ser de un mínimo de 8 carácteres";
var regexPass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;

function coincidePassword(valor, idSpan, esPass2) {

    // Obtengo el span
    var span = $('[id=' + idSpan + ']')[0];

    //muestro el span y borro cualquier clase que ya se haya seteado anteriormente
    //si no se cumple alguna condición, se agrega la clase "negación"
    //si cumple, se agrega la clase "confirmación"
    span.className = "";
    span.style.display = "block";
    span.textContent = "";

    //valido que contenga el formato correcto
    if (!regexPass.exec(valor)) {
        span.className = "negacion";
        span.textContent = formato;
        //agrego un return para que salga de la validación y no continúe validando
        return;
    }
    //valido si estoy en la segunda pass y si coincide con la primera
    if (esPass2 === true) {
        // Obtengo el valor de la pass1
        var pass1 = $('[id=txtPass1]')[0];
        if (esPass2 === true && valor !== pass1.value) {
            span.className = "negacion";
            span.textContent = negacion;
        } else {
            span.className = "confirmacion";
            span.textContent = confirmacion;
        }
    }
}