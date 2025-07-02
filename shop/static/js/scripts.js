document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel');
    const items = document.querySelectorAll('.carousel-item');
    const prevButton = document.querySelector('.carousel-control-prev');
    const nextButton = document.querySelector('.carousel-control-next');
    let currentIndex = 0;
    const itemWidth = items[0].offsetWidth;
    const interval = 3000; // Change slide every 3 seconds

    function nextSlide() {
        currentIndex = (currentIndex + 1) % items.length;
        updateCarousel();
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + items.length) % items.length;
        updateCarousel();
    }

    function updateCarousel() {
        carousel.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
    }

    // Start the automatic sliding
    setInterval(nextSlide, interval);

    // Handle button clicks
    nextButton.addEventListener('click', nextSlide);
    prevButton.addEventListener('click', prevSlide);
});