document.getElementById('updateButton').addEventListener('click', function (event) {
    event.preventDefault();

    const selectedProduct = document.getElementById('productSelect').value;
    const productContainer = document.querySelector(`.image-container[data-product="${selectedProduct}"]`);

    if (!productContainer) return;

    const valueInput = document.getElementById('value').value || 'N/A';
    const quantityInput = document.getElementById('quantity').value || 'N/A';
    const weightInput = document.getElementById('weight').value || 'N/A';

    productContainer.querySelector(`td[id="${selectedProduct.toLowerCase()}-value"]`).textContent = "$" + valueInput;
    productContainer.querySelector(`td[id="${selectedProduct.toLowerCase()}-quantity"]`).textContent = quantityInput + "g";
    productContainer.querySelector(`td[id="${selectedProduct.toLowerCase()}-weight"]`).textContent = weightInput + "kg";
});

document.getElementById("calculateKnapsack").addEventListener('click', function (event) {
    console.log("Clicked");
    const valueInput = document.getElementById('value').value || 'N/A';
    const quantityInput = document.getElementById('quantity').value || 'N/A';
    const weightInput = document.getElementById('weight').value || 'N/A';

    const capacity = 850; // a constant for the knapsack capacity.
    const n = 50; // determines number of items in weights and values. 

    // define values as a list from 0 to valueInput in intervals of 5s.
    // const values = [];

    // for (let i = 0; i <= valueInput; i += 2) {
    //     values.push(i);
    // }

    // // define weights as a list from 0 to weightInput in intervals of 5s.
    // const weights = [];

    // for (let i = 0; i <= weightInput; i += 0.05) {
    //     weights.push(i);
    // }

    // // define quantities as a list from 0 to quantityInput in intervals of 1s.
    // const quantities = [];

    // for (let i = 0; i <= quantityInput; i += 0.05) {
    //     quantities.push(i);
    // }

    // const values = [10, 20, 30, 40];
    // const weights = [5, 10, 15, 20];
    // const quantities = [1, 2, 3, 4];

    // const values = [1680, 1440, 1840];
    // const weights = [0.265, 0.5, 0.441];
    const values = [
        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
        312
    ]; 
    // logs values size
    console.log(values.length);
    const weights = [
        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    ];
    const quantities = [0.41, 0.13, 0.29];
    const result = knapsack(values, weights, capacity, n);

    console.log(document.getElementById('max-value').innerHTML);

    document.getElementById('max-value').innerHTML = result;
    const selectedProduct = document.getElementById('productSelect').value;
    const productContainer = document.querySelector(`.image-container[data-product="${selectedProduct}"]`);
    // console.log(productContainer.outerHTML);
    document.getElementById('selected-items').innerHTML = productContainer.getAttribute("data-product"); // Assigning the outerHTML to get the element and its content.
});

// A basic Dynamic Programming based solution for 0-1 Knapsack problem
function knapsack(values, weights, capacity, n, precision = 100) {
    // Scale the weights and capacity to convert problem to integer knapsack
    let scaledWeights = weights.map(w => Math.round(w * precision));
    let scaledCapacity = Math.round(capacity * precision);

    let K = Array(n + 1).fill().map(() => Array(scaledCapacity + 1).fill(0));

    // Build table K[][] in bottom up manner
    for (let i = 0; i <= n; i++) {
        for (let w = 0; w <= scaledCapacity; w++) {
            if (i === 0 || w === 0) {
                K[i][w] = 0;
            } else if (scaledWeights[i - 1] <= w) {
                K[i][w] = Math.max(values[i - 1] + K[i - 1][w - scaledWeights[i - 1]], K[i - 1][w]);
            } else {
                K[i][w] = K[i - 1][w];
            }
        }
    }

    return K[n][scaledCapacity];
}


