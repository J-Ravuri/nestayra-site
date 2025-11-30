
// Smooth scroll effect for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Button hover animation (pulse effect)
const btn = document.querySelector('.btn');
btn.addEventListener('mouseenter', () => {
    btn.style.transform = 'scale(1.05)';
    btn.style.transition = 'transform 0.3s ease';
});
btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'scale(1)';
});
