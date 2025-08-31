document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("[data-target]").forEach(src => {
        const targetId = src.dataset.target;
        const tgt = document.getElementById(targetId);

        if (!tgt) return; // skip kalau target tidak ada

        function sync() {
            const newVal = src.value || src.textContent || src.innerText || "";
            if (tgt.value !== undefined) {
                tgt.value = newVal;
            } else {
                tgt.textContent = newVal;
            }
        }

        // jalankan sekali saat load
        sync();

        // kalau bisa diinput (tidak readonly), sync realtime
        if (!src.hasAttribute("readonly")) {
            src.addEventListener("input", sync);
        } else {
            // kalau readonly, pantau dengan MutationObserver
            const observer = new MutationObserver(sync);
            observer.observe(src, { attributes: true, attributeFilter: ["value"] });

            // jaga-jaga kalau ada perubahan manual lewat JS
            setInterval(sync, 1000);
        }
    });
});