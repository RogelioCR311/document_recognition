$(document).ready(function() {
    $('#id_identification').change(function() {
      $('#idForm').submit();
    });

    $('#id_curp').change(function() {
        $('#curpForm').submit();
      });

    $('#id_rfc').change(function() {
        $('#rfcForm').submit();
    });

    $('#id_acta').change(function() {
      $('#actaForm').submit();
    });

    $('#id_seguro').change(function() {
      $('#seguroForm').submit();
    });
  });