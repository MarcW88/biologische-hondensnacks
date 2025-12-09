/* ========================================
   PRODUCT PAGE FUNCTIONALITY
   ======================================== */

// Initialize product page
document.addEventListener('DOMContentLoaded', function() {
    setupImageGallery();
    setupWishlist();
    setupShareFunctionality();
    setupMobileOptimizations();
});

// Image Gallery Functions
function changeMainImage(src) {
    const mainImage = document.getElementById('mainImage');
    if (mainImage) {
        mainImage.src = src;
        
        // Update active thumbnail
        document.querySelectorAll('.thumbnail').forEach(thumb => {
            thumb.classList.remove('active');
            if (thumb.src === src) {
                thumb.classList.add('active');
            }
        });
    }
}

function setupImageGallery() {
    // Add keyboard navigation for image gallery
    document.addEventListener('keydown', function(e) {
        const thumbnails = document.querySelectorAll('.thumbnail');
        const activeThumbnail = document.querySelector('.thumbnail.active');
        
        if (!activeThumbnail || thumbnails.length <= 1) return;
        
        let currentIndex = Array.from(thumbnails).indexOf(activeThumbnail);
        
        if (e.key === 'ArrowLeft' && currentIndex > 0) {
            e.preventDefault();
            thumbnails[currentIndex - 1].click();
        } else if (e.key === 'ArrowRight' && currentIndex < thumbnails.length - 1) {
            e.preventDefault();
            thumbnails[currentIndex + 1].click();
        }
    });
    
    // Add zoom functionality on main image
    const mainImage = document.getElementById('mainImage');
    if (mainImage) {
        mainImage.addEventListener('click', function() {
            openImageModal(this.src);
        });
    }
}

function openImageModal(imageSrc) {
    // Create modal for image zoom
    const modal = document.createElement('div');
    modal.className = 'image-modal';
    modal.innerHTML = `
        <div class="modal-backdrop" onclick="closeImageModal()">
            <div class="modal-content">
                <img src="${imageSrc}" alt="Product image" class="modal-image">
                <button class="modal-close" onclick="closeImageModal()">×</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    document.body.style.overflow = 'hidden';
    
    // Add styles for modal
    if (!document.getElementById('modal-styles')) {
        const modalStyles = document.createElement('style');
        modalStyles.id = 'modal-styles';
        modalStyles.textContent = `
            .image-modal {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .modal-backdrop {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .modal-content {
                position: relative;
                max-width: 90vw;
                max-height: 90vh;
            }
            
            .modal-image {
                max-width: 100%;
                max-height: 100%;
                object-fit: contain;
                border-radius: 8px;
            }
            
            .modal-close {
                position: absolute;
                top: -40px;
                right: 0;
                background: white;
                border: none;
                width: 32px;
                height: 32px;
                border-radius: 50%;
                font-size: 20px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
            }
        `;
        document.head.appendChild(modalStyles);
    }
}

function closeImageModal() {
    const modal = document.querySelector('.image-modal');
    if (modal) {
        modal.remove();
        document.body.style.overflow = '';
    }
}

// Wishlist Functions
function setupWishlist() {
    updateWishlistUI();
}

function addToWishlist(productId) {
    let wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    
    if (!wishlist.includes(productId)) {
        wishlist.push(productId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        showNotification('✅ Toegevoegd aan verlanglijst!', 'success');
    } else {
        wishlist = wishlist.filter(id => id !== productId);
        localStorage.setItem('wishlist', JSON.stringify(wishlist));
        showNotification('❌ Verwijderd uit verlanglijst', 'info');
    }
    
    updateWishlistUI();
}

function updateWishlistUI() {
    const wishlist = JSON.parse(localStorage.getItem('wishlist') || '[]');
    const wishlistButtons = document.querySelectorAll('[onclick*="addToWishlist"]');
    
    wishlistButtons.forEach(button => {
        const productId = extractProductIdFromOnclick(button.getAttribute('onclick'));
        if (wishlist.includes(parseInt(productId))) {
            button.innerHTML = '💖 In verlanglijst';
            button.classList.add('in-wishlist');
        } else {
            button.innerHTML = '❤️ Toevoegen aan verlanglijst';
            button.classList.remove('in-wishlist');
        }
    });
}

function extractProductIdFromOnclick(onclickStr) {
    const match = onclickStr.match(/addToWishlist\((\d+)\)/);
    return match ? match[1] : null;
}

// Share Functions
function setupShareFunctionality() {
    // Check if Web Share API is supported
    if (navigator.share) {
        const shareButtons = document.querySelectorAll('[onclick*="shareProduct"]');
        shareButtons.forEach(button => {
            button.innerHTML = '📤 Delen';
        });
    }
}

function shareProduct() {
    const productName = document.querySelector('h1').textContent;
    const productUrl = window.location.href;
    const productDescription = document.querySelector('.product-description p').textContent;
    
    if (navigator.share) {
        navigator.share({
            title: productName,
            text: productDescription,
            url: productUrl
        }).catch(err => console.log('Error sharing:', err));
    } else {
        // Fallback: copy to clipboard
        navigator.clipboard.writeText(productUrl).then(() => {
            showNotification('🔗 Link gekopieerd naar klembord!', 'success');
        }).catch(() => {
            // Final fallback: show share modal
            showShareModal(productName, productUrl);
        });
    }
}

function showShareModal(title, url) {
    const modal = document.createElement('div');
    modal.className = 'share-modal';
    modal.innerHTML = `
        <div class="modal-backdrop" onclick="closeShareModal()">
            <div class="modal-content share-content">
                <h3>Deel dit product</h3>
                <div class="share-options">
                    <a href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}" target="_blank" class="share-btn facebook">
                        📘 Facebook
                    </a>
                    <a href="https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(url)}" target="_blank" class="share-btn twitter">
                        🐦 Twitter
                    </a>
                    <a href="https://wa.me/?text=${encodeURIComponent(title + ' ' + url)}" target="_blank" class="share-btn whatsapp">
                        💬 WhatsApp
                    </a>
                    <button onclick="copyToClipboard('${url}')" class="share-btn copy">
                        📋 Kopieer link
                    </button>
                </div>
                <button class="modal-close" onclick="closeShareModal()">Sluiten</button>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Add styles for share modal
    if (!document.getElementById('share-modal-styles')) {
        const shareStyles = document.createElement('style');
        shareStyles.id = 'share-modal-styles';
        shareStyles.textContent = `
            .share-modal .modal-backdrop {
                background: rgba(0, 0, 0, 0.5);
            }
            
            .share-content {
                background: white;
                padding: 2rem;
                border-radius: 12px;
                max-width: 400px;
                width: 90vw;
            }
            
            .share-content h3 {
                margin: 0 0 1rem 0;
                text-align: center;
            }
            
            .share-options {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
                margin-bottom: 1rem;
            }
            
            .share-btn {
                padding: 0.75rem;
                border: 1px solid #ddd;
                border-radius: 8px;
                text-decoration: none;
                color: #333;
                text-align: center;
                transition: all 0.2s;
                background: white;
                cursor: pointer;
            }
            
            .share-btn:hover {
                background: #f8f9fa;
                border-color: var(--primary-orange);
            }
            
            .modal-close {
                width: 100%;
                padding: 0.75rem;
                background: var(--primary-orange);
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
        `;
        document.head.appendChild(shareStyles);
    }
}

function closeShareModal() {
    const modal = document.querySelector('.share-modal');
    if (modal) {
        modal.remove();
    }
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('🔗 Link gekopieerd!', 'success');
        closeShareModal();
    });
}

