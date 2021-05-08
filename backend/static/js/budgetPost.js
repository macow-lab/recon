function addRow() {
    // Insert another columns row, with proper fields
    $("#budgetform").append(
        '<div class="columns"> \n ' +
        '<input type="hidden" name="id" value="new"> \n' +
        '<div class="column">\n' +
        '<label for="Amount"><b>Amount</b></label> \n' +
        '<input class="input amount" type="number" pattern="/^[0-9]*(.[0-9]{0,2})?$/" \n' +
        'title="Only positive numbers, with period (.) as a delimiter. Example: 100 or 100.25" id="amount" placeholder="Enter amount" required> \n' +
        "</div>\n" +
        '<div class="column select is-fullwidth"> \n' +
        '<label for="type"><b>Type</b></label> \n' +
        '<select id="type" required> \n' +
        '<option value="incomes" selected>Incomes</option> \n' +
        '<option value="expenses">Expenses</option> \n' +
        '<option value="investments">Investments</option> \n' +
        '<option value="savings">Savings</option> \n' +
        "</select> \n" +
        "</div> \n" +
        '<div class="column"> \n' +
        '<label for="category"><b>Category</b></label> \n' +
        '<input class="input category" type="text" id="category" placeholder="Enter category for item" required> \n' +
        "</div> \n" +
        '<div class="column">\n' +
        '<label for="category"><b>Delete Row</b></label>\n' +
        '<button class="button is-fullwidth is-danger delete-row" type="button" onclick="deleteRow()">Delete</button>\n' +
        "</div>\n" +
        "</div>\n"
    );
    // Slet nearest columns
}

function deleteRow() {
    $(document).on("click", ".delete-row", function (e) {
        e.preventDefault();
        $(this).closest(".columns").remove();
        return false;
    });
}

function postBudget() {
    $(document).on("click", ".post-budget", function (e) {
        e.preventDefault();
        // Validate .amount fields to ensure value is present
        var valueArr = [];
        document.querySelectorAll(".amount").forEach(function (el) {
            if (el.value == "") { return alert("Remember to fill out all fields!") }

            // Convert String in input to number, and set fraction digits
            var currentAmount = Number(el.value);
            el.value = currentAmount.toFixed(2)
            valueArr.push(currentAmount.toFixed(2));
        });

        document.querySelectorAll(".category").forEach(function (el) {
            if (el.value == "") { return alert("Remember to fill out all fields!") }});

        // TODO Create post
        fetch("/dash/budget/edit", {
            method: 'POST', // or 'PUT'
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
    });
}
