$(document).ready(function(){
    $("#id_documento").blur(function(){
        if($.trim($(this).val()).length > 0){
            $.get("https://ruc.com.py/v2/getci/"+$(this).val(), function(data){
                if(data.result){
                    $("#id_razon_social").val(data.nombres+" "+data.apellidos)
                }
            });
        }
    });
});