// Analytics and Tracking
function trackPurchaseClick(productId, productName) {
    // Google Analytics tracking
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            event_category: 'affiliate_link',
            event_label: productName,
            value: productId
        });
    }
    
    // Custom tracking
    console.log(`Purchase click tracked: ${productId} - ${productName}`);
    
    // You can add additional tracking here (Facebook Pixel, etc.)
}

// Mobile Optimizations
function setupMobileOptimizations() {
    // Optimize for mobile touch
    if ('ontouchstart' in window) {
        // Add touch-friendly interactions
        document.body.classList.add('touch-device');
        
        // Improve button tap targets
        const buttons = document.querySelectorAll('button, .btn-primary, .btn-secondary');
        buttons.forEach(button => {
            button.style.minHeight = '44px';
            button.style.minWidth = '44px';
        });
    }
    
    // Lazy load related products images
    setupLazyLoading();
}

function setupLazyLoading() {
    const images = document.querySelectorAll('.products-grid img');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        images.forEach(img => {
            imageObserver.observe(img);
        });
    }
}

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    const colors = {
        success: '#28a745',
        error: '#dc3545',
        info: '#17a2b8',
        warning: '#ffc107'
    };
    
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${colors[type] || colors.info};
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        z-index: 10000;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        animation: slideInRight 0.3s ease;
        max-width: 300px;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Add CSS animations for notifications
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
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
    
    .in-wishlist {
        background: #dc3545 !important;
        color: white !important;
    }
    
    .touch-device button {
        -webkit-tap-highlight-color: rgba(0,0,0,0.1);
    }
`;
document.head.appendChild(notificationStyles);

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // ESC to close modals
    if (e.key === 'Escape') {
        closeImageModal();
        closeShareModal();
    }
    
    // Ctrl/Cmd + D to add to wishlist
    if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
        e.preventDefault();
        const wishlistBtn = document.querySelector('[onclick*="addToWishlist"]');
        if (wishlistBtn) {
            wishlistBtn.click();
        }
    }
    
    // Ctrl/Cmd + S to share
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        shareProduct();
    }
});

// Performance monitoring
window.addEventListener('load', function() {
    // Log page load time
    const loadTime = performance.now();
    console.log(`Page loaded in ${Math.round(loadTime)}ms`);
    
    // Track page view
    if (typeof gtag !== 'undefined') {
        gtag('event', 'page_view', {
            page_title: document.title,
            page_location: window.location.href
        });
    }
});
