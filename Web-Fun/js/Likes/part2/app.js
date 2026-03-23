function increaseLike(button) {
    //I put the button and likes span in the same div, then, using parent element, i access
    // to span  likes from parent div which contains span + button
    let likeSpan = button.parentElement.querySelector(".NoOfLikes");
    let count = parseInt(likeSpan.innerText);
    count++;
    likeSpan.innerText = count;
}