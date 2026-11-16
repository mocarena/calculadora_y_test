const operations = {
    sumar: (first, second) => first + second,
    restar: (first, second) => first - second,
    multiplicar: (first, second) => first * second,
    dividir: (first, second) => {
        if (second === 0) {
            throw new Error("No se puede dividir por cero");
        }
        return first / second;
    },
};

const firstInput = document.getElementById("numero1");
const secondInput = document.getElementById("numero2");
const result = document.getElementById("resultado");

function calculate(operation) {
    if (firstInput.value === "" || secondInput.value === "") {
        result.textContent = "Ingresá los dos números";
        return;
    }

    try {
        const first = Number(firstInput.value);
        const second = Number(secondInput.value);
        result.textContent = `Resultado: ${operations[operation](first, second)}`;
    } catch (error) {
        result.textContent = error.message;
    }
}

Object.keys(operations).forEach((operation) => {
    document.getElementById(operation).addEventListener("click", () => calculate(operation));
});
