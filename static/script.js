function validateForm() {
    let packet = document.getElementById("packet_rate").value;
    let cpu = document.getElementById("cpu").value;
    let memory = document.getElementById("memory").value;
    let alert = document.getElementById("alert").value;

    if (packet === "" || cpu === "" || memory === "" || alert === "") {
        alert("All fields are required!");
        return false;
    }

    if (packet < 0 || cpu < 0 || memory < 0 || alert < 0) {
        alert("Values cannot be negative!");
        return false;
    }

    if (cpu > 100 || memory > 100) {
        alert("CPU and Memory usage should be between 0 and 100");
        return false;
    }

    return true;
}

function showHint(inputId, limit) {
    let value = document.getElementById(inputId).value;
    if (value > limit) {
        document.getElementById(inputId).style.border = "2px solid red";
    } else {
        document.getElementById(inputId).style.border = "none";
    }
}
function goBack() {
    window.history.back();
}

function closePage() {
    window.location.href = "/dashboard";  
    
}