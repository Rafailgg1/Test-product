async function deleteTodo(id) {
    const response = await fetch(`/todos/${id}/`, {
          method: 'delete',
          headers: {
              'Content-Type': 'application/json'
      },

    });
    
    const data = await response.json();
  

  if (response.ok) {
    element.remove();
  }
  }
  
  
  
  
  document.querySelectorAll('.todo-list')
  function deleteFormListener(event) {
      
  
   const form = event.target;
   console.log(form);
  
   if(form.classList.contains('delete-todo-form')) {
      event.preventDefault();
  
      const todoElement = form.closest('.todo'); 
      
      deleteTodo(todoElement.dataset.id);
      }
    }
  
  const todoList = document.querySelector('.todo-list')
  todoList.addEventListener('submit', deleteFormListener);
  
  

function updateUrlDisplay() {
    const urlDisplay = document.getElementById('url-display');
    urlDisplay.textContent = window.location.pathname;
}


updateUrlDisplay();


window.addEventListener('popstate', updateUrlDisplay);
 
document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', function (e) {
            e.stopPropagation(); 
            this.querySelector('.dropdown-content').classList.toggle('show');
        });
    });

   
    window.addEventListener('click', function () {
        dropdowns.forEach(dropdown => {
            dropdown.querySelector('.dropdown-content').classList.remove('show');
        });
    });

   
    const currentUrl = window.location.pathname; 
    const navLinks = document.querySelectorAll('.nav__link, .dropdown-content a');

    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentUrl) {
            link.classList.add('active');
        }
    });


    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault(); 
            const url = this.getAttribute('href');


            history.pushState(null, null, url);


            navLinks.forEach(link => link.classList.remove('active'));
            this.classList.add('active');


            console.log(`Переход на ${url}`);
        });
    });
});