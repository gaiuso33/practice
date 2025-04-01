document.addEventListener("DOMContentLoaded", loadExpenses);

function addExpense() {
    let name = document.getElementById("expense-name").value;
    let amount = document.getElementById("expense-amount").value;

    if (!name || !amount) return;

    let expenseList = document.getElementById("expense-list");
    let li = document.createElement("li");
    li.innerHTML = `${name} - $${amount} <button class="delete" onclick="deleteExpense(event)">X</button>`;
    expenseList.appendChild(li);

    saveExpense(name, amount);
    updateTotal();
}

function deleteExpense(event) {
    event.target.parentElement.remove();
    saveToLocalStorage();
    updateTotal();
}



function clearAllExpenses() {
    localStorage.removeItem("expenses");
    document.getElementById("expense-list").innerHTML = "";
    document.getElementById("total").textContent = "0";
}


function saveExpense(name, amount) {
    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    expenses.push({ name, amount });
    localStorage.setItem("expenses", JSON.stringify(expenses));
}

function loadExpenses() {
    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    let expenseList = document.getElementById("expense-list");
    
    expenses.forEach(expense => {
        let li = document.createElement("li");
        li.innerHTML = `${expense.name} - $${expense.amount} <button class="delete" onclick="deleteExpense(event)">X</button>`;
        expenseList.appendChild(li);
    });

    updateTotal();
}

function updateTotal() {
    let expenses = JSON.parse(localStorage.getItem("expenses")) || [];
    let total = expenses.reduce((sum, exp) => sum + parseFloat(exp.amount), 0);
    document.getElementById("total").textContent = total;
}
