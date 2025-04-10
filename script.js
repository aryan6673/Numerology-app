document.addEventListener('DOMContentLoaded', () => {
    console.log("Initializing mystical calculator...");
    updateDateTime();
    setInterval(updateDateTime, 1000);
    setupEventListeners();
    initializeFloatingElements();
});

function updateDateTime() {
    const now = new Date();
    const formatted = now.toISOString().replace('T', ' ').slice(0, 19);
    document.getElementById('utcTime').textContent = formatted;
}

function setupEventListeners() {
    const calculateBtn = document.getElementById('calculateBtn');
    if (calculateBtn) {
        calculateBtn.addEventListener('click', () => {
            console.log("Calculate button clicked");
            animateCalculation();
            calculateNumerology();
        });
    } else {
        console.error("Calculate button not found!");
    }
}

function animateCalculation() {
    const btn = document.getElementById('calculateBtn');
    const btnText = btn.querySelector('.btn-text');
    btn.disabled = true;
    btnText.textContent = '✨ Consulting the Stars... ✨';
    
    setTimeout(() => {
        btn.disabled = false;
        btnText.textContent = 'Reveal Your Destiny';
    }, 2000);
}

// Fixed Numerology Calculations
function calculateDestinyNumber(name) {
    console.log("Calculating destiny number for:", name);
    const numerologyValue = {
        'a': 1, 'j': 1, 's': 1,
        'b': 2, 'k': 2, 't': 2,
        'c': 3, 'l': 3, 'u': 3,
        'd': 4, 'm': 4, 'v': 4,
        'e': 5, 'n': 5, 'w': 5,
        'f': 6, 'o': 6, 'x': 6,
        'g': 7, 'p': 7, 'y': 7,
        'h': 8, 'q': 8, 'z': 8,
        'i': 9, 'r': 9
    };

    const cleanName = name.toLowerCase().replace(/[^a-z]/g, '');
    let sum = 0;
    
    for (let char of cleanName) {
        sum += numerologyValue[char] || 0;
    }
    
    return reduceToSingleDigit(sum);
}

function calculateLifePathNumber(dateStr) {
    console.log("Calculating life path number for:", dateStr);
    const date = new Date(dateStr);
    const day = date.getDate();
    const month = date.getMonth() + 1;
    const year = date.getFullYear();
    
    const dayNum = reduceToSingleDigit(day);
    const monthNum = reduceToSingleDigit(month);
    const yearNum = reduceToSingleDigit(year);
    
    return reduceToSingleDigit(dayNum + monthNum + yearNum);
}

function calculateSoulNumber(name) {
    console.log("Calculating soul number for:", name);
    const vowels = {'a': 1, 'e': 5, 'i': 9, 'o': 6, 'u': 3};
    const cleanName = name.toLowerCase().replace(/[^a-z]/g, '');
    let sum = 0;
    
    for (let char of cleanName) {
        if (vowels[char]) {
            sum += vowels[char];
        }
    }
    
    return reduceToSingleDigit(sum);
}

function reduceToSingleDigit(num) {
    while (num > 9) {
        num = String(num)
            .split('')
            .reduce((a, b) => parseInt(a) + parseInt(b), 0);
    }
    return num;
}

function animateNumber(elementId, finalNumber) {
    const element = document.getElementById(elementId);
    if (!element) {
        console.error(`Element not found: ${elementId}`);
        return;
    }

    const duration = 1500;
    const steps = 20;
    const stepDuration = duration / steps;
    let currentStep = 0;

    const interval = setInterval(() => {
        if (currentStep === steps) {
            clearInterval(interval);
            element.textContent = finalNumber;
            return;
        }

        const progress = currentStep / steps;
        const currentNumber = Math.floor(finalNumber * progress);
        element.textContent = currentNumber || '-';
        currentStep++;
    }, stepDuration);
}

