
// -------------------------function search bar-----------------------------

function filterComputers() {
    var input, filter, container, units, unit, i;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    container = document.getElementById("computerU nitsContainer");
    units = container.getElementsByClassName("computer-unit");

    for (i = 0; i < units.length; i++) {
        unit = units[i];
        if (unit.getAttribute("data-name").toUpperCase().indexOf(filter) > -1) {
            unit.style.display = "";
        } else {
            unit.style.display = "none";
        }
    }
}

// ----------------------------function for displaying the box------------------
function showPopup(unitElement) {
    const unitId = unitElement.getAttribute('data-id');
    const monitor = unitElement.getAttribute('data-monitor');
    const keyboard = unitElement.getAttribute('data-keyboard');
    const mouse = unitElement.getAttribute('data-mouse');
    const ram = unitElement.getAttribute('data-ram');
    const motherboard = unitElement.getAttribute('data-motherboard');
    const cpu = unitElement.getAttribute('data-cpu');
    const remarks = unitElement.getAttribute('data-remarks');
    const date = unitElement.getAttribute('data-date');

    document.getElementById('popupPcNumber').innerText = `Computer ${unitId}`;
    document.getElementById('popupMonitor').innerText = monitor;
    document.getElementById('popupKeyboard').innerText = keyboard;
    document.getElementById('popupMouse').innerText = mouse;
    document.getElementById('popupRam').innerText = ram;
    document.getElementById('popupMotherboard').innerText = motherboard;
    document.getElementById('popupCpu').innerText = cpu;
    document.getElementById('popupRemarks').innerText = remarks;
    document.getElementById('popupDate').innerText = date;

    document.querySelector('input[name="status_id"]').value = unitId; 
    document.getElementById('popupBox').style.display = 'block';
}

function closePopup() {
    document.getElementById('popupBox').style.display = 'none';
}


window.onclick = function(event) {
    if (event.target === document.getElementById("popupBox")) {
        closePopup();
    }
};

document.querySelector('.popup-content').onclick = function(event) {
    event.stopPropagation();
};



// ---------------------------------loading function-----------------------------



window.addEventListener('load', function() {
    setTimeout(function() {
        document.getElementById('loadingScreen').style.display = 'none';

        setTimeout(function() {
            welcomeAlert.classList.remove('show');
            welcomeAlert.classList.add('hide');
        }, 1000); 

        
        setTimeout(function() {
            welcomeAlert.style.display = 'none';
        }, 3500);
    }, 800); 
});

// ---------------------message alert------