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
    
    // Notifications
    function popUp(mensaje, tipo) {
        $('#popUp').prepend('<div class="alert alert-' + tipo + ' alert-dismissible fade show" role="alert">' + mensaje + '<button class="remove-item-btn">X</button></div>');
        $('.remove-item-btn').on('click', function () {
            $(this).closest('div').remove();
        });
    }



});