function calculateNumerology() {
    console.log("Starting numerology calculation...");
    
    const fullName = document.getElementById('fullName').value.trim();
    const birthDate = document.getElementById('birthDate').value;

    if (!fullName || !birthDate) {
        alert('✨ Please enter both your sacred name and star date ✨');
        return;
    }

    // Show calculating state
    const resultsSection = document.getElementById('results');
    resultsSection.classList.remove('hidden');

    try {
        // Calculate numbers
        const destinyNumber = calculateDestinyNumber(fullName);
        const lifePathNumber = calculateLifePathNumber(birthDate);
        const soulNumber = calculateSoulNumber(fullName);

        console.log("Calculated numbers:", {
            destiny: destinyNumber,
            lifePath: lifePathNumber,
            soul: soulNumber
        });

        // Animate numbers
        animateNumber('destinyNumber', destinyNumber);
        animateNumber('lifePathNumber', lifePathNumber);
        animateNumber('soulNumber', soulNumber);

        // Update meaning
        updateNumerologyMeaning(destinyNumber, lifePathNumber, soulNumber);

        // Show results with animation
        resultsSection.style.opacity = '0';
        resultsSection.classList.remove('hidden');
        
        setTimeout(() => {
            resultsSection.style.opacity = '1';
        }, 100);

        // Scroll to results
        setTimeout(() => {
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        }, 500);

    } catch (error) {
        console.error("Calculation error:", error);
        alert('✨ The stars are misaligned. Please try again. ✨');
    }
}

function initializeFloatingElements() {
    const container = document.querySelector('.floating-elements');
    if (!container) return;
    
    // Create additional floating elements
    for (let i = 0; i < 20; i++) {
        const spirit = document.createElement('div');
        spirit.className = 'spirit';
        spirit.style.left = `${Math.random() * 100}%`;
        spirit.style.top = `${Math.random() * 100}%`;
        spirit.style.animationDelay = `${Math.random() * 4}s`;
        spirit.textContent = Math.random() > 0.5 ? '✦' : '✧';
        container.appendChild(spirit);
    }
}

function updateNumerologyMeaning(destinyNumber, lifePathNumber, soulNumber) {
    const meaningElement = document.getElementById('numerologyMeaning');
    if (!meaningElement) return;

    const meanings = {
        1: {
            destiny: "A natural leader and pioneer",
            lifePath: "Independent and ambitious",
            soul: "Creative and original"
        },
        2: {
            destiny: "A diplomatic peacemaker",
            lifePath: "Cooperative and sensitive",
            soul: "Emotional and intuitive"
        },
        3: {
            destiny: "A creative communicator",
            lifePath: "Expressive and joyful",
            soul: "Artistic and social"
        },
        4: {
            destiny: "A practical builder",
            lifePath: "Organized and reliable",
            soul: "Stable and hardworking"
        },
        5: {
            destiny: "An adventurous free spirit",
            lifePath: "Versatile and progressive",
            soul: "Freedom-loving and adaptable"
        },
        6: {
            destiny: "A nurturing guardian",
            lifePath: "Responsible and loving",
            soul: "Harmonious and caring"
        },
        7: {
            destiny: "A spiritual seeker",
            lifePath: "Analytical and mystical",
            soul: "Introspective and wise"
        },
        8: {
            destiny: "A powerful achiever",
            lifePath: "Ambitious and successful",
            soul: "Material and influential"
        },
        9: {
            destiny: "A humanitarian teacher",
            lifePath: "Compassionate and wise",
            soul: "Universal and giving"
        }
    };

    const meaning = `
        <div class="mystical-reading">
            <p class="destiny-text">
                ✧ Your Destiny Number ${destinyNumber} reveals you as ${meanings[destinyNumber].destiny}. 
                The stars have aligned to guide you toward leadership and innovation.
            </p>
            
            <p class="life-path-text">
                ✧ Walking the Life Path of ${lifePathNumber}, you are ${meanings[lifePathNumber].lifePath}. 
                This path calls you to embrace change and growth.
            </p>
            
            <p class="soul-text">
                ✧ Your Soul Number ${soulNumber} whispers that you are ${meanings[soulNumber].soul}. 
                Your inner light shines with unique purpose.
            </p>
            
            <div class="synthesis">
                <h4>✧ Mystical Synthesis ✧</h4>
                <p>
                    The combination of these sacred numbers creates a unique cosmic signature. 
                    Your destiny (${destinyNumber}) and life path (${lifePathNumber}) numbers dance together, 
                    while your soul number (${soulNumber}) illuminates your inner truth.
                </p>
            </div>
        </div>
    `;

    meaningElement.innerHTML = meaning;
}