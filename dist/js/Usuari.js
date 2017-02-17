$(document).ready(function(){
    var proba;
    $('.clicat').click(function() {
        proba=$(this).closest(".item"); 
    })
    $('.okReservar').click(function(){
            var price = $(proba).closest('.viatge').attr('data-preu');
            var dte=$(proba).closest('.viatge').attr('data-dte');
            var calculdte = (price -(price * (dte/100)));
            var pais=$(proba).closest('.viatge').attr("data-pais");
            var pare=$(proba).closest('.viatge');
            var nom=$('#nomReserva').val();
            var gent= $('#numPersones').val();
            var dat = $('#dat').val();
            if ((pare).hasClass('soyguay')){
                   var li=$('<li class="well well-sm"><p><b>'+ pais + ': </b>reserva en nom de '+ nom + '<br>Nombre de persones: '+ gent +'<br>Preu Total:'+(gent*calculdte)  + ' € <br> Data: ' + dat +' </p></li>');
                   $('.reserves').append(li); 
              }else{
                    var li1=$('<li class="well well-sm"><p><b>'+ pais + ': </b>reserva en nom de '+ nom + '<br>Nombre de persones: '+ gent +'<br>Preu Total:'+( gent*price)  + ' € </p></li>');
                     $('.reserves').append(li1);
              }
      });
});