
document.addEventListener("DOMContentLoaded", function () {
    const animalSelect = document.getElementById("animal");
    const checkboxes = document.querySelectorAll('input[name="symptoms"]');

    let referenceData = {};

    // JSON verisini yükle
    fetch("/static/reference_data.json")
        .then(response => response.json())
        .then(data => {
            referenceData = data;
            animalSelect.addEventListener("change", handleAnimalChange);
            handleAnimalChange(); // sayfa yüklendiğinde çalışsın
        });

    
    const referenceBox = document.getElementById("reference-info");
    let referenceDetails = {};

    fetch("/static/animal_info_reference.json")
        .then(response => response.json())
        .then(data => {
            referenceDetails = data;
        });

    function updateReferenceInfo(selectedAnimal) {
        const meta = referenceDetails[selectedAnimal];
        if (!meta) {
            referenceBox.innerHTML = "";
            return;
        }
        referenceBox.innerHTML = `
            <div class="info-section">
                <strong>Recommended age:</strong> ${meta.age[0]} – ${meta.age[1]}<br>
                <strong>Recommended temp:</strong> ${meta.temperature[0]} – ${meta.temperature[1]}
            </div>`;
    }


function handleAnimalChange() {
        const selectedAnimal = animalSelect.value.toLowerCase();
        updateReferenceInfo(selectedAnimal);
        const validSymptoms = referenceData[selectedAnimal] || [];

        checkboxes.forEach(cb => {
            if (validSymptoms.includes(cb.value.toLowerCase())) {
                cb.disabled = false;
                cb.parentElement.style.color = "";
            } else {
                cb.disabled = true;
                cb.checked = false;
                cb.parentElement.style.color = "#999";
            }
        });
    }
});
