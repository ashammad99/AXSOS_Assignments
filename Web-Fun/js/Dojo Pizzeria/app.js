function pizzaOven(crustType, sauceType, cheeses, toppings) {
    let pizza = {};

    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;

    return pizza;
}

let pizza1 = pizzaOven(
    "deep dish",
    "traditional",
    ["mozzarella"],
    ["pepperoni", "sausage"]
);
let pizza2 = pizzaOven(
    "hand tossed",
    "marinara",
    ["mozzarella", "feta"],
    ["mushrooms", "olives", "onions"]
);
let pizza3 = pizzaOven(
    "thin crust",
    "pesto",
    ["mozzarella", "parmesan"],
    ["chicken"]
);

let pizza4 = pizzaOven(
    "stuffed crust",
    "bbq",
    ["cheddar"],
    ["onions", "peppers"]
);



console.log(pizza1);
console.log(pizza2);
console.log(pizza3);
console.log(pizza4);

let crusts = ["deep dish", "thin crust", "hand tossed", "stuffed crust"];
let sauces = ["traditional", "marinara", "pesto", "bbq"];
let cheeses = ["mozzarella", "cheddar", "feta", "parmesan"];
let toppings = ["pepperoni", "sausage", "mushrooms", "olives", "onions", "bacon", "peppers"];

function randomPizza() {
    let crust = crusts[Math.floor(Math.random() * crusts.length)];
    let sauce = sauces[Math.floor(Math.random() * sauces.length)];
    let cheese = [cheeses[Math.floor(Math.random() * cheeses.length)]];
    let topping = [toppings[Math.floor(Math.random() * toppings.length)]];

    return pizzaOven(crust, sauce, cheese, topping);
}

console.log(randomPizza());
console.log(randomPizza());