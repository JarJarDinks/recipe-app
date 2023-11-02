document.addEventListener('DOMContentLoaded', function () {
  const dropdownButton = document.getElementById('dropdownMenuButton');
  const dropdownMenu = document.querySelector('.dropdown-menu');
  const detailsButtons = document.querySelectorAll('.details-button');

  detailsButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      if (button) {
        const recipeUrl = button.getAttribute('data-recipe-url');
        if (recipeUrl) {
          window.location.href = recipeUrl;
        } else {
          console.error('data-recipe-url attribute not found on the button.');
        }
      } else {
        console.error('Button element not found.');
      }
    });
  });

  // Add click event to the custom button to show/hide the dropdown
  dropdownButton.addEventListener('click', () => {
    if (dropdownMenu.style.display === 'block') {
      dropdownMenu.style.display = 'none';
    } else {
      dropdownMenu.style.display = 'block';
    }
  });

  // Add click event to the document to hide the dropdown when the user clicks outside of it
  document.addEventListener('click', (e) => {
    if (e.target.id !== 'dropdownMenuButton') {
      dropdownMenu.style.display = 'none';
    }
  });
});
