$(document).ready(function () {

    // Login
    /*
    $('#login-button').click(function () {
        var email = $('#username').val();
        var password = $('#password').val();
        emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
        if (password == '' || email == '') {
            popUp("Si us plau, ompli tots els camps", "error");
            return;
        } else if (!emailRegex.test(email)) {
            popUp("Si us plau, introdueixi un correu electrònic vàlid", "warning");
            return;
        }
        else {
            // Obtener el token CSRF de la cookie
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                url: 'http://localhost:8000/api/login/',
                type: 'POST',
                data: {
                    email: email,
                    password: password
                },
                
                success: function (response) {
                    console.log(response);
                    if (response == 'success') {
                        popUp("Sessió iniciada, redirigint", "success");
                        localStorage.setItem('email', email);
                        console.log("logged");
                    } else {
                        popUp("Correu electrònic o contrasenya incorrectes", "error");
                    }
                }
            });
        }
    });*/

    // Función para obtener el valor de una cookie por nombre
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Si la cookie comienza con el nombre especificado, obtenemos su valor
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

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
                zIndex: "2147483647"
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
                boxShadow: "0 3px 6px -1px rgba(0, 0, 0, .12), 0 10px 36px -4px rgba(77, 96, 232, .3)",
                background: "-webkit-linear-gradient(315deg, #73a5ff, #5477f5)",
                background: "linear-gradient(135deg, #ffec80, #ffda4d)",
                position: "fixed",
                opacity: "1",
                transition: "all .4s cubic-bezier(.215, .61, .355, 1)",
                borderRadius: "2px",
                cursor: "pointer",
                textDecoration: "none",
                maxWidth: "calc(50% - 20px)",
                zIndex: "2147483647"
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
                boxShadow: "0 3px 6px -1px rgba(0, 0, 0, .12), 0 10px 36px -4px rgba(77, 96, 232, .3)",
                background: "-webkit-linear-gradient(315deg, #73a5ff, #5477f5)",
                background: "linear-gradient(135deg, #ff4d4d, #ff0000)",
                position: "fixed",
                opacity: "1",
                transition: "all .4s cubic-bezier(.215, .61, .355, 1)",
                borderRadius: "2px",
                cursor: "pointer",
                textDecoration: "none",
                maxWidth: "calc(50% - 20px)",
                zIndex: "2147483647"
            };
                                    
            break;
            
    }

    $.ajax({
        url: 'notifications/',
        type: 'POST',
        data: {
            type: type,
            message: msg
        },
        success: function(response) {
            console.log('Notificación mostrada exitosamente');
        },
        error: function(xhr, errmsg, err) {
            console.log('Error al mostrar la notificación:', errmsg);
        }
    });

    if (data.status = "success") {
        Toastify({
            node: nodeElement[0],
            className: `notification ${type}`,
            close: true,
            duration: -1,
            style: style
        }).showToast();
    } else {
        console.log('Error al mostrar la notificación');
    }
}