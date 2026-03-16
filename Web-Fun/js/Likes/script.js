var like_count_element = document.querySelector('.likes-count');
var likes_count = parseInt(like_count_element.innerText);

console.log(likes_count);
function like() {
    likes_count++;
    like_count_element.innerText = likes_count + " Like(s)";

    console.log(likes_count);
}