$(document).ready(function () {
    function getParameterByName(name) {
        name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
        var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
            results = regex.exec(location.search);
        return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
    }
    var search = getParameterByName('searchItems');

    $.ajax({
        url: '/api/searchItems/' + search,
        type: 'GET',
        success: function (response) {
            for (var i = 0; i < response.items.length; i++) {
                var item = response.items[i];
                // Verificar el valor del checkbox "disponible"
                if ($('#disponible').prop('checked')) {
                    // Si el checkbox está marcado (disponible == true) y el número de ejemplares es mayor que 1
                    if (item.ejemplares > 1) {
                        // Crear el elemento de la tarjeta y agregarlo a los resultados de búsqueda
                        var itemElement = $.parseHTML(`<div class="card">
                                                        <div class="card-body">
                                                            <h5 class="card-title">${item.titol}</h5>
                                                            <p class="card-text">${item.descripcio}</p>
                                                            <p class="card-text">${item.autor}</p>
                                                            <p class="card-text">${item.ejemplares}</p>
                                                        </div>
                                                    </div>`);
                        $('#searchResults').append(itemElement);
                    }
                } else {
                    // Si el checkbox no está marcado (disponible == false), mostrar todos los elementos
                    var itemElement = $.parseHTML(`<div class="card">
                                                    <div class="card-body">
                                                        <h5 class="card-title">${item.titol}</h5>
                                                        <p class="card-text">${item.descripcio}</p>
                                                        <p class="card-text">${item.autor}</p>
                                                        <p class="card-text">${item.ejemplares}</p>
                                                    </div>
                                                </div>`);
                    $('#searchResults').append(itemElement);
                }
            }
        }
    });

    // Search elements on index and search page
    $("#searchItems").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: '/api/searchItems/' + request.term,
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    var titles = data.items.map(function (item) {
                        return item.titol;
                    }).slice(0, 5); // Limita el array a los primeros 5 elementos
                    response(titles); // Devuelve solo los primeros 5 títulos como sugerencias de autocompletado
                },
                error: function (error) {
                    console.log(error);
                }
            });
        },
        minLength: 3 // La cantidad mínima de caracteres antes de que se muestren sugerencias
    });
});
