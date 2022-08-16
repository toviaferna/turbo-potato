$(document).ready(function () {

    function checkMaquinaria($maquinaria) {
      let $detalleContainer = $maquinaria.closest("tr");
      let $maquinariaPrecio = $detalleContainer.find(".precio-ha");
      let $precioHa = $maquinaria.find('option:selected').attr('data-precio-ha');
      $maquinariaPrecio.val($precioHa);
    }

    $(document).on("change", "select[data-maquinaria-select]", function (event) {
      checkMaquinaria($(event.target))
    });

    function checkItem($item) {

      let $detalleContainer = $item.closest("tr");
      let $itemCosto = $detalleContainer.find(".item-costo");
      let $itemPorcentajeIva = $detalleContainer.find(".item-porcentaje-impuesto");
      let $precioCosto = $($item.find('option:selected').text()).data("costo");
      let $impuestoPorcentaje = $($item.find('option:selected').text()).data("tipoImpuestoPorcentaje")

      $itemCosto.val($precioCosto);
      $itemPorcentajeIva.val($impuestoPorcentaje);
    }

    $(document).on("change", "select[data-item-select]", function (event) {
      checkItem($(event.target))
    });

    $("#id_es_credito").change(function () {
      if ($(this).is(":checked")) {
        $(".None").removeClass("d-none");
      } else {
        $(".None").addClass("d-none");
      }
    });
    
  });