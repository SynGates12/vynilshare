
$(document).ready(function(){
    var proba;
    
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
        $('.prova').click(function() {
        proba=$(this).closest(".item"); 
        $('#YES').click(function(){
            $(proba).remove();
        })
    });
});



