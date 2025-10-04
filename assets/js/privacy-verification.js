/**
 * Privacy Verification Script
 * Provides client-side privacy verification functionality
 */

// Privacy verification functions
const PrivacyVerification = {
    /**
     * Checks for common tracking scripts in the current page
     */
    checkTrackingScripts: function() {
        const trackingPatterns = [
            'google-analytics',
            'google.com/analytics',
            'facebook.com/tr',
            'gtm.js',
            'gtag',
            'facebook-pixel',
            'hotjar',
            'plausible',
            'matomo',
            'mixpanel',
            'segment',
            'ga.js',
            'urchin',
            'tagmanager',
            'adsbygoogle',
            'doubleclick',
            'googletag'
        ];

        const foundTracking = [];
        const scripts = document.getElementsByTagName('script');
        
        for (let script of scripts) {
            if (script.src) {
                for (let pattern of trackingPatterns) {
                    if (script.src.toLowerCase().includes(pattern)) {
                        foundTracking.push({
                            type: pattern,
                            location: 'external-script',
                            source: script.src
                        });
                    }
                }
            }
            
            // Check inline scripts for tracking patterns
            if (script.textContent) {
                for (let pattern of trackingPatterns) {
                    if (script.textContent.toLowerCase().includes(pattern)) {
                        foundTracking.push({
                            type: pattern,
                            location: 'inline-script',
                            source: 'inline script content'
                        });
                    }
                }
            }
        }
        
        return foundTracking;
    },

    /**
     * Checks for cookie-setting scripts that might be used for tracking
     */
    checkCookieTracking: function() {
        const cookieTrackingPatterns = [
            'document.cookie',
            'localStorage',
            'sessionStorage'
        ];
        
        const foundCookies = [];
        const scripts = document.getElementsByTagName('script');
        
        for (let script of scripts) {
            if (script.textContent) {
                for (let pattern of cookieTrackingPatterns) {
                    if (script.textContent.toLowerCase().includes(pattern.toLowerCase())) {
                        foundCookies.push({
                            type: 'cookie-tracking',
                            pattern: pattern,
                            source: script.src || 'inline script'
                        });
                    }
                }
            }
        }
        
        return foundCookies;
    },

    /**
     * Checks for tracking in iframes and other embedded content
     */
    checkExternalContent: function() {
        const trackingFound = [];
        
        // Check for iframes from tracking services
        const iframes = document.getElementsByTagName('iframe');
        for (let iframe of iframes) {
            if (iframe.src) {
                if (iframe.src.includes('youtube.com') || 
                    iframe.src.includes('facebook.com') || 
                    iframe.src.includes('twitter.com')) {
                    trackingFound.push({
                        type: 'tracking-iframe',
                        location: 'iframe',
                        source: iframe.src
                    });
                }
            }
        }
        
        // Check for other tracking elements
        const embeds = document.querySelectorAll('embed, object');
        for (let embed of embeds) {
            if (embed.src) {
                if (embed.src.includes('tracking') || embed.src.includes('analytics')) {
                    trackingFound.push({
                        type: 'tracking-embed',
                        location: embed.tagName.toLowerCase(),
                        source: embed.src
                    });
                }
            }
        }
        
        return trackingFound;
    },

    /**
     * Performs a complete privacy verification
     */
    verify: function() {
        const trackingScripts = this.checkTrackingScripts();
        const cookieTracking = this.checkCookieTracking();
        const externalContent = this.checkExternalContent();
        
        const result = {
            verificationDate: new Date().toISOString(),
            status: "PASS",
            trackingScriptsFound: trackingScripts,
            details: {
                cookiesCheck: cookieTracking.length === 0 ? "PASS" : "FAIL",
                thirdPartyScripts: externalContent.length === 0 ? "PASS" : "FAIL",
                fingerprintingChecks: "PENDING", // Would require more complex analysis
                analyticsCheck: trackingScripts.length === 0 ? "PASS" : "FAIL"
            },
            summary: {
                trackingScripts: trackingScripts.length,
                cookieIssues: cookieTracking.length,
                externalResources: externalContent.length
            }
        };
        
        // Overall status is PASS only if no tracking is found
        if (trackingScripts.length > 0 || cookieTracking.length > 0 || externalContent.length > 0) {
            result.status = "FAIL";
        }
        
        return result;
    },

    /**
     * Runs verification and displays results in the console
     */
    runAndDisplay: function() {
        const result = this.verify();
        console.log("Privacy Verification Result:", result);
        return result;
    }
};

// Export for use in other modules if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PrivacyVerification;
}