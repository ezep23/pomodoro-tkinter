import html from './app.html?raw';
import { createClient } from 'pexels';

const client = createClient(import.meta.env.VITE_PEXELS_API_KEY);

const ElementIDs = {
    background: '#main',
    display: '#timer',
    start: '#startButton',
    reset: '#resetButton'
}

/**
 * 
 * @param {string} id -> del div donde se monta la aplicación  
 * 
*/

export const App = ( id ) => {

    const switchBackground = () => {
        const random = Math.random();
        
        try {
            // const imageInfo = fetch('link')

            client.photos.show({ id: random })
            .then(response => response.json())
            .then(data => console.log(data.name));

            background.setAttribute('style', `background-image: url(${image})`);
        } catch (error) {
            console.error(error);
        }
    }

    const initTimer = () => {
        timer = setInterval(() => {
            currentTime--;
            updateDisplay();
    
            if (currentTime <= 0) {
                clearInterval(timer);
    
                if (isWorking) {
                    // Tiempo de descanso
                    alert('¡Tiempo de descanso!');
                    currentTime = breakTime;
                } else {
                    // Tiempo de trabajo
                    alert('¡Es hora de trabajar!');
                    currentTime = workTime;
                }
                isWorking = !isWorking;
                initTimer(); // Inicia el siguiente ciclo
            }
        }, 1000);
    }
    

    const render = (seconds) => {
        let minutes = Math.floor(seconds / 60);
        let secondsRemaining = seconds % 60;
        return `${minutes.toString().padStart(2, '0')}:${secondsRemaining.toString().padStart(2, '0')}`;
    }

    const updateDisplay = () => display.textContent = render(currentTime);

    const resetTimer = () => {
        clearInterval(timer);
        isWorking = true;
        currentTime = workTime;
        updateDisplay();
    }

    (() => {
        const container = document.createElement('div');
        container.innerHTML = html;
        document.querySelector(id).append(container);
    })();

    // Referencias
    const background = document.querySelector( ElementIDs.background)
    const display = document.querySelector( ElementIDs.display );
    const start = document.querySelector( ElementIDs.start );
    const reset = document.querySelector( ElementIDs.reset ); 

    let workTime = 25 * 60; // 25 minutos en segundos
    let breakTime = 5 * 60; // 5 minutos en segundos
    let isWorking = true; // Indica si es tiempo de trabajo o descanso
    let timer;
    let currentTime = workTime;

    // Listeners
    start.addEventListener('click', () => {
        start.disabled = true;
        initTimer();
        switchBackground();
    });

    reset.addEventListener('click', resetTimer);

    updateDisplay();
};


