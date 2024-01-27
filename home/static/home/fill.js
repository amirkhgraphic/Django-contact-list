const SearchAPILink = 'http://127.0.0.1:8000/api/search/?first-name=';
const search = document.getElementById('search-input');


search.addEventListener(
    'input', () => {
    fetch(SearchAPILink + search.value.trim())
        .then((response) => response.json())
        .then((data) => {
            let container = document.getElementById('card-container');
            container.innerHTML = '';

            for (let item of data) {
                let cardDiv = document.createElement("div");
                cardDiv.className = "card";
                cardDiv.id = "rem" + item['id'];

                let cardBodyDiv = document.createElement("div");
                cardBodyDiv.className = "card-body";

                cardBodyDiv.innerHTML = `
                    <h5 class="card-title">${item['first_name']} ${item['last_name']}</h5>
                    <p class="card-text">${item['country']}, ${item['city']}, ${item['address']}</p>
                    <p>${item['country_code']} ${item['phone_number']}</p>
                    <p>${item['created_time']}</p>
                    <button class="btn btn-danger" id="${item['id']}">Close</button>`;

                let a = document.createElement('a');
                a.href = `/phone-list/${item['id']}/update/`;
                let button = document.createElement('button');
                button.className = 'btn btn-secondary';
                button.innerText = 'Edit';
                a.appendChild(button);
                cardBodyDiv.appendChild(a);

                cardDiv.appendChild(cardBodyDiv);

                container.appendChild(cardDiv);
            }
        })
        .catch((error) => {
            console.log(error)
        })
    }
);