document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const message = document.getElementById('message');
    const loading = document.getElementById('loading');
    const loginContainer = document.getElementById('login-container');
    let currentLevel = 1;

    function updateLevelInfo(levelData) {
        document.getElementById('current-level').textContent = levelData.id;
        document.getElementById('meme-era').textContent = levelData.memeEra;
        document.getElementById('persona').textContent = levelData.persona;
        document.getElementById('captcha').textContent = levelData.captcha;
        document.getElementById('year').textContent = levelData.year;
        document.getElementById('language').textContent = levelData.language;
        document.getElementById('task').textContent = levelData.task;

        // Update theme
        loginContainer.className = ''; // Reset classes
        loginContainer.classList.add(`theme-${levelData.memeEra.toLowerCase().replace(' ', '-')}`);

        // Animate level change
        loginContainer.style.transform = 'scale(0.9)';
        loginContainer.style.opacity = '0.5';
        setTimeout(() => {
            loginContainer.style.transform = 'scale(1)';
            loginContainer.style.opacity = '1';
        }, 300);
    }

    function fetchLevel(level) {
        loading.classList.remove('hidden');
        loginForm.classList.add('hidden');

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ level: level }),
        })
        .then(response => response.json())
        .then(data => {
            loading.classList.add('hidden');
            loginForm.classList.remove('hidden');

            if (data.success) {
                if (data.completed) {
                    message.textContent = "Congratulations! You've completed all levels!";
                    loginForm.style.display = 'none';
                    confetti();
                } else {
                    message.textContent = "Login successful! Moving to next level...";
                    currentLevel++;
                    updateLevelInfo(data.nextLevel);
                }
            } else {
                message.textContent = "Login failed. Try again!";
                shakeForm();
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            message.textContent = "An error occurred. Please try again.";
            loading.classList.add('hidden');
            loginForm.classList.remove('hidden');
        });
    }

    function shakeForm() {
        loginForm.classList.add('shake');
        setTimeout(() => loginForm.classList.remove('shake'), 500);
    }

    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        fetchLevel(currentLevel);
    });

    // Fetch the first level on page load
    fetchLevel(0);
});

// Simple confetti effect
function confetti() {
    const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'];
    for (let i = 0; i < 100; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.animationDelay = Math.random() * 5 + 's';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        document.body.appendChild(confetti);
    }
}