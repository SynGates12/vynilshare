
$(document).ready(function(){
    var proba;
    var prov;
    //borrar
    $('.clicat').click(function() {
        $(".amagat").hide();
        proba=$(this).closest(".item"); 
        $('.pesao').click(function(){
            $(".amagat").slideDown();
            $('.OK').click(function(){
                $(proba).remove();
            });
        });
    });
    //vendre
       $('.prova').click(function() {
        prov=$(this);
        proba=$(this).closest(".item"); 
        $('#YES').click(function(){
            $(proba).fadeTo( "slow" , 0.5, function() {
                // Animation complete.
            });
            $(prov).css("background-color", "red");
            $(prov).attr("disabled", true);
            $(proba).children('.clicat').hide();
            $(proba).find('a').bind('click', false);
        })
    });
});



