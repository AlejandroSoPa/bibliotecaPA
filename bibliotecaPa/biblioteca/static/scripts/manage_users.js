$(document).ready(function () {

    $.ajax({
        url: '/api/getUsers/' + centreId,
        type: 'GET',
        success: function (response) {
            for (var i = 0; i < response.users.length; i++) {
                var item = response.users[i];
                console.log(item);
                var itemElement = $.parseHTML(`
                                                        <div class="card">
                                                            <div class="card-body">
                                                                <h5 class="card-title">${item.first_name} ${item.last_name}</h5>
                                                                <p class="card-text">${item.email}</p>
                                                                <p class="card-text">${item.username}</p>
                                                                <button id="modifyProfile" value="${item.id}">
                                                                    <a href="/edit_profile/${item.id}">Canviar dades</a>
                                                                </button>
                                                            </div>
                                                        </div>`
                );

                $('#showUsers').append(itemElement);
            }
        }
    });

});
