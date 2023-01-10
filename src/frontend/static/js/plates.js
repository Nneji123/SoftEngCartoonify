field_editPlateID  = document.getElementById('field_editPlateID')
field_editName     = document.getElementById('field_editName')
field_editCategory = document.getElementById('field_editCategory')
field_editPrice    = document.getElementById('field_editPrice')

function loadModalFieldsEditPanel(component){ 
    cells = component.parentNode.parentNode.cells;
    field_editPlateID.value  = cells[0].innerHTML;
    field_editName.value     = cells[1].innerHTML;
    field_editCategory.value = cells[2].innerHTML;
    field_editPrice.value    = cells[3].innerHTML;
}