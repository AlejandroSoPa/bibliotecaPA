$(document).ready(function () {

    // Obtener el valor de 'searchItems' de la URL
    var search = localStorage.getItem('search') || '';
    // Función para realizar la llamada AJAX y mostrar los resultados
    console.log(localStorage.getItem('checkboxChecked'))
    console.log(search)
    $("#resultats").html("Resultats per a la cerca: " + search)
    if (search == null || search == '') {
        search = undefined
        $("#resultats").html("Resultats per a la cerca")
    }
    else {
        $("#resultats").html("Resultats per a la cerca: " + search)
    }
    function searchItems() {
        $.ajax({
            url: '/api/searchItems/' + search,
            type: 'GET',
            success: function (response) {
                for (var i = 0; i < response.items.length; i++) {
                    var item = response.items[i];
                    var checkboxChecked = $('#disponible').prop('checked') || JSON.parse(localStorage.getItem('checkboxChecked'));
                    // Obtener el valor del checkbox "disponible" dentro del bucle
                    console.log(checkboxChecked);
                    console.log(item);

                    // Verificar la disponibilidad del elemento y si debe mostrarse según el estado del checkbox
                    if (checkboxChecked) {
                        // Crear el elemento de la tarjeta y agregarlo a los resultados de búsqueda
                        if (item.ejemplares > 0) {
                            var itemElement = $.parseHTML(`<div class="card">
                                                <div class="card-body">
                                                    <h3 class="card-title">Titol: ${item.titol}</h5>
                                                    <p class="card-text">Autor: ${item.autor}</p>
                                                    <p class="card-text">Descripció: ${item.descripcio}</p>
                                                    <p class="card-text">Exemplars: ${item.ejemplares}</p>
                                                </div>
                                            </div>`);
                            $('#searchResults').append(itemElement);
                        }

                    } else if (!checkboxChecked) {
                        // Si el checkbox "disponible" no está marcado, mostrar todos los elementos
                        var itemElement = $.parseHTML(`<div class="card">
                                                <div class="card-body">
                                                    <h5 class="card-title">Titol: ${item.titol}</h5>
                                                    <p class="card-text">Autor: ${item.autor}</p>
                                                    <p class="card-text">Descripció: ${item.descripcio}</p>
                                                    <p class="card-text">Exemplars: ${item.ejemplares}</p>
                                                </div>
                                            </div>`);
                        $('#searchResults').append(itemElement);
                    }
                }
                // Borrar el elemento del localStorage después de usarlo
            }
        });
    }


    // Llamar a la función searchItems cuando el documento esté listo
    searchItems();

    // Manejar el evento de submit del formulario para realizar la búsqueda
    $(document).on('submit', '#searchElements', function (event) {
        // Prevenir el comportamiento predeterminado del evento de submit del formulario
        event.preventDefault();
        localStorage.removeItem('checkboxChecked');
        localStorage.removeItem('search');
        // Obtener el valor de 'searchItems' del input de búsqueda
        search = $('#searchItems').val();
        if (search == null || search == '') {
            search = undefined
            $("#resultats").html("Resultats per a la cerca")
        }
        else {
            $("#resultats").html("Resultats per a la cerca: " + search)
        }
        // Limpiar los resultados anteriores
        $('#searchResults').empty();

        // Llamar a la función searchItems con el nuevo término de búsqueda
        searchItems();
    });

    // Configurar el autocompletado para el input de búsqueda
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
