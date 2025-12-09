/* ========================================
   WISHLIST & INTERACTIONS FUNCTIONALITY
   ======================================== */

// Initialize wishlist functionality
document.addEventListener('DOMContentLoaded', function() {
    initializeWishlist();
    initializeQuiz();
    initializeNotifications();
});

// Wishlist Functions
function addToWishlist(productId) {
    let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    
    if (!wishlist.includes(productId)) {
        wishlist.push(productId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        showNotification('Product toegevoegd aan verlanglijst!', 'success');
        
        // Update button text
        const button = document.querySelector(`[onclick*="${productId}"]`);
        if (button) {
            button.innerHTML = '❤ In verlanglijst';
            button.style.background = '#dc3545';
            button.style.color = 'white';
        }
        
        // Track event
        trackEvent('wishlist_add', productId);
    } else {
        // Remove from wishlist
        wishlist = wishlist.filter(id => id !== productId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        showNotification('Product verwijderd uit verlanglijst', 'info');
        
        // Update button text
        const button = document.querySelector(`[onclick*="${productId}"]`);
        if (button) {
            button.innerHTML = '❤ Bewaren';
            button.style.background = 'transparent';
            button.style.color = '#E68161';
        }
        
        // Track event
        trackEvent('wishlist_remove', productId);
    }
    
    updateWishlistCount();
}

function initializeWishlist() {
    const wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    
    // Update all wishlist buttons on page load
    wishlist.forEach(productId => {
        const button = document.querySelector(`[onclick*="${productId}"]`);
        if (button) {
            button.innerHTML = '❤ In verlanglijst';
            button.style.background = '#dc3545';
            button.style.color = 'white';
        }
    });
    
    updateWishlistCount();
}

function updateWishlistCount() {
    const wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    const count = wishlist.length;
    
    // Update wishlist counter in navigation (if exists)
    const counter = document.querySelector('.wishlist-count');
    if (counter) {
        counter.textContent = count;
        counter.style.display = count > 0 ? 'inline' : 'none';
    }
}

// Quiz Functions
function initializeQuiz() {
    const quizOptions = document.querySelectorAll('.option');
    let currentQuestion = 1;
    const totalQuestions = 3;
    
    quizOptions.forEach(option => {
        option.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            
            // Store answer
            localStorage.setItem(`quiz_q${currentQuestion}`, value);
            
            // Visual feedback
            this.style.borderColor = '#E68161';
            this.style.background = '#fef7f0';
            
            // Progress to next question or show result
            setTimeout(() => {
                if (currentQuestion < totalQuestions) {
                    currentQuestion++;
                    showNextQuestion(currentQuestion);
                    updateProgressBar(currentQuestion, totalQuestions);
                } else {
                    showQuizResult();
                }
            }, 500);
            
            // Track quiz progress
            trackEvent('quiz_answer', `q${currentQuestion}_${value}`);
        });
    });
}

function showNextQuestion(questionNumber) {
    // This would show the next question
    // For now, we'll simulate with the result
    if (questionNumber > 3) {
        showQuizResult();
    }
}

function updateProgressBar(current, total) {
    const progressFill = document.querySelector('.progress-fill');
    const progressText = document.querySelector('.quiz-progress span');
    
    if (progressFill) {
        const percentage = (current / total) * 100;
        progressFill.style.width = percentage + '%';
    }
    
    if (progressText) {
        progressText.textContent = `Vraag ${current} van ${total}`;
    }
}

function showQuizResult() {
    const quizQuestion = document.querySelector('.quiz-question');
    const quizResult = document.querySelector('.quiz-result');
    
    if (quizQuestion && quizResult) {
        quizQuestion.style.display = 'none';
        quizResult.style.display = 'block';
        
        // Generate recommendation based on answers
        const recommendation = generateRecommendation();
        const productContainer = document.querySelector('.recommended-product');
        
        if (productContainer) {
            productContainer.innerHTML = `
                <img src="${recommendation.image}" alt="${recommendation.name}" style="width: 80px; height: 80px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
                <h4 style="margin: 0.5rem 0; color: #2d3748;">${recommendation.name}</h4>
                <div style="color: #FFD700; margin-bottom: 0.5rem;">★★★★★ ${recommendation.rating}/5</div>
                <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">${recommendation.description}</p>
                <div style="font-size: 1.2rem; font-weight: 600; color: #E68161;">€${recommendation.price}</div>
            `;
        }
        
        // Update CTA link
        const ctaLink = document.querySelector('.quiz-result .btn-primary');
        if (ctaLink) {
            ctaLink.href = recommendation.url;
        }
        
        // Track quiz completion
        trackEvent('quiz_complete', recommendation.id);
    }
}

