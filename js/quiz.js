/**
 * SNACK FINDER QUIZ
 * =================
 * Quiz interactif pour trouver les meil leurs snacks
 */

// State
let quizAnswers = {};
let currentQuestion = 1;

// Initialize quiz
document.addEventListener('DOMContentLoaded', function() {
    console.log('🎯 Quiz initialized');
    
    // Add click handlers to all option buttons
    const allButtons = document.querySelectorAll('.quiz-question .option');
    console.log(`📊 Found ${allButtons.length} option buttons`);
    
    allButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const questionNum = parseInt(this.closest('.quiz-question').id.split('-')[1]);
            const value = this.getAttribute('data-value');
            
            console.log(`✅ Selected: Q${questionNum} = ${value}`);
            
            selectOption(questionNum, value);
        });
        
        // Hover effects
        button.addEventListener('mouseenter', function() {
            if (!this.classList.contains('selected')) {
                this.style.borderColor = '#E68161';
                this.style.background = '#fef7f0';
                this.style.transform = 'translateY(-2px)';
            }
        });
        
        button.addEventListener('mouseleave', function() {
            if (!this.classList.contains('selected')) {
                this.style.borderColor = '#e5e7eb';
                this.style.background = 'white';
                this.style.transform = 'translateY(0)';
            }
        });
    });
});

function selectOption(questionNum, value) {
    console.log(`🎯 selectOption called: Q${questionNum} = ${value}`);
    
    quizAnswers[questionNum] = value;
    console.log('Current answers:', quizAnswers);
    
    // Visual feedback for selected option
    const currentQuestion = document.getElementById(`question-${questionNum}`);
    if (!currentQuestion) {
        console.error(`❌ Question ${questionNum} not found!`);
        return;
    }
    
    const currentOptions = currentQuestion.querySelectorAll('.option');
    console.log(`Found ${currentOptions.length} options in question ${questionNum}`);
    
    currentOptions.forEach(btn => {
        btn.style.borderColor = '#e5e7eb';
        btn.style.background = 'white';
        btn.classList.remove('selected');
    });
    
    // Highlight selected option
    const selectedBtn = currentQuestion.querySelector(`.option[data-value="${value}"]`);
    if (selectedBtn) {
        selectedBtn.style.borderColor = '#E68161';
        selectedBtn.style.background = '#fef7f0';
        selectedBtn.classList.add('selected');
        console.log('✅ Option highlighted');
    } else {
        console.error(`❌ Selected button not found for value: ${value}`);
    }
    
    // Small delay for visual feedback, then proceed
    setTimeout(() => {
        if (questionNum < 3) {
            console.log(`➡️ Moving to question ${questionNum + 1}`);
            showNextQuestion(questionNum + 1);
        } else {
            console.log('🎉 Quiz complete, showing results');
            showResults();
        }
    }, 300);
}

function updateProgress(questionNum) {
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.quiz-progress span');
    
    if (progressFill && progressText) {
        const percentage = (questionNum / 3) * 100;
        progressFill.style.width = percentage + '%';
        progressText.textContent = `Vraag ${questionNum} van 3`;
        console.log(`📊 Progress updated: ${percentage}%`);
    }
}

function showNextQuestion(questionNum) {
    console.log(`📄 showNextQuestion(${questionNum})`);
    
    // Hide current question
    const prevQuestion = document.getElementById(`question-${questionNum - 1}`);
    if (prevQuestion) {
        prevQuestion.style.display = 'none';
        console.log(`✅ Hidden question-${questionNum - 1}`);
    }
    
    // Show next question
    const nextQuestion = document.getElementById(`question-${questionNum}`);
    if (nextQuestion) {
        nextQuestion.style.display = 'block';
        currentQuestion = questionNum;
        console.log(`✅ Showing question-${questionNum}`);
        
        // Update progress
        updateProgress(questionNum);
    } else {
        console.error(`❌ Question ${questionNum} not found!`);
    }
}

