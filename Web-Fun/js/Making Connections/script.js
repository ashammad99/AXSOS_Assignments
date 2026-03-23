
let count = document.querySelectorAll(".pending").length;
document.querySelector('.no-connection').innerText = count;
function editProfile() {
    event.preventDefault()
    var username = document.getElementById("username");
    username.innerText = "Linkedin User";
}

function rejectRequest(element) {
    //get the first parent of img,then parent of parent
    // element.parentElement.parentElement.remove();
    //or using closet function which return the first element has the given class's name as a parm
    element.closest(".card-list-item").remove();
    count--;
    document.querySelector('.no-connection').innerText = count;
}

function acceptRequest(element) {
    element.closest(".card-list-item").remove();
    count--;
    document.querySelector('.no-connection').innerText = count;

    let connection_count = parseInt(document.querySelector(".your-connections").innerText);
    // connection_count++;
    document.querySelector('.your-connections').innerText = ++connection_count;
}