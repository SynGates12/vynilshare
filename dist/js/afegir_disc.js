$(document).ready(function(){
function mostrarImagen(input) {
         if (input.files && input.files[0]) {
<<<<<<< HEAD
        
          var reader = new FileReader();
          reader.onload = function (e) {
           $('#img-dsk').css('backgroundImage','url('+e.target.result+')');
=======
          var reader = new FileReader();
          reader.onload = function (e) {
           $('#img-usr').css('backgroundImage','url('+e.target.result+')');
>>>>>>> c613c034a3da29c1d2ea307672ac107224b450fd
          }
          reader.readAsDataURL(input.files[0]);
         }
    }

        $("#id_image").change(function(){
        mostrarImagen(this);
    });
})
