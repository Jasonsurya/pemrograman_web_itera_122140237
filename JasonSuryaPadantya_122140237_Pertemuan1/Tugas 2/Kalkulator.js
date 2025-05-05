function calculate(operation) {
    const num1 = parseFloat(document.getElementById("num1").value);
    const num2 = parseFloat(document.getElementById("num2").value);
    const outputDiv = document.getElementById("output");

    let result;

    if (isNaN(num1) || (["add", "subtract", "multiply", "divide", "power", "mod"].includes(operation) && isNaN(num2))) {
        outputDiv.textContent = "Masukkan angka yang valid.";
        return;
    }

    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            if (num2 === 0) {
                outputDiv.textContent = "Error: Tidak bisa dibagi 0!";
                return;
            }
            result = num1 / num2;
            break;
        case 'power':
            result = Math.pow(num1, num2);
            break;
        case 'sqrt':
            if (num1 < 0) {
                outputDiv.textContent = "Error: Akar dari bilangan negatif tidak valid!";
                return;
            }
            result = Math.sqrt(num1);
            break;
        case 'mod':
            result = num1 % num2;
            break;
        default:
            result = "Operasi tidak dikenali";
    }

    outputDiv.textContent = `Hasil: ${result}`;
}