function showResults() {
    console.log('🎉 Showing results...');
    
    // Hide last question
    const q3 = document.getElementById('question-3');
    if (q3) {
        q3.style.display = 'none';
    }
    
    // Update progress to 100%
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.quiz-progress span');
    if (progressFill) progressFill.style.width = '100%';
    if (progressText) progressText.textContent = 'Voltooid!';
    
    // Get recommendation
    const recommendation = getRecommendation();
    console.log('Recommendation:', recommendation);
    
    // Show result
    const resultDiv = document.querySelector('.quiz-result');
    const productDiv = document.querySelector('.recommended-product');
    
    if (productDiv) {
        productDiv.innerHTML = `
            <div style="display: flex; gap: 1rem; align-items: center; text-align: left;">
                <img src="${recommendation.image}" alt="${recommendation.name}" style="width: 80px; height: 80px; border-radius: 8px; object-fit: cover;">
                <div style="flex: 1;">
                    <h4 style="margin: 0 0 0.5rem 0; color: #2d3748; font-size: 1.2rem;">${recommendation.name}</h4>
                    <p style="margin: 0 0 0.5rem 0; color: #666; font-size: 0.9rem;">${recommendation.description}</p>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="font-size: 1.2rem; font-weight: 700; color: #E68161;">${recommendation.price}</span>
                        <span style="color: #FFD700;">★★★★★</span>
                        <span style="font-size: 0.9rem; color: #666;">${recommendation.rating}</span>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Update CTA link
    const ctaLink = resultDiv.querySelector('.btn-primary');
    if (ctaLink) {
        ctaLink.href = recommendation.url;
    }
    
    if (resultDiv) {
        resultDiv.style.display = 'block';
        console.log('✅ Results displayed');
    }
}

function getRecommendation() {
    const age = quizAnswers[1];
    const purpose = quizAnswers[2];
    const size = quizAnswers[3];
    
    console.log(`Getting recommendation for: age=${age}, purpose=${purpose}, size=${size}`);
    
    // Recommendations database
    const recommendations = {
        'puppy-training-small': {
            name: 'HobbyFirst Canex Trainers Konijn',
            description: 'Perfect voor training van kleine puppy\'s. Klein formaat, zacht en makkelijk te verteren.',
            price: '€18,00',
            rating: '4.8/5 (127 reviews)',
            image: '../images/HobbyFirst Canex Trainers Konijn .jpg',
            url: '../produits/hobbyfirst-canex-trainers-konijn.html'
        },
        'puppy-reward-small': {
            name: 'Softies Eend',
            description: 'Zachte beloning voor puppy\'s. Ideaal voor jonge honden met gevoelige tandjes.',
            price: '€12,95',
            rating: '4.7/5 (89 reviews)',
            image: '../images/Softies Eend .jpg',
            url: '../produits/softies-eend.html'
        },
        'adult-training-medium': {
            name: 'Petstyle Living Sticks Kip 100 stuks',
            description: 'Training sticks perfect voor volwassen honden. 100 stuks voor intensieve training.',
            price: '€19,95',
            rating: '4.9/5 (203 reviews)',
            image: '../images/Petstyle Living Sticks Kip 100 stuks .jpg',
            url: '../produits/petstyle-living-sticks-kip-100-stuks.html'
        },
        'adult-reward-large': {
            name: 'Chewpi Kauwstaaf (20+ kg) - Extra Large',
            description: 'Langdurig kauwplezier voor grote honden. 100% natuurlijk en duurzaam.',
            price: '€15,99',
            rating: '4.8/5 (156 reviews)',
            image: '../images/Chewpi Kauwstaaf (20+ kg) - Extra Large.jpg',
            url: '../produits/chewpi-kauwstaaf-20-kg-extra-large.html'
        },
        'adult-health-any': {
            name: 'Landman Eendfilet Gedroogd',
            description: 'Hypoallergeen en 100% natuurlijk. Perfect voor honden met gevoelige magen.',
            price: '€21,50',
            rating: '4.9/5 (178 reviews)',
            image: '../images/Landman Eendfilet Gedroogd .jpg',
            url: '../produits/landman-eendfilet-gedroogd.html'
        },
        'default': {
            name: 'Petstyle Living Kipfilet',
            description: 'Veelzijdige snack geschikt voor alle honden. Puur kipfilet zonder toevoegingen.',
            price: '€29,95',
            rating: '4.8/5 (234 reviews)',
            image: '../images/Petstyle Living Kipfilet .jpg',
            url: '../produits/petstyle-living-kipfilet.html'
        }
    };
    
    // Build key
    let key = `${age}-${purpose}-${size}`;
    
    // Try exact match
    if (recommendations[key]) {
        return recommendations[key];
    }
    
    // Try without size
    key = `${age}-${purpose}-any`;
    if (recommendations[key]) {
        return recommendations[key];
    }
    
    // Default
    return recommendations['default'];
}

function restartQuiz() {
    console.log('🔄 Restarting quiz');
    
    quizAnswers = {};
    currentQuestion = 1;
    
    // Hide result
    const resultDiv = document.querySelector('.quiz-result');
    if (resultDiv) {
        resultDiv.style.display = 'none';
    }
    
    // Show first question, hide others
    const q1 = document.getElementById('question-1');
    const q2 = document.getElementById('question-2');
    const q3 = document.getElementById('question-3');
    
    if (q1) q1.style.display = 'block';
    if (q2) q2.style.display = 'none';
    if (q3) q3.style.display = 'none';
    
    // Reset progress
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.quiz-progress span');
    if (progressFill) progressFill.style.width = '33%';
    if (progressText) progressText.textContent = 'Vraag 1 van 3';
    
    // Reset button styles
    document.querySelectorAll('.option').forEach(btn => {
        btn.style.borderColor = '#e5e7eb';
        btn.style.background = 'white';
        btn.classList.remove('selected');
    });
    
    console.log('✅ Quiz restarted');
}

// Make functions global for onclick attributes
window.selectOption = selectOption;
window.restartQuiz = restartQuiz;
