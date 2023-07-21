
const nav = document.querySelector('.navbar');
document.querySelector('#menu-btn').onclick =()=>{
    nav.classList.toggle('active');
}

  
document.addEventListener('DOMContentLoaded', function() {
    const radiochoices = document.querySelectorAll('input[type="radio"][name="set"]');
  
    // Attach a change event listener to each radio button
    radiochoices.forEach(function(radio) {
      radio.addEventListener('change', function() {
        // Get the value of the selected radio button
        const selectedValue = this.value;
        
        // Get the elements by their IDs
        const secondside = document.getElementById('ssd');
        const desert = document.getElementById('ds');
        
        // Toggle the visibility of the elements based on the selected value
        if (selectedValue === "GOSET") {
          secondside.style.display = "block";
          desert.style.display = "block";
        } else if (selectedValue === "YONSET") {
          secondside.style.display = "block";
          desert.style.display = "none";
        } else {
          secondside.style.display = "none";
          desert.style.display = "none";
        }
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        const orderId = this.getAttribute('data-order-id');
        deleteOrder(orderId);
      });
    });

    function deleteOrder(orderId) {
      const csrfToken = getCookie('csrftoken'); // Function to get the CSRF token from cookies

      fetch(`/delete_order/${orderId}/`, {
        method: 'DELETE',
        headers: {
          'X-CSRFToken': csrfToken, // Include the CSRF token in the headers
        },
      })
      .then(response => {
        if (response.ok) {
          window.location.reload();
        } else {
          console.error('Failed to delete the order.');
        }
      })
      .catch(error => console.error('Error during the delete request:', error));
    }

    // Function to get the CSRF token from cookies
    function getCookie(name) {
      const value = `; ${document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
  });
}

