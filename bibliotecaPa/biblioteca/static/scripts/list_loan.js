$(document).ready(function() {
    $("#createLoan").click(function () {
        $(".fade-in-text").css("filter", "blur(5px)"); $("#createLoan").css("filter", "blur(5px)");
        $("#crearPrestecForm").css("display", "flex");
    });

    $("#closeLoanForm").click(function () {
        $("#crearPrestecForm").css("display", "none");
        $(".fade-in-text").css("filter", "blur(0)"); $("#createLoan").css("filter", "blur(0)");
        $("#crearPrestecForm")[0].reset();
    });

    $('#id_data_préstec').change(function() {
        var dataPréstec = new Date($(this).val());
        var minDate = new Date(dataPréstec.getTime() + 7 * 24 * 60 * 60 * 1000); // Añadir 7 días a la fecha de préstamo
        var formattedMinDate = minDate.toISOString().split('T')[0]; // Convertir a formato YYYY-MM-DD
        $('#id_data_retorn').attr('min', formattedMinDate).val("");;
    });

    $(".cambiarEstado").click(function () {
        var id = $(this).val();
        console.log(id);
        $.ajax({
            url: "/api/returnLoan/" + id,
            type: "GET",
            success: function (data) {
                location.reload();
            }
        });
    });
});