# explain the purpose of the code

from pyscript import display, document

def ordering_form(e):
    document.getElementById("output").innerHTML=""

    # CHECKBOX & VALUES
    item1 = document.getElementById('food1')
    item2 = document.getElementById('food2')
    item3 = document.getElementById('food3')
    item4 = document.getElementById('food4')
    item5 = document.getElementById('food5')

    total = (float(item1.value) * item1.checked +
             float(item2.value) * item2.checked +
             float(item3.value) * item3.checked +
             float(item4.value) * item4.checked +
             float(item5.value) * item5.checked)

    display(f'Total amount is {total}', target='output')

    # Name, address, contact no.
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("cnumber").value
    

    message = f""" 👤 Order Form:
        Name    : {name}
        Address : {address}
        Number  : {number}
        """

    display(message, target="output")





















