fieldPlateId = document.getElementById('fieldPlateId')
fieldPlateName = document.getElementById('fieldPlateName')
    
document.getElementById('radioPlateId').onclick = (e) => {
    fieldPlateId.disabled = false
    fieldPlateName.disabled = true
} 

document.getElementById('radioPlateName').onclick = (e) => {
    fieldPlateId.disabled = true
    fieldPlateName.disabled = false
}