function validateForm(form)
{
  if(checkRestaurantId(form))
      return true;
  else
    return false
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