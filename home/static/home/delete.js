const APILink = 'http://127.0.0.1:8000/api/delete/';
const cards = document.getElementsByClassName('btn-danger');

for (let card of cards) {
    let id = card.id
    card.addEventListener(
        'click', (elem) => {
            fetch(APILink+id, {method: 'DELETE'})
                .then(() => {
                    let removingElement = document.getElementById(`rem`+id)
                    removingElement.remove()
                })
                .catch((error) => {
                    console.log(`failed: ${error}`)
                })
        }
    )
}