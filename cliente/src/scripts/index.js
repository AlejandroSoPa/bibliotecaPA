$(document).ready(function () {
    $('#login-button').click(function () {
        var email = $('#username').val();
        var password = $('#password').val();
        emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
        if (password == '' || email ==  '') {
            popUp("Si us plau, ompli tots els camps", "error");
            return;
        }   else if (!emailRegex.test(email)) {
            popUp("Si us plau, introdueixi un correu electrònic vàlid", "warning");
            return;
        }

         else {
            localStorage.setItem('email', email);
            popUp("Benvingut " + email + ", redirigint", "success");
            $('#login-button').attr('disabled', true);
            setTimeout(function () {
                window.location.href = 'dashboard.html';
            }, 2000);
        }
        var datos = {
            email: email,
            password: password
        };
        console.log(datos);
    });

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

    function popUp(mensaje, tipo) {
        $('#popUp').prepend('<div class="alert alert-' + tipo + ' alert-dismissible fade show" role="alert">' + mensaje + '<button class="remove-item-btn">X</button></div>');
        $('.remove-item-btn').on('click', function () {
            $(this).closest('div').remove();
        });
    }

});