gsap.registerPlugin(ScrollTrigger);


gsap.from(".video-overlay h1", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 0.5,
});

gsap.from(".video-overlay p", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 1,
});

gsap.from(".cta-button", {
    opacity: 0,
    y: 50,
    duration: 1.5,
    delay: 1.5,
});


gsap.from(".section-1 .text-content", {
    scrollTrigger: {
        trigger: ".section-1",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: -100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-1 .image-content", {
    scrollTrigger: {
        trigger: ".section-1",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-2 .text-content", {
    scrollTrigger: {
        trigger: ".section-2",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    y: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-2 .image-content", {
    scrollTrigger: {
        trigger: ".section-2",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    y: -100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-3 .text-content", {
    scrollTrigger: {
        trigger: ".section-3",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: 100,
    opacity: 0,
    duration: 1,
});

gsap.from(".section-3 .image-content", {
    scrollTrigger: {
        trigger: ".section-3",
        start: "top center",
        end: "bottom center",
        scrub: true,
    },
    x: -100,
    opacity: 0,
    duration: 1,
});