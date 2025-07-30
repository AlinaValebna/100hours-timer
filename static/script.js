function startCountdown(id, seconds, paused) {
    const timerElement = document.getElementById(id);
    function update() {
        if (!paused && seconds > 0) seconds--;

        const hrs = Math.floor(seconds / 3600);
        const min = Math.floor((seconds % 3600) / 60);
        const sec = seconds % 60;
        timerElement.textContent = `${String(hrs).padStart(2, '0')}:${String(min).padStart(2, '0')}:${String(sec).padStart(2, '0')}`;

        if (seconds > 0 && !paused) {
            setTimeout(update, 1000);
        } else if (seconds === 0) {
            timerElement.textContent = "✅ Done!";
        }
    }
    update();
}

