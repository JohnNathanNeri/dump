document.addEventListener('DOMContentLoaded', () => {
    const boxes = document.querySelectorAll('.box');
    
    function handleScroll() {
      boxes.forEach(box => {
        const img = box.querySelector('img');
        const rect = box.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
          img.classList.add('revealed');
        }
      });
    }
  
    window.addEventListener('scroll', handleScroll);
    handleScroll(); // Initial check in case elements are in view on load
  });
  