function generateRecommendation() {
    const age = localStorage.getItem('quiz_q1') || 'adult';
    
    // Simple recommendation logic based on age
    const recommendations = {
        puppy: {
            id: 'puppy-koekjes',
            name: 'Zachte Puppy Koekjes',
            image: 'images/zachte-puppy-koekjes.jpg',
            rating: 4.8,
            description: 'Perfect voor jonge honden. Zacht, verteerbaar en vol belangrijke voedingsstoffen.',
            price: '6.75',
            url: 'https://partnerprogramma.bol.com/click/click?p=2&t=url&s=XXXX&f=TXN&url=https://www.bol.com/nl/p/puppy-koekjes/'
        },
        adult: {
            id: 'zalm-bites',
            name: 'Natuurlijke Zalm Bites',
            image: 'images/natuurlijke-zalm-bites.jpg',
            rating: 4.7,
            description: '100% natuurlijke zalm, perfect voor training. Graanvrij en vol omega-3 vetzuren.',
            price: '8.95',
            url: 'https://partnerprogramma.bol.com/click/click?p=2&t=url&s=XXXX&f=TXN&url=https://www.bol.com/nl/p/natuurlijke-zalm-bites/'
        },
        senior: {
            id: 'hertenvlees-strips',
            name: 'Biologische Hertenvlees Strips',
            image: 'images/Biologische-Hertenvlees-Strips .jpg',
            rating: 4.9,
            description: 'Zacht en gemakkelijk verteerbaar voor oudere honden. Hypoallergeen en rijk aan proteïnen.',
            price: '12.50',
            url: 'https://partnerprogramma.bol.com/click/click?p=2&t=url&s=XXXX&f=TXN&url=https://www.bol.com/nl/p/hertenvlees-strips/'
        }
    };
    
    return recommendations[age] || recommendations.adult;
}

function restartQuiz() {
    // Clear stored answers
    localStorage.removeItem('quiz_q1');
    localStorage.removeItem('quiz_q2');
    localStorage.removeItem('quiz_q3');
    
    // Reset UI
    const quizQuestion = document.querySelector('.quiz-question');
    const quizResult = document.querySelector('.quiz-result');
    
    if (quizQuestion && quizResult) {
        quizQuestion.style.display = 'block';
        quizResult.style.display = 'none';
    }
    
    // Reset progress bar
    updateProgressBar(1, 3);
    
    // Reset option styles
    document.querySelectorAll('.option').forEach(option => {
        option.style.borderColor = '#e5e7eb';
        option.style.background = 'white';
    });
    
    trackEvent('quiz_restart');
}

// Notification System
function initializeNotifications() {
    // Create notification container if it doesn't exist
    if (!document.querySelector('.notification-container')) {
        const container = document.createElement('div');
        container.className = 'notification-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 10000;
            pointer-events: none;
        `;
        document.body.appendChild(container);
    }
}

function showNotification(message, type = 'info') {
    const container = document.querySelector('.notification-container');
    if (!container) return;
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    
    const colors = {
        success: '#22c55e',
        error: '#dc3545',
        info: '#17a2b8',
        warning: '#ffc107'
    };
    
    notification.style.cssText = `
        background: ${colors[type] || colors.info};
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        animation: slideInRight 0.3s ease;
        pointer-events: auto;
        cursor: pointer;
        max-width: 300px;
        word-wrap: break-word;
    `;
    
    notification.textContent = message;
    
    // Add click to dismiss
    notification.addEventListener('click', () => {
        removeNotification(notification);
    });
    
    container.appendChild(notification);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        removeNotification(notification);
    }, 3000);
}

function removeNotification(notification) {
    if (notification && notification.parentNode) {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }
}

// Analytics Tracking
function trackEvent(eventName, eventData = null) {
    // Google Analytics 4
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, {
            event_category: 'user_interaction',
            event_label: eventData,
            value: 1
        });
    }
    
    // Console log for development
    console.log(`Event tracked: ${eventName}`, eventData);
    
    // You can add other analytics services here
    // Facebook Pixel, Hotjar, etc.
}

// Smooth scrolling for anchor links
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Track scroll to section
                trackEvent('scroll_to_section', this.getAttribute('href'));
            }
        });
    });
});

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    .option:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(230, 129, 97, 0.2);
    }
    
    .option:active {
        transform: translateY(0);
    }
    
    .btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .product-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
`;
document.head.appendChild(style);
