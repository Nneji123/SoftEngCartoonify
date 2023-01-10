function validateForm(form)
{
  if(checkConfirmPassword(form) && checkRestaurantId(form))
      return true;
  else
    return false
}

function checkConfirmPassword(form)
{
  const password = form.password.value;
  const confirmPassword = form.confirmPassword.value;

  if (password != confirmPassword) 
  {
    alert("Error! Password did not match.");
    return false;
  } else {
    return true;
  }
}

function checkRestaurantId(form)
{
  const restaurantId = parseInt(form.fieldRestaurant.value)

  if (restaurantId == 0) 
  {
    alert("Please, select a restaurant.");
    return false;
  } else {
    return true;
  }
}