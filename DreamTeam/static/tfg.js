function cargarBase(){
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente1').replaceWith($("#id_suplente1",response)); })
    .fail(function() { alert("hello") })
}
function cargarEscolta(){
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente2').replaceWith($("#id_suplente2",response)); $('#id_suplente3').replaceWith($("#id_suplente3",response));$('#id_alero').replaceWith($("#id_alero",response)); })
    .fail(function() { alert("hello") })
}
function cargarAlero(){
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente3').replaceWith($("#id_suplente3",response));$('#id_suplente2').replaceWith($("#id_suplente2",response));$('#id_escolta').replaceWith($("#id_escolta",response)); })
    .fail(function() { alert("hello") })
}
function cargarAP(){
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente4').replaceWith($("#id_suplente4",response)); })
    .fail(function() { alert("hello") })
}
function cargarPivot(){
	
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente5').replaceWith($("#id_suplente5",response)); })
    .fail(function() { alert("hello") })
}

function cargarAleroSuplente(){
	var b=$('#id_base').val()
	if(b== null){
		b="-1"
	}
	var a=$('#id_escolta').val()
	if(a== null){
		a="-1"
	}
	var c=$('#id_alero').val()
	if(c== null){
		c="-1"
	}
	var d=$('#id_ap').val()
	if(d== null){
		d="-1"
	}
	var e=$('#id_pivot').val()
	if(e== null){
		e="-1"
	}
	var f=$('#id_suplente1').val()
	if(f== null){
		f="-1"
	}
	var g=$('#id_suplente2').val()
	if(g== null){
		g="-1"
	}
	var h=$('#id_suplente3').val()
	if(h== null){
		h="-1"
	}
	var i=$('#id_suplente4').val()
	if(i== null){
		i="-1"
	}
	var j=$('#id_suplente5').val()
	if(j== null){
		j="-1"
	}
	
	var jqxhr = $.ajax( "/suplente", {
        type: "POST", 
        data: {base:b,
        	escolta:a,
        	alero:c,
        	ap:d,
        	pivot:e,
        	s1:f,
        	s2:g,
        	s3:h,
        	s4:i,
        	s5:j,
        	
 		   csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()}
    })
    .done(function(response) { $('#id_suplente3').replaceWith($("#id_suplente3",response));$('#id_suplente2').replaceWith($("#id_suplente2",response));})
    .fail(function() { alert("hello") })
}



function abrir_modal(url)
{
        $('#popup').load(url, function()
        {
                $(this).modal('show');
        });
        return false;
}

function cerrar_modal(url)
{
	 $('#popup').load(url, function()
		        {
		                $(this).modal('hide');
		        });
		        return false;
}

function valid(){
	var cond = document.getElementById("cond").value;
	if(cond == 'vender'){
		return validVenta()
	}else{
	var valor = document.getElementById("id_valor");
	var valorReal= parseFloat(document.getElementById("id_valorReal").value);
	var valorV=parseFloat(valor.value);
	 if (valorV<valorReal) {
		 
		 document.getElementById("error-name").innerHTML="La puja no puede ser menor a su valor";
		 return false;
	  } else {
	    
	    return true;
	  }}
	
}
function validVenta(){
	var valor = document.getElementById("valor");
	var valorReal= parseFloat(document.getElementById("valor_jugador").value);
	var valorV=parseFloat(valor.value);
	 if (valorV<valorReal) {
		 
		 document.getElementById("error-name2").innerHTML="No se puede vender por menos de su valor";
		 return false;
	  } else {
	    
	    return true;
	  }
	
}

