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
    
});


