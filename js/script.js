document.querySelectorAll('img').forEach(img => {
    console.log("runs")
    img.onerror = function() {
        this.onerror = null;
        this.src = '../js/placeholer-image.jpg';
        this.alt = ""
    };
});

// script.js

/**
 * Toggle navigation menu on mobile devices.
 */
document.addEventListener('DOMContentLoaded', function () {
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
  
    if (navToggle) {
      navToggle.addEventListener('click', function () {
        navMenu.classList.toggle('nav-menu-active');
  
        // Update aria-expanded attribute
        const isExpanded = navMenu.classList.contains('nav-menu-active');
        navToggle.setAttribute('aria-expanded', isExpanded);
      });
    }
  });
  
  /**
   * Implement collapsible sections for content.
   */
  document.addEventListener('DOMContentLoaded', function () {
    const collapsibleHeaders = document.querySelectorAll('.collapsible');
  
    collapsibleHeaders.forEach(header => {
      header.addEventListener('click', function () {
        const content = this.nextElementSibling;
        content.classList.toggle('expanded');
  
        // Update aria-expanded attribute
        const isExpanded = content.classList.contains('expanded');
        this.setAttribute('aria-expanded', isExpanded);
      });
    });
  });
  
  /**
   * Athlete search functionality for filtering athlete list.
   */
  document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const athleteListItems = document.querySelectorAll('#athlete-list li');
  
    if (searchInput) {
      searchInput.addEventListener('input', function () {
        const filter = this.value.toLowerCase();
  
        athleteListItems.forEach(item => {
          const text = item.textContent.toLowerCase();
          if (text.includes(filter)) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
      });
    }
  });
  
  