function addRow() {
    var form = document.getElementById('budgetform');
    form.innerHTML += '<div class="columns"> \n ' +
                        '<div class="column">\n' +
                        '<label for="Amount"><b>Amount</b></label>\n' +
                        '<input class="input" type="number" pattern="(0\,((0[1-9]{1})|([1-9]{1}([0-9]{1})?)))|(([1-9]+[0-9]*)(\, \n "+ "([0-9]{1,2}))?)" \n ' +
                        'title="Only positive numbers, with comma (,) as a delimiter" id="amount" placeholder="Enter amount - 0,00" required>' +
                        '</div>\n ' +
                        '<div class="column select is-fullwidth">\n' +
                        '<label for="type"><b>Type</b></label>\n' +
                        '<select id="type" required> \n' +
                        '<option value="incomes" selected>Incomes</option> \n' +
                        '<option value="expenses">Expenses</option>\n' +
                        '<option value="investments">Investments</option>\n' +
                        '<option value="savings">Savings</option>' +
                        '</select>\n' +
                        '</div>\n' +
                        '<div class="column">\n' +
                        '<label for="category"><b>Category</b></label>\n' +
                        '<input class="input" type="text" id="category" placeholder="Enter category for item" required>\n' +
                        '</div>\n ' +
                        '<div class="column">\n' +
                        '<label for="category"><b>Delete Row</b></label>\n' +
                        '<button class="button is-fullwidth is-danger">Delete</button>\n' +
                        '</div>\n' +
                        '</div>\n';
                
    // Slet nearest columns
                    }

