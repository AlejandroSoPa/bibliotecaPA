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
                                                                <p class="card-text">${item.username}</p><br>
                                                                <button class="card-text" value="${item.id}">
                                                                    <a href="/edit_profile/${item.id}" class="text-white bg-verde focus:ring-4 focus:outline-none font-medium rounded-lg text-sm px-4 py-2 text-center">Canviar dades</a>
                                                                </button>
                                                            </div>
                                                        </div>`
                );

                $('#showUsers').append(itemElement);
            }
        }
    });

});
