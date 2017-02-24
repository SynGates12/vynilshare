$(document).ready(function(){
function mostrarImagen(input) {
         if (input.files && input.files[0]) {
        alert("HOLA")
          var reader = new FileReader();
          reader.onload = function (e) {
           $('#img-user').css('backgroundImage','url('+e.target.result+')');
          }
          reader.readAsDataURL(input.files[0]);
         }
    }

        $("#id_image").change(function(){
        mostrarImagen(this);
    });
})
