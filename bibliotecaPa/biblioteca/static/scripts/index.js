//Directory: ProyectoBiblioteca/biblioteca/static/scripts/index.js

$(document).ready(function () {

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

    // Sign Out
    $("#signOut").click(function () {
        localStorage.removeItem('email');
        popUp("Sessió tancada, redirigint", "success");
        $('#changePassword').attr('disabled', true);
        $('#modifyProfile').attr('disabled', true);
        $('#signOut').attr('disabled', true);
        setTimeout(function () {
            window.location.href = 'index.html';
        }, 2000);
    });


    function checkboxChecked() {
        return $('#disponible').prop('checked');
    }

    // Evento de envío del formulario de búsqueda
    $('#searchForm').submit(function (event) {
        event.preventDefault(); // Evitar el envío del formulario por defecto
        
        var search = $('#searchItems').val(); // Obtener el término de búsqueda
        var disponible = checkboxChecked(); // Obtener el valor del checkbox
        localStorage.setItem('checkboxChecked', disponible);
        // Redirigir a la página de búsqueda con los parámetros en la URL
        window.location.href = '/search/?searchItems=' + search;
    });
});

function createNotification(type, msg) {
    let nodeElement = ""
    let style = ""
    switch (type) {
        case "info":
            nodeElement = $.parseHTML(`<div class="message">
                                        <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-info-circle"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0" /><path d="M12 9h.01" /><path d="M11 12h1v4h1" /></svg>
                                        <span>${msg}</span>
                                       </div>
            `)

            style = { 
                padding: "12px 20px",
                color: "#fff",
                display: "inline-block",
                boxShadow: "0 3px 6px -1px rgba(0, 0, 0, .12), 0 10px 36px -4px rgba(77, 96, 232, .3)",
                background: "-webkit-linear-gradient(315deg, #73a5ff, #5477f5)",
                background: "linear-gradient(135deg, #ff8080, #ff3333)",
                position: "fixed",
                opacity: "1",
                transition: "all .4s cubic-bezier(.215, .61, .355, 1)",
                borderRadius: "2px",
                cursor: "pointer",
                textDecoration: "none",
                maxWidth: "calc(50% - 20px)",
                zIndex: "2147483647",
                top: "35% !important",
                left: "64%"
            };

            break
        case "warning":
            nodeElement = $.parseHTML(`<div class="message">
                                        <svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-alert-triangle"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 9v4" /><path d="M10.363 3.591l-8.106 13.534a1.914 1.914 0 0 0 1.636 2.871h16.214a1.914 1.914 0 0 0 1.636 -2.87l-8.106 -13.536a1.914 1.914 0 0 0 -3.274 0z" /><path d="M12 16h.01" /></svg>
                                        <span>${msg}</span>
                                       </div>
            `)

            style = { 
                padding: "12px 20px",
                color: "#fff",
                display: "inline-block",
                boxShadow: "0 3px 6px -1px rgba(255, 235, 0, .12), 0 10px 36px -4px rgba(255, 255, 0, .3)",
                background: "-webkit-linear-gradient(315deg, #73a5ff, #5477f5)",
                background: "linear-gradient(135deg, #ffec80, #ffda4d)",
                color: "black",
                position: "fixed",
                opacity: "1",
                transition: "all .4s cubic-bezier(.215, .61, .355, 1)",
                borderRadius: "2px",
                cursor: "pointer",
                textDecoration: "none",
                maxWidth: "calc(50% - 20px)",
                zIndex: "2147483647",
                top: "35% !important",
                left: "64%"
            };
            
            break
        case "error":
            nodeElement = $.parseHTML(`<div class="message">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler icons-tabler-outline icon-tabler-alert-circle"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M3 12a9 9 0 1 0 18 0a9 9 0 0 0 -18 0" /><path d="M12 8v4" /><path d="M12 16h.01" /></svg>
                                            <span>${msg}</span>
                                            </div>`
            );
            style = {
                padding: "12px 20px",
                color: "#fff",
                display: "inline-block",
                boxShadow: "0 3px 6px -1px rgba(255, 71, 71, .12), 0 10px 36px -4px rgba(255, 99, 71, .3)",
                background: "-webkit-linear-gradient(315deg, #73a5ff, #5477f5)",
                background: "linear-gradient(135deg, #ff4d4d, #ff0000)",
                position: "fixed",
                opacity: "1",
                transition: "all .4s cubic-bezier(.215, .61, .355, 1)",
                borderRadius: "2px",
                cursor: "pointer",
                textDecoration: "none",
                maxWidth: "calc(50% - 20px)",
                zIndex: "2147483647",
                top: "35% !important",
                left: "64%"
            };
            
            break;
    }

    Toastify({
        node: nodeElement[0],
        className: `notification ${type}`,
        close: true,
        duration: -1,
        style: style
    }).showToast();

}
