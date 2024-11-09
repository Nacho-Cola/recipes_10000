document.getElementById('ingredient-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const ingredientInput = document.getElementById('ingredient-input').value;

  const requestData = {
    chat: ingredientInput  // Modify the key as per your server's expected structure
  };

  const url = "http://172.30.1.13:8888"
  // Show the loading spinner
  const loadingSpinner = document.getElementById('loading-spinner');
  loadingSpinner.style.display = 'block';

  // Make the first fetch request to get the recipe data
  fetch(url+'/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData)
  })
  .then(response => response.json())
  .then(recipeData => {
    // Populate the HTML elements with the received recipe data
    document.getElementById('recipe-title').textContent = recipeData.title || "No title provided";
    document.getElementById('recipe-summary').textContent = recipeData.summary || "No summary provided";

    // Clear and display ingredients
    const ingredientsList = document.getElementById('recipe-ingredients');
    ingredientsList.innerHTML = '';
    (recipeData.ingredients || []).forEach(ingredient => {
      const li = document.createElement('li');
      li.textContent = `${ingredient.name}: ${ingredient.ea}`;
      ingredientsList.appendChild(li);
    });

    // Clear and display steps
    const stepsList = document.getElementById('recipe-steps');
    stepsList.innerHTML = '';
    (recipeData.steps || []).forEach(step => {
      const li = document.createElement('li');
      li.textContent = step.step;
      stepsList.appendChild(li);
    });

    // Display tips
    document.getElementById('recipe-tips').textContent = recipeData.tips || "No tips provided";

    // Now make the second request to generate an image using title and summary
    return fetch(url+'/generate_img', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ img: `${recipeData.title}, ${recipeData.summary}` })
    }).then(response => response.json());
  })
  .then(imageData => {
    // Display the generated image
    if (imageData && imageData.image) {
      const imgElement = document.getElementById('generated-image');
      imgElement.src = imageData.image;
      imgElement.style.display = 'block';  // Make the image visible
    }

    // Make the recipe output visible
    document.getElementById('output-section').style.display = 'block';
  })
  .catch(error => {
    console.error('Error:', error);
    document.getElementById('recipe-output').textContent = 'An error occurred while fetching the recipe or image.';
  })
  .finally(() => {
    // Hide the loading spinner
    loadingSpinner.style.display = 'none';
  });
});
