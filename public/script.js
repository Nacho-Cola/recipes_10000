document.getElementById('ingredient-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const ingredientInput = document.getElementById('ingredient-input').value;

  // 여기에서 AI에 재료를 보내고 JSON 레시피를 생성하는 로직을 추가하세요.
  // 임시로 예시 레시피를 생성합니다.
  const exampleRecipe = {
      title: "샘플 레시피",
      ingredients: [ingredientInput],
      instructions: "재료를 섞고 맛있게 드세요!"
  };

  // JSON 출력
  document.getElementById('recipe-output').textContent = JSON.stringify(exampleRecipe, null, 2);